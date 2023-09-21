# -*- coding: utf-8 -*-
import SparkApi
import sys
import ntchat

# 以下密钥信息从控制台获取
appid = "fd727d01"  # 填写控制台中获取的 APPID 信息
api_secret = "N2Q2MzM0ZmQ2MmEyMjdhNWZkMzM3Mzlm"  # 填写控制台中获取的 APISecret 信息
api_key = "4eccafc065aa5272a1502a61c724d7d9"  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
# domain = "general"   # v1.5版本
domain = "generalv2"  # v2.0版本
# 云端环境的服务地址
# Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

text = []


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while getlength(text) > 8000:
        del text[0]
    return text


wechat = ntchat.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)


# 注册消息回调
@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def on_recv_text_msg(wechat_instance: ntchat.WeChat, message):
    data = message["data"]
    print(data)
    from_wxid = data["from_wxid"]
    self_wxid = wechat_instance.get_login_info()["wxid"]
    room_wxid = data["room_wxid"]
    ccc = wechat_instance.get_rooms()
    print('***********',ccc,'***********')
    # 判断消息不是自己发的，并回复对方
    if from_wxid != self_wxid and not room_wxid:
        question = checklen(getText("user", f"{data['msg']}"))
        SparkApi.answer = ""
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        shuchu = getText('assistant', SparkApi.answer)
        # print('**********,', shuchu, '**********')
        shuchu = shuchu[-1]['content']
        wechat_instance.send_text(to_wxid=from_wxid, content=f"{shuchu}")

try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
