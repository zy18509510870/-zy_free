from wxauto import *


# 获取当前微信客户端
wx = WeChat()
who = '钟迅'
wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
for i in range(1,101):
    # 向某人发送消息（以`文件传输助手`为例）
    msg = '你好~'
    wx.SendMsg(msg)  # 向`文件传输助手`发送消息：你好~
