from PyWeChatSpy import WeChatSpy

def parser(data):
    # 获取文本信息
    if data.get("type") == 1:
        # spy.query_personal_info()  # 获取登录账号的个人信息
        print(data)  # 打印收到的信息
        if data.get('chatroom_ID'):  # 微信群消息
            chatroom_ID = data.get('chatroom_ID')  # 获取微信群id
            spy.send_text(chatroom_ID, '微信群消息自动回复测试！')  # 在此，你可以根据需要来设置消息的内容
        elif not data.get('chatroom_ID') and data.get('self') == 0:
            wx_ID = data.get('wx_ID')  # 好友消息
            spy.send_text(wx_ID, '好友消息自动回复测试！')  # 在此，你可以根据需要来设置消息的内容

    # 获取个人信息
    elif data.get("type") == 2:
        print(data)


if __name__ == '__main__':
    spy = WeChatSpy(parser=parser)
    spy.run()
