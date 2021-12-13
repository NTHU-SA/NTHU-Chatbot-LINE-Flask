from linebot.models import *

def qa_info():
    '''校園電話Q&A'''
    QuickReply_text_message = TextSendMessage(
        text = '請輸入想要查詢的單位名稱',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    image_url='https://i.imgur.com/szzgMji.png',
                    action = MessageAction(label = "校安中心", text = "校安中心"),
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/lwoIwZa.png',
                    action = MessageAction(label = "駐衛警察隊", text = "駐衛警察隊"),
                ),
                # QuickReplyButton(
                #     image_url='https://i.imgur.com/7wGbjZJ.png',
                #     action = MessageAction(label = "清華總機", text = "清華總機"),
                # )
            ]
        )
    )
    return QuickReply_text_message

def unit_phone_carousel(name, phone):

    bubble_json = '''
    {{
    "type": "bubble",
    "body": {{
    "type": "box",
    "layout": "vertical",
    "contents": [
        {{
        "type": "text",
        "text": "{name}",
        "adjustMode": "shrink-to-fit",
        "weight": "bold",
        "size": "xl"
        }},
        {{
        "type": "separator",
        "margin": "md"
        }},
        {{
        "type": "box",
        "layout": "horizontal",
        "contents": [
            {{
            "type": "text",
            "text": "電話：",
            "margin": "none"
            }},
            {{
            "type": "text",
            "text": "📞 {phone}",
            "align": "end"
            }}
        ],
        "margin": "lg"
        }},
        {{
        "type": "separator",
        "margin": "md"
        }},
        {{
        "type": "button",
        "action": {{
            "type": "uri",
            "label": "撥打電話",
            "uri": "tel://{phone}"
        }},
        "style": "secondary",
        "adjustMode": "shrink-to-fit",
        "margin": "lg",
        "height": "sm",
        "position": "relative"
        }}
        ]
        }}
    }}
    '''.format(name = name, phone = phone)

    return bubble_json