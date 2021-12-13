from linebot.models import *

def intro():
    QuickReply_text_message = TextSendMessage(
        text = '請輸入你想查詢的校園位置，本汪帶你走',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    action = MessageAction(label = "北校門", text = "北校門"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "小吃部", text = "小吃部"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "圖書館", text = "圖書館"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "人社院", text = "人社院"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "台積館", text = "台積館"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "南校門", text = "南校門"),
                )
            ]
        )
    )
    return QuickReply_text_message

def personal_intro(item):
    QuickReply_text_message = TextSendMessage(
            text = '請輸入你想查詢的校園位置，本汪帶你走',
            quick_reply = QuickReply(
                items = item
            )
        )
    return QuickReply_text_message

    
