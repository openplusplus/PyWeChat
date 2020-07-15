from ast import literal_eval
import json
import os
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep
from subprocess import Popen, PIPE
from .exceptions import handle_error_code
import logging
import warnings
import re
import threading

pattern = '[\u4e00-\u9fa5]'
formatter = logging.Formatter('%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)


class WeChatSpy:
    def __init__(self, parser=None, error_handle=None, multi=False):
        self.logger = logging.getLogger(__file__)
        self.logger.addHandler(sh)
        self.logger.setLevel(logging.DEBUG)
        # TODO: 异常处理函数
        self.__error_handle = error_handle
        # 是否多开微信PC客户端
        self.__multi = multi
        # socket数据处理函数
        self.__parser = parser
        self.__pid2client = {}
        self.__socket_server = socket(AF_INET, SOCK_STREAM)
        self.__socket_server.bind(("127.0.0.1", 9527))  # 绑定socket到微信端口
        self.__socket_server.listen(1)  # 开始监听微信
        t_start_server = Thread(target=self.__start_server)
        t_start_server.daemon = True
        t_start_server.name = "socket accept"
        t_start_server.start()

    def add_log_output_file(self, filename="spy.log", mode='a', encoding="utf8", delay=False, level="WARNING"):
        fh = logging.FileHandler(filename, mode=mode, encoding=encoding, delay=delay)
        if level.upper() == "DEBUG":
            fh.setLevel(logging.DEBUG)
        elif level.upper() == "INFO":
            fh.setLevel(logging.INFO)
        elif level.upper() == "WARNING":
            fh.setLevel(logging.WARNING)
        elif level.upper() == "ERROR":
            fh.setLevel(logging.ERROR)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def __start_server(self):
        while True:
            socket_client, client_address = self.__socket_server.accept()  # 接收微信客户端的连接
            t_socket_client_receive = Thread(target=self.receive, args=(socket_client,))
            t_socket_client_receive.name = f"client {client_address[1]}"
            t_socket_client_receive.daemon = True
            t_socket_client_receive.start()

    def __str_to_json(self, data):
        """
        把接收到的json字符串反序列化成python对象
        :param data:
        :return:
        """
        data_list = data.split(',"content":"')
        # print(data_list)
        if len(data_list) == 1:
            return literal_eval(data_list[0])
        elif len(data_list) == 2:
            data_info = data_list[0] + '}'
            data_json = literal_eval(data_info)
            content = data_list[1].strip('"}')
            data_json['content'] = content
            return data_json
        else:
            raise

    def receive(self, socket_client):
        while True:
            data_str = None
            try:
                data_str = socket_client.recv(4096).decode(encoding="utf-8", errors="ignore")
                # print(data_str)
            except Exception as e:
                for pid, client in self.__pid2client.items():
                    if client == socket_client:
                        self.__pid2client.pop(pid)
                        return self.logger.warning(f"A WeChat process (PID:{pid}) has disconnected: {e}")
                else:
                    pid = "unknown"
                    return self.logger.warning(f"A WeChat process (PID:{pid}) has disconnected: {e}")

            if data_str and data_str.endswith("*393545857*"):  # 防止socket黏包
                for data in data_str.split("*393545857*"):
                    if data:
                        try:
                            data = self.__str_to_json(data)
                            # data = literal_eval(data)
                            # print(data)
                            # print(type(data))
                        except:
                            self.logger.warning("接收数据解析出错！")
                            data = None
                        if data:
                            # print('socket_client:', socket_client)
                            # print(type(socket_client))
                            if not self.__pid2client.get(data["pid"]) and data["type"] == 200:
                                self.__pid2client[data["pid"]] = socket_client
                                self.logger.info(f"A WeChat process (PID:{data['pid']}) successfully connected")
                            if callable(self.__parser):
                                self.__parser(data)

    def __send(self, data, pid):
        if pid:
            socket_client = self.__pid2client.get(pid)
        else:
            socket_client_list = list(self.__pid2client.values())
            socket_client = socket_client_list[0] if socket_client_list else None
        if socket_client:
            # print(json.dumps(data))
            data = json.dumps(data, ensure_ascii=False)
            data_length_bytes = int.to_bytes(len(data.encode(encoding="utf-8")), length=4, byteorder="little")
            try:
                # socket_client.send(data_length_bytes + data.encode(encoding="utf8"))
                # print(data)
                # encode_str = data.encode(encoding="utf8")
                # unicode_str = data.encode(encoding='unicode-escape')
                # print(unicode_str)
                # print(encode_str)
                # socket_client.send(encode_str)
                # encode会把data字符串转成对应编码的bytes类型数据
                socket_client.send(data.encode(encoding="utf-8"))
                # socket_client.send(data)
            except Exception as e:
                for pid, v in self.__pid2client.items():
                    if v == socket_client:
                        self.__pid2client.pop(pid)
                        return self.logger.warning(f"A WeChat process (PID:{pid}) has disconnected: {e}")
                else:
                    pid = "unknown"
                    return self.logger.warning(f"A WeChat process (PID:{pid}) has disconnected: {e}")

    def run(self, background=False):
        # 注入当前目录下名字为：WeChatSpy.dll的dll
        current_path = os.path.split(os.path.abspath(__file__))[0]
        launcher_path = os.path.join(current_path, "Launcher.exe")
        cmd_str = f"{launcher_path} multi" if self.__multi else launcher_path
        p = Popen(cmd_str, shell=True, stdout=PIPE)
        res_code, err = p.communicate()
        res_code = res_code.decode()
        handle_error_code(res_code)
        # self.logger.info("Python server starts successfully.")
        if not background:
            while True:
                sleep(86400)

    def send_text(self, wxid, content, at_wxid="", pid=None):
        """
        发送文本消息
        :param wxid: 文本消息接收wxid（个人id或者群id）
        :param content: 文本消息内容
        :param at_wxid: 如果wxid为群wxid且需要@群成员 此参数为被@群成员wxid，以英文逗号分隔
        :param pid: 微信的进程id
        """
        if not wxid.endswith("chatroom"):
            at_wxid = ""
        data = {"code": 1, "wxid": wxid, "at_wxid": at_wxid, "content": content}
        self.__send(data, pid)

    def query_personal_info(self, pid=None):
        """
        获取个人信息
        :param pid: 微信的进程id
        :return:
        """
        data = {"code": 2}
        self.__send(data, pid)
