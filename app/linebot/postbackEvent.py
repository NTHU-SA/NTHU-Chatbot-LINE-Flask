from linebot.models import *

from app.linebot import line_bot_api, handler, user

from app.handler import PostbackHandler
from utils import postbackUtil

postback_handler = PostbackHandler(line_bot_api, user)

# 監聽 Postback
# Richmenu: epidemic
@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    param = postbackUtil.parse(data)

    postback_handler.run(event, param)