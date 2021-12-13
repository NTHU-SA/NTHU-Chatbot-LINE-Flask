from linebot.models import *

def stop_qa():
    text_template = TextSendMessage(text="狗狗了解！有問題歡迎再找本汪！")
    return text_template
def cancel_sign():
    text_template = TextSendMessage(text="狗狗了解！")
    return text_template