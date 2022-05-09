from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from NTUSTCourse import SearchCommon,SearchEnglish,SearchBeauty,programmerStory
#
from FinalSearchLocation import SearchLocation
app = Flask(__name__)
import requests
UserIdlist=[]
"""
CourseNum=['ADG015301', 'ADG018301', 'ADG020301', 'BAG004301', 'BAG005301', 'BAG006301', 'BAG007301', 'CEG321301', 'CEG323301', 'CHG303301', 'ECG003301', 'FBG006301', 'GE1515301', 'GE1515302', 'GE3401301', 'GE3401302', 'GE3402301', 'GE3405301', 'GE3405304', 'GE3407301', 'GE3604301', 'GE3605302', 'GE3606301', 'GE3642301', 'GE3700301', 'GE3708301', 'GE3708302', 'GE3709301', 'GE3709302', 'GE3710301', 'GE3710302', 'GE3711301', 'GE3711302', 'GE3714301', 'GE3714302', 'GE3719301', 'GE3719302', 'GE3723301', 'GE3723302', 'GE3724301', 'GE3724302', 'GE3725301', 'GE3727301', 'GE3727302', 'GE3728301', 'GE3728302', 'GE3728304', 'GE3729301', 'GE3729302', 'GE3900301', 'GE3900304', 'GE3901301', 'GE3901302', 'GE3901303', 'GE3903302', 'GE3907301', 'GE3907302', 'GE3909302', 'GE3909303', 'GE3909305', 'GE3909306', 'GE3917301', 'GE3917302', 'GE3931301', 'GE3931302', 'HCG015301', 'IBG006301', 'IBG007301',
'MBG204301', 'MBG204302', 'MEG302301', 'MEG302301', 'MEG302302', 'MEG302302', 'MIG001301', 'TCG003301', 'TCG033301', 'TCG034301', 'TCG035301', 'TCG036301', 'TCG037301', 'TCG039301', 'TCG040301', 'TCG045301', 'TCG046301', 'TCG047301', 'TCG047302', 'TCG048301', 'TCG056301', 'TCG058301', 'TCG062301', 'TCG063301', 'TCG065301', 'TCG068301', 'TCG072301', 'TCG073301', 'TCG074301', 'TCG075301', 'TCG078301', 'TCG079301', 'TCG080301', 'TCG082301', 'TCG084301', 'TCG085301', 'TCG086301', 'TCG087301', 'TCG088301', 'TCG093301', 'TCG094301', 'TCG095301', 'TCG096301', 'TCG097301', 'TCG098301', 'TCG099301', 'TCG100301', 'FE1041701', 'FE1041702', 'FE1041703', 'FE1042701', 'FE1042702', 'FE1043701', 'FE1044701', 'FE1045701', 'FE1051701', 'FE1062701', 'FE1071701', 'FE1071702', 'FE1071703', 'FE1072701', 'FE1081701', 'FE1112701', 'FE1112702', 'FE1112703', 'FE1151701', 'FE1151702', 'FE1151703', 'FE1151704', 
'FE1231701', 'FE1231702', 'FE1231703', 'FE1231704', 'FE1241701', 'FE1241702', 'FE1241703', 'FE1351701', 'FE1471701', 'FE1471702', 'FE1571701', 'FE1571702', 'FE1571703', 'FE1571704', 'FE1581701', 'FE1581702', 'FE1591701', 'FE1591702', 'FE1591703', 'FE1591704', 'FE1621701', 'FE1621702', 'FE1621703', 'FE1721701', 'FE1741701', 'FE1741702', 'FE1751701', 'FE1751702', 'FE1751703', 'FE1771701', 'FE1781701', 'FE1781702', 'FE1781703', 'FE1781704', 'FE1791701', 'FE1791702', 'FE1791703', 'FE1821701', 'FE1821702', 'FE1821703', 'FE1851701', 'FE1851702', 'FE1871701', 'FE1871702', 'FE1871703', 'FE1911701', 'FE1911702', 'FE1911703', 'FE1921701', 'FE1921702', 'FE1921703', 'FE1931701', 'FE1931702', 'FE1931703', 'FE1951701', 'FE1961701', 'FE1962701', 'FE2021701', 'FE2021702', 'FE2031701', 'FE2031702', 'FE2031703', 'FE2051701', 'FE2061701', 'FE2062701', 'FE2111701', 'FE2131701', 'FE2132701', 'FE2141701', 
'FE2141702', 'FE2151701', 'FE2171701', 'FE2172701', 'FL1006302', 'FL3323701', 'FL3402302', 'FL3800701', 'FL3805701', 'FL3805702', 'FL3813701', 'FL3830701', 'FL3833701', 'FL3833702', 'FL3833703', 'FL3833704', 'FL3833705', 'FL3833706', 'FL3833707', 'FL3841701', 'FL3841702', 'FL3846701', 'FL3846702', 'FL3848701']
"""
# Channel Access Token
line_bot_api = LineBotApi('/sPpeEPIru0m5P2txDoPBzwTqITRFouIV29npt1CKLc2AHDkZ4NQMQ8SEwL5AvvkR3WOWpG0x6hNxnc0d607un6mocArr3UzATzIASLWFgB9RSGy2Kf/2wx4PI82HYUEMoye/WxAuM4YwkEl5rj9eQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f031bd700ca4ac82cdf84e3cbc66518b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    UserQuery=event.message.text
    User_id=event.source.user_id
    profile = line_bot_api.get_profile(User_id)
    if User_id not in UserIdlist and profile.display_name!="李俊賢":
        UserIdlist.append(User_id)
    personalData="\n"+profile.display_name+"\n查詢: "+UserQuery
    requests.post('https://maker.ifttt.com/trigger/value1/with/key/c77uZwZ_UcVdPZ3wSq2jF2', data = {'value1':personalData})
    """
    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)
    print(profile.status_message)
    IFTTT
    requests.post('https://maker.ifttt.com/trigger/value1/with/key/c77uZwZ_UcVdPZ3wSq2jF2', data = {'value1':"this is a test"})
    """
    """
    if UserQuery.find("通識")>=0:
        message = TextSendMessage(text=SearchCommon())
        line_bot_api.reply_message(event.reply_token, message)
    elif UserQuery.find("英文")>=0:
        message = TextSendMessage(text=SearchEnglish())
        line_bot_api.reply_message(event.reply_token, message)
    """
    if UserQuery[0] =="!" or UserQuery[0]=="！":
        message = TextSendMessage(text=SearchLocation(UserQuery[1:]))
        line_bot_api.reply_message(event.reply_token, message)
    elif UserQuery.find("表特")>=0:
        message = TextSendMessage(text=SearchBeauty())
        line_bot_api.reply_message(event.reply_token, message)
    elif UserQuery.find("故事")>=0 or UserQuery.find("客家")>=0:
        message = TextSendMessage(text=programmerStory())
        line_bot_api.reply_message(event.reply_token, message)
    elif UserQuery.lower()=="help":
        message = TextSendMessage(text="目前功能有表特、故事、作者指令，\n在文字前加上\"!\"可以搜尋教室位置(\"!初級\"可以找到初級日文)\n可以找到所有台科的課，李俊賢超帥的啦!\n排版很醜我也沒辦法啦，我就客家人啦。")
        line_bot_api.reply_message(event.reply_token, message)
    elif UserQuery.find("作者")>=0:
        message = TextSendMessage(text='1.李俊賢 (184/65) \n 客家人、單身、無不良嗜好、有點裝會疼會癢 \n ig:gooseahead_ \n\n 2.姚佳均 (180/69) \n純情捲毛、程式很強 \n興趣是吵人跟寫很屌的程式 \nig:yyao_1120_')
        line_bot_api.reply_message(event.reply_token, message)
    elif UserQuery[0:9]=="advertise":
        message = TextSendMessage(text=UserQuery[10::])
        for to in UserIdlist:
            line_bot_api.push_message(to, message)
    else:
        message = TextSendMessage(text=UserQuery+"\n聽不懂的指令，細妹(小妹)只會學你說話拉，想了解目前有啥功能請打help")
        line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
