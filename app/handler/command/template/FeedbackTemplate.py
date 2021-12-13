from linebot.models import *

def get_feedback():
    return TextSendMessage(text='你有什麼意見或問題呢？告訴本汪，盡快為你處理！')