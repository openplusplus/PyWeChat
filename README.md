# PyWeChat
PC微信Hook逆向程序：Hook到微信消息，然后与Python程序进行交互。

## 支持的环境配置
* Windows系统
* Python 3.5以上

## 支持的微信版本
* [2.8.0.133](https://github.com/MaoningGuan/PyWeChat/raw/master/WeChat%202.8.0.133%20(Win%2C%2064bit).exe)

## [WeChatSpy.dll](https://github.com/MaoningGuan/PyWeChat/blob/master/PyWeChatSpy/1644691589/WeChatSpy.dll) 开发的源代码(C++)
* [https://github.com/MaoningGuan/WeChatSpy](https://github.com/MaoningGuan/WeChatSpy)

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
* `query_personal_info()` > 查询登录账号的个人信息
## 使用教程
1. git clone工程到本地之后，确保已经安装2.8.0.133版本的微信到电脑上，并且已经登录电脑微信。
2. cd到项目工程目录下，运行里面的使用示例example.py：
> ```python
> python example.py
> ```
3. 用另外一个微信给登录的电脑微信发送好友消息或者群消息，运行结果如下：
> * 显示接收到的微信消息：  
![](https://github.com/MaoningGuan/PyWeChat/blob/master/images/example1.png)  
> * 好友消息自动回复：    
![](https://github.com/MaoningGuan/PyWeChat/blob/master/images/example2.jpg)  
> * 微信群消息自动回复：    
![](https://github.com/MaoningGuan/PyWeChat/blob/master/images/example3.jpg)  

## 作者寄语
* 本项目完全开源，若你开发了更多的功能，可以pull request给我。
* 开源代码地址：[WeChatSpy.dll 开发的源代码(C++)](https://github.com/MaoningGuan/PyWeChat/blob/master/PyWeChatSpy/1644691589/WeChatSpy.dll) 
