''' flag handler 
    Flag Type:
        - andx_insert           : 新增笑話
        - feedback              : 問題回饋
        - epidemic_feedback     : 疫情新增問題
        - epidemic_qa           : 疫情Q&A
'''

from linebot.models import *

from app.handler.flag.template import EpidemicQATemplate, AffairQATemplate

from API import AndxAPI, FeedbackAPI, PhoneAPI
from qa_engine.engine import QA_Engine
from qa_engine.phone_engine import Phone_Engine
from utils import mapUtil
from API import UserAPI
from app.handler.richmenu.template import phoneT
import json


class FlagHandler():
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def _andx_insert(self, reply_token, user_id, message_text):
        andx = AndxAPI()
        err = andx.insertOne(user_id, message_text)
        if err:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text='新增笑話失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
            print(err)
        else:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text='狗狗情報員成功收到您的提供的趣聞！ 校園歡樂值+1'))
        self.user.initFlag(user_id)
        
    def _feedback(self, reply_token, user_id, message_text):
        fb = FeedbackAPI()
        err = fb.insertOne('normal', user_id, message_text)
        if err:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text="問題回饋失敗 嗷嗷qq。你可以寄信到 nthuchatbot@gmail.com或聯絡粉專，讓他們知道狀況！"))
            print(err)
        else:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text="謝謝您的回饋！我們會盡快改善，汪！"))
        self.user.initFlag(user_id)

    def _epidemic_feedback(self, reply_token, user_id, message_text):
        fb = FeedbackAPI()
        err = fb.insertOne('epidemic', user_id, message_text)
        if err:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text="問題回饋失敗 嗷嗷qq。你可以寄信到 nthuchatbot@gmail.com或聯絡粉專，讓他們知道狀況！"))
            print(err)
        else:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text="謝謝您的回饋及提問！本汪會盡快通知校方，更新第一手資訊！"))
        self.user.initFlag(user_id)

    def _epidemic_qa(self, reply_token, user_id, message_text):
        qa_engine = QA_Engine()
        qa_engine.load_data('epidemic')

        ans = qa_engine.match_ans(message_text)

        self.line_bot_api.reply_message(reply_token, EpidemicQATemplate.ans_and_confirm_btn(ans))
        self.user.initFlag(user_id)
    
    def _affair_qa(self, reply_token, user_id, message_text):
        qa_engine = QA_Engine()
        qa_engine.load_data('affair_all')

        ans = qa_engine.match_ans(message_text)

        self.line_bot_api.reply_message(reply_token, AffairQATemplate.ans_and_confirm_btn(ans))
        self.user.initFlag(user_id)

    def _mapping(self, reply_token, user_id, message_text):
        location = message_text
        mapInfo = mapUtil.mapping(location)
        if not mapInfo['isExist']:
            message = TextSendMessage(text=mapInfo['errMsg'])
            self.line_bot_api.reply_message(reply_token, message)
        else:
            err = self.user.mapRecordInsertOne(user_id,location)
            if err:
                self.line_bot_api.reply_message(reply_token, TextSendMessage(text=err))
            else:
                message = LocationSendMessage(
                    title = mapInfo['info']['title'],
                    address = mapInfo['info']['address'],
                    latitude = mapInfo['info']['latitude'],
                    longitude = mapInfo['info']['longitude']
                )
                self.line_bot_api.reply_message(reply_token, message)
        self.user.initFlag(user_id)

    def _get_phonelists(self, reply_token, user_id, message_text):
        qa_engine = Phone_Engine()
        qa_engine.load_data()

        name, phone, none_msg = qa_engine.match_ans(message_text)

        if none_msg:
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text=none_msg))
        else:
            unit_phone_carousel = phoneT.unit_phone_carousel(name, phone)
            self.line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text="校園單位電話", contents=json.loads(unit_phone_carousel)))
        self.user.initFlag(user_id)

    def run(self, event, flag):
        reply_token = event.reply_token
        user_id = event.source.user_id
        message_text = event.message.text

        if flag == "andx_insert":
            self._andx_insert(reply_token, user_id, message_text)
        elif flag == "feedback":
            self._feedback(reply_token, user_id, message_text)
        elif flag == "epidemic_feedback":
            self._epidemic_feedback(reply_token, user_id, message_text)
        elif flag == "epidemic_qa":
            self._epidemic_qa(reply_token, user_id, message_text)
        elif flag == "affair_qa":
            self._affair_qa(reply_token, user_id, message_text)
        elif flag == "mapping":
            self._mapping(reply_token, user_id, message_text)
        elif flag == "phone_qa":
            self._get_phonelists(reply_token, user_id, message_text)