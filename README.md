# PyWeChat
PC微信Hook程序：Hook到微信消息，然后与Python程序进行交互。

##支持微信版本
* 2.8.0.133

## 返回数据样例
* ‘{'pid': , 'type': 1, 'chatroom_ID': '', 'wx_ID': '', 'content': ''}’ >微信文本消息 
* ‘{'pid': , 'type': 2, 'wx_ID': '', 'nickname': '', 'account': '', 'phone': '', 'province': '', 'city': '', 'device': '', 'avatar': '’ >用户个人信息

## 功能列表
* `send_text(wxid, content, at_wxid="")` >发送文本
* `query_personal_info()` >查询用户个人信息
