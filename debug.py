from PyWeChatSpy import WeChatSpy
import threading


def parser(data):
    # 微信信息
    if data.get("type") == 1:
            length = len(threading.enumerate())  # 枚举返回个列表
            print("线程数量：", length)
            print(data)
            spy.send_text(data.get('wx_ID'), "python server已接收到消息！")
            # spy.query_personal_info()  # 获取用户个人信息

    # 用户个人信息
    elif data.get("type") == 2:
        print(data)


if __name__ == '__main__':
    spy = WeChatSpy(parser=parser)
    spy.run()
