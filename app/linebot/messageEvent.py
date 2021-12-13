from linebot.models import *

from app.linebot import line_bot_api, handler, user
from app.handler import RichmenuHandler, FlagHandler, CmdHandler
# from richmenu.handler import RichmenuHandler, PostbackHandler
# from flag.handler import FlagHandler
# from command.handler import CmdHandler

cmd_handler = CmdHandler(line_bot_api, user)
richmenu_handler = RichmenuHandler(line_bot_api, user)
flag_handler = FlagHandler(line_bot_api, user)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id  #使用者ID
    message_text = event.message.text  #使用者訊息
    
    flag, err = user.getFlag(user_id)
    if err:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="訊息處理失敗 嗷嗷qq。你可以寄信到 nthuchatbot@gmail.com或聯絡粉專，讓他們知道狀況！"))

    print('user_id: ', user_id)
    print('flag: ', flag)
    print('message_text: ', message_text)

    # 指令事件
    if cmd_handler.detect(message_text):
        user.initFlag(user_id)
        cmd_handler.run(event, message_text)

    # 選單事件
    elif richmenu_handler.detect(message_text):
        print('is richmenu:', richmenu_handler.detect(message_text))
        user.initFlag(user_id)
        richmenu_handler.run(event, message_text)
    
    # flag流程
    elif flag != 'init':
        flag_handler.run(event, flag)