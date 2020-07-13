from PyWeChatSpy import WeChatSpy
import threading

OWNER_WX_ID = 'wxid_5d7paxx35o8h22'


def parser(data):
    # 打印接收信息
    # print('接收的文本信息：', data)

    # 文本信息
    if data.get("type") == 1:
        if data.get('wx_ID') == OWNER_WX_ID:
            length = len(threading.enumerate())  # 枚举返回个列表
            print("线程数量：", length)
            print(data)
            # print(type(data))
            print('-----------------')
            # pass
            if data.get('chatroom_ID') != '':
                spy.send_text(data.get('chatroom_ID'), "接收到群消息")
            else:
                spy.send_text(data.get('wx_ID'), "接收到个人消息")
                spy.query_personal_info()
    # 个人信息
    elif data.get("type") == 2:
        print(data)



if __name__ == '__main__':
    spy = WeChatSpy(parser=parser)
    spy.run()
