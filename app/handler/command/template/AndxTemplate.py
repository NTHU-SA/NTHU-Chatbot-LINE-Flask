from linebot.models import *

def none_anecdote():
    return TextSendMessage(text='沒找到笑話')

def get_anecdote(content):
    return TextSendMessage(text=content)

def add_anecdote():
    return TextSendMessage(text='說吧！有什麼笑話這麼好笑？')