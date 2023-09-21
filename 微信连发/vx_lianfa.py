# -*- coding: utf-8 -*-
import sys
import ntchat

wechat = ntchat.WeChat()
# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)
# 等待登录
wechat.wait_login()
# 向微信群发送一条消息
for i in range(1,101):
    wechat.send_text(to_wxid="18601263348@chatroom", content="hello, filehelper")

try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()