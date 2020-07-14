# PyWeChat
PC微信Hook程序：Hook到微信消息，然后与Python程序进行交互。

## 支持微信版本
* [2.8.0.133](https://github.com/MaoningGuan/PyWeChat/raw/master/WeChat%202.8.0.133%20(Win%2C%2064bit).exe)

## [WeChatSpy.dll](https://github.com/MaoningGuan/PyWeChat/blob/master/PyWeChatSpy/1644691589/WeChatSpy.dll) 开发的源代码(C++)
[https://github.com/MaoningGuan/WeChatSpy](https://github.com/MaoningGuan/WeChatSpy)

## 返回数据样例
* `{'pid': , 'self': , 'type': 1, 'msg_type': , 'chatroom_ID': '', '': '', 'content': ''}` > 微信消息 
  * `self`类型说明：
    * 1 消息由当前登录账号发出
    * 0 消息由他人发出
  * `msg_type`类型说明：
    * 1 文本消息
    * 3 图片消息
    * 37 好友申请消息
	* ...
* `{'pid': , 'type': 2, 'wx_ID': '', 'nickname': '', 'account': '', 'phone': '', 'province': '', 'city': '', 'device': '', 'avatar': ''` > 用户个人信息

## 功能列表
* `send_text(wxid, content, at_wxid="")` > 发送文本，暂不支持@某个人
* `query_personal_info()` > 查询用户个人信息
