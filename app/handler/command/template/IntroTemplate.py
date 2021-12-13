from linebot.models import *

def intro_carousel():
    carousel_template = TemplateSendMessage(        
        alt_text = '下指令給狗狗情報員',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '分享狗狗情報員',
                    text = '快讓更多朋友認識我吧！\n @nthuchatbot',
                    actions = [
                        PostbackTemplateAction(
                            label='分享給好友',
                            data='source=richmenu&flag=intro&info=share'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '笑一下',
                    text = '聽聽四散在校園的奇聞軼事吧！讓自己輕鬆一下！',
                    actions = [
                        MessageTemplateAction(
                            label='笑一下',
                            text='!笑一下'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '新增笑話',
                    text = '告訴狗狗情報員關於你在校園生活中的笑料，讓校園充滿歡笑吧！',
                    actions = [
                        MessageTemplateAction(
                            label='新增笑話',
                            text='!新增笑話'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '問題回饋',
                    text = '我跟校園狗狗情報員溝通不良，想要回報問題或提供意見',
                    actions = [
                        MessageTemplateAction(
                            label='問題回饋',
                            text='!問題回饋'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '2020清大新生領航營',
                    text = '點我入新生領航營',
                    actions = [
                        MessageTemplateAction(
                            label='點我進入',
                            text='!新生領航營'
                        )
                    ]
                )
            ]
        )
    )

    return carousel_template

# def share_template():
#     QuickReply_text_message = TextSendMessage(
#         text = '太讚了！請問您想要如何分享我呢？',
#         quick_reply = QuickReply(
#             items = [
#                 QuickReplyButton(
#                     image_url='https://i.imgur.com/pHV1IIF.png',
#                     action = URIAction(label = "分享給LINE好友", uri = 'https://line.me/R/nv/recommendOA/@nthuchatbot'),
#                 ),
#                 QuickReplyButton(
#                     image_url='https://i.imgur.com/5I5Xi5E.png',
#                     action = PostbackAction(label = "QRcode分享", data = 'source=richmenu&flag=intro&info=qrcode')
#                 )
#             ]
#         )
#     )
#     return QuickReply_text_message

def share_template():
    bubble_json = '''
    {{
        "type": "bubble",
        "size": "mega",
        "header": {{
            "type": "box",
            "layout": "baseline",
            "contents": [
            {{
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "offsetStart": "10px"
            }},
            {{
                "type": "text",
                "text": "掃描加入 — 清華校園情報員",
                "offsetStart": "25px",
                "color": "#FFFFFF",
                "weight": "bold",
                "adjustMode": "shrink-to-fit"
            }}
            ],
            "backgroundColor": "#6F00D2",
            "borderWidth": "none",
            "cornerRadius": "none",
            "offsetTop": "none"
        }},
        "hero": {{
            "type": "image",
            "url": "https://i.imgur.com/40t9Qo0.png",
            "position": "relative",
            "margin": "none",
            "align": "center",
            "gravity": "center",
            "offsetTop": "lg",
            "size": "5xl"
        }},
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "@nthuchatbot",
                "color": "#7B7B7B",
                "align": "center",
                "size": "md",
                "offsetTop": "none"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [],
                "justifyContent": "center",
                "alignItems": "center",
                "offsetEnd": "none",
                "offsetBottom": "md",
                "spacing": "none",
                "margin": "lg",
                "borderWidth": "none",
                "cornerRadius": "none",
                "paddingBottom": "none",
                "paddingTop": "none",
                "paddingAll": "none",
                "paddingStart": "none"
            }},
            {{
                "type": "button",
                "action": {{
                "type": "uri",
                "label": "分享給LINE好友",
                "uri": "https://line.me/R/nv/recommendOA/@nthuchatbot"
                }},
                "style": "secondary",
                "height": "sm",
                "offsetTop": "sm",
                "margin": "none"
            }}
            ],
            "spacing": "none",
            "margin": "none",
            "borderWidth": "none",
            "offsetBottom": "sm",
            "offsetTop": "none",
            "paddingBottom": "xxl"
        }}
    }}
    '''.format()

    return bubble_json