# PyWeChat
PC微信Hook程序：Hook到微信消息，然后与Python程序进行交互。

## 支持微信版本
* 2.8.0.133

## WeChatSpy.dll开发的源代码(C++)
[https://github.com/MaoningGuan/WeChatSpy](https://github.com/MaoningGuan/WeChatSpy)

## 返回数据样例
* ‘{'pid': , 'self': , 'type': 1, 'msg_type': , 'chatroom_ID': '', '': '', 'content': ''}’ > 微信消息 
* 'self = 1: 代表消息由用户自己发出'
* 'self = 0: 代表消息由其他人发出'
* ‘msg_type: 代表消息类型’
* ‘{'pid': , 'type': 2, 'wx_ID': '', 'nickname': '', 'account': '', 'phone': '', 'province': '', 'city': '', 'device': '', 'avatar': '’ > 用户个人信息

## 功能列表
* `send_text(wxid, content, at_wxid="")` > 发送文本，暂不支持@某个人
* `query_personal_info()` > 查询用户个人信息
