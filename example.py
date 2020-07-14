from PyWeChatSpy import WeChatSpy

def parser(data):
    # 获取文本信息
    if data.get("type") == 1:
        print(data)
        # spy.query_personal_info()  # 获取个人信息

    # 获取个人信息
    elif data.get("type") == 2:
        print(data)


if __name__ == '__main__':
    spy = WeChatSpy(parser=parser)
    spy.run()
