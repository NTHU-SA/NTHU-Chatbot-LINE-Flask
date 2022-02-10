''' Chatbot command  '''
from linebot.models import *

from app.handler.command.template import AndxTemplate, FeedbackTemplate, IntroTemplate, LinggleTemplate
from app.handler.richmenu.template import pointT

from API import AndxAPI


class CmdHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance
    
    def detect(self, msg):
        '''判斷是否為chatbot command
            Params:
                - msg
            Return:
                - isCMD(bool): 若!在第一個字元
        '''

        if msg[0]=='!' or msg[0]=='！':
            return True
        else:
            return False

    def extract_msg(self, msg):
        if msg[0]=='!':
            return msg.split("!")[1]
        elif msg[0]=='！':
            return msg.split("！")[1]

    def run(self, event, msg):
        user_id = event.source.user_id
        reply_token = event.reply_token

        # intro all cmd of chatbot
        if msg=='!' or msg=='！':
            self.line_bot_api.reply_message(reply_token, IntroTemplate.intro_carousel())
        # 執行 cmd    
        else:
            em = self.extract_msg(msg)

            if em == "笑一下":
                andx = AndxAPI()
                anecdote, err = andx.getOne()
                if err:
                    self.line_bot_api.reply_message(reply_token, AndxTemplate.none_anecdote())
                    print(err)
                else:
                    anec_content = AndxTemplate.get_anecdote(anecdote)
                    self.line_bot_api.reply_message(reply_token, anec_content)
            
            elif em == "新增笑話":
                self.line_bot_api.reply_message(reply_token, AndxTemplate.add_anecdote())
                self.user.setFlag(user_id, 'andx_insert')
            
            elif em == "問題回饋":
                self.line_bot_api.reply_message(reply_token, FeedbackTemplate.get_feedback())
                self.user.setFlag(user_id, 'feedback')

        
    