from linebot.models import *
from datetime import date
from datetime import datetime

def isExisted():
    text_template = TextSendMessage(text="您已註冊！前往時間銀行專區")
    return text_template

def notActive():
    text_template = TextSendMessage(text="您尚未認證您的帳號，請前往點選認證信連結後再回來唷！")
    return text_template

def signup_email():
    text_template = TextSendMessage(text="請輸入您的學校信箱來進行下一步註冊")
    return text_template

def signup_name():
    text_template = TextSendMessage(text="請輸入您的暱稱來完成註冊")
    return text_template

def no_demands():
    text_template = TextSendMessage(text="目前沒有任何可媒合的需求唷！")
    return text_template

def is_matched():
    text_template = TextSendMessage(text="哎呀！該需求已被媒合！")
    return text_template

def is_conflicted():
    text_template = TextSendMessage(text="哎呀！您不能回覆自己的需求！")
    return text_template

def no_url():
    text_template = TextSendMessage(text="目前刊登中並無互動留言板！")
    return text_template

def no_match():
    text_template = TextSendMessage(text="目前刊登中，無法完成需求！")
    return text_template

def demand_complete(demand):
    demand_id = str(demand['id'])
    if demand['type'] == 'intern_chat':
        demand_type = '實習經驗一對一對談 ' + demand_id
    elif demand['type'] == 'traffic_chat':
        demand_type = '交通資訊 ' + demand_id

    text_template = TextSendMessage(text= demand_type + '，完成！')

    return text_template

def list_carousel(): # 實習交通分類
    carousel_template = TemplateSendMessage(        
        alt_text = '需求列表',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '實習資訊需求列表',
                    text = '查看更多實習資訊需求',
                    thumbnail_image_url='https://i.imgur.com/idSUvAh.png',
                    actions = [
                        PostbackTemplateAction(
                            label='查看實習需求',
                            data='source=richmenu&flag=list&info=intern'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '交通資訊需求列表',
                    text = '查看更多交通資訊需求',
                    thumbnail_image_url='https://i.imgur.com/Eu83Ync.png',
                    actions = [
                        PostbackTemplateAction(
                            label='查看交通需求',
                            data='source=richmenu&flag=list&info=traffic'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template

def intern_demand_carousel(): # 實習類別
    carousel_template = TemplateSendMessage(        
        alt_text = '實習需求列表',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '實習需求列表',
                    text = '點選查看想要協助的實習需求類別',
                    actions = [
                        PostbackTemplateAction(
                            label='實習一對一對談',
                            data='source=richmenu&flag=demand&info=intern_chat'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template

def traffic_demand_carousel(): # 交通類別
    carousel_template = TemplateSendMessage(        
        alt_text = '交通需求列表',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '交通需求列表',
                    text = '點選查看想要協助的交通需求類別',
                    actions = [
                        PostbackTemplateAction(
                            label='交通資訊',
                            data='source=richmenu&flag=demand&info=traffic_chat'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template

def intern_chat_carousel(intern_demands): # 實習經驗對談列表
    demands_list = []

    data_blocks = []
    while len(intern_demands) > 10:
        data_blocks.append(intern_demands[0:10])
        intern_demands = intern_demands[10:len(intern_demands)]
    data_blocks.append(intern_demands)

    for block in data_blocks:
        columns = []
        for item in block:
            demand_id = item['id']
            demand_title = '實習經驗一對一對談 ' + str(demand_id)
            demand_desc = '發佈時間：' + item['created_datetime'] + '\n產業類別：' + item['content']['industry'] + '\n公司名稱：' + item['content']['company']

            col = CarouselColumn(
                title= demand_title,
                text= demand_desc,
                actions=[
                    PostbackTemplateAction(
                        label='顯示需求詳細資訊',
                        data='source=richmenu&flag=demand&info=intern_chat_content_' + str(demand_id)
                    ),
                    PostbackTemplateAction(
                        label='我要協助',
                        data='source=richmenu&flag=demand&info=intern_chat_confirm_' + str(demand_id)
                    )
                ]
            )
            columns.append(col)

        carousel_template = TemplateSendMessage(
            alt_text='實習經驗一對一對談需求列表',
            template=CarouselTemplate(
                columns=columns
            )
        )
        demands_list.append(carousel_template)

    return demands_list

def traffic_chat_carousel(intern_demands): # 實習經驗對談列表
    demands_list = []

    data_blocks = []
    while len(intern_demands) > 10:
        data_blocks.append(intern_demands[0:10])
        intern_demands = intern_demands[10:len(intern_demands)]
    data_blocks.append(intern_demands)

    for block in data_blocks:
        columns = []
        for item in block:
            demand_id = item['id']
            demand_title = '交通資訊 ' + str(demand_id)
            demand_desc = '發佈時間：' + item['created_datetime'] + '\n出發地：' + item['content']['start'] + '\n目的地：' + item['content']['end']

            col = CarouselColumn(
                title= demand_title,
                text= demand_desc,
                actions=[
                    PostbackTemplateAction(
                        label='顯示需求詳細資訊',
                        data='source=richmenu&flag=demand&info=traffic_chat_content_' + str(demand_id)
                    ),
                    PostbackTemplateAction(
                        label='我要協助',
                        data='source=richmenu&flag=demand&info=traffic_chat_confirm_' + str(demand_id)
                    )
                ]
            )
            columns.append(col)

        carousel_template = TemplateSendMessage(
            alt_text='交通資訊需求列表',
            template=CarouselTemplate(
                columns=columns
            )
        )
        demands_list.append(carousel_template)

    return demands_list

def intern_demand_content(intern_demands): # 回覆顯示單一需求之內容
    
    demand_id = str(intern_demands['id'])
    industry = intern_demands['content']['industry']
    company = intern_demands['content']['company']
    background = intern_demands['content']['background']
    question = intern_demands['content']['question']
    confirm_data = 'source=richmenu&flag=demand&info=intern_chat_confirm_' + demand_id

    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "需求詳細資訊",
                "size": "lg",
                "color": "#4B0091",
                "weight": "regular"
            }},
            {{
                "type": "separator",
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "需求編號："
                }},
                {{
                    "type": "text",
                    "text": "{demand_id}",
                    "align": "end"
                }}
                ],
                "margin": "xxl"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "產業類別："
                }},
                {{
                    "type": "text",
                    "text": "{industry}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "公司名稱："
                }},
                {{
                    "type": "text",
                    "text": "{company}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "背景領域："
                }},
                {{
                    "type": "text",
                    "text": "{background}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "問題："
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "text",
                "text": "{question}",
                "margin": "lg",
                "wrap": true,
                "maxLines": 0,
                "adjustMode": "shrink-to-fit",
                "align": "start"
            }},
            {{
            "type": "button",
            "action": {{
                "type": "postback",
                "label": "我要協助",
                "data": "{confirm_data}"
            }},
            "style": "secondary",
            "offsetTop": "md",
            "height": "sm",
            "margin": "lg"
            }}
            ]
        }}
    }}
    '''.format(demand_id= demand_id, industry= industry, company= company, background= background, question= question, confirm_data= confirm_data)
    
    return bubble_json

    # demand_content = '需求編號：' + demand_id + '\n產業類別：' + industry + '\n公司名稱：' + company + '\n背景：' + background + '\n問題：' + question  
    # text_template = TextSendMessage(text=demand_content)
    # return text_template

def traffic_demand_content(intern_demands): # 回覆顯示單一需求之內容
    
    demand_id = str(intern_demands['id'])
    start = intern_demands['content']['start']
    end = intern_demands['content']['end']
    date = intern_demands['content']['date']
    time = intern_demands['content']['time']
    additional_info = intern_demands['content']['additional_info']
    confirm_data = 'source=richmenu&flag=demand&info=traffic_chat_confirm_' + demand_id

    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
        "type": "box",
        "layout": "vertical",
        "contents": [
            {{
            "type": "text",
            "text": "需求詳細資訊",
            "size": "lg",
            "color": "#4B0091",
            "weight": "regular"
            }},
            {{
            "type": "separator",
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "需求編號："
                }},
                {{
                "type": "text",
                "text": "{demand_id}",
                "align": "end"
                }}
            ],
            "margin": "xxl"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發地："
                }},
                {{
                "type": "text",
                "text": "{start}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "目的地："
                }},
                {{
                "type": "text",
                "text": "{end}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發日期："
                }},
                {{
                "type": "text",
                "text": "{date}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發時間："
                }},
                {{
                "type": "text",
                "text": "{time}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "備註："
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "text",
            "text": "{additional_info}",
            "margin": "lg",
            "wrap": true,
            "maxLines": 0,
            "adjustMode": "shrink-to-fit",
            "align": "start"
            }},
            {{
            "type": "button",
            "action": {{
                "type": "postback",
                "label": "我要協助",
                "data": "{confirm_data}"
            }},
            "style": "secondary",
            "offsetTop": "md",
            "height": "sm",
            "margin": "lg"
            }}
        ]
        }}
    }}
    '''.format(demand_id= demand_id, start= start, end= end, date= date, time= time, additional_info= additional_info, confirm_data= confirm_data)
    
    return bubble_json

def intern_published_demands_content(published_demand):
    demand_id = str(published_demand['id'])
    industry = published_demand['content']['industry']
    company = published_demand['content']['company']
    background = published_demand['content']['background']
    question = published_demand['content']['question']
    
    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "需求詳細資訊",
                "size": "lg",
                "color": "#4B0091",
                "weight": "regular"
            }},
            {{
                "type": "separator",
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "需求編號："
                }},
                {{
                    "type": "text",
                    "text": "{demand_id}",
                    "align": "end"
                }}
                ],
                "margin": "xxl"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "產業類別："
                }},
                {{
                    "type": "text",
                    "text": "{industry}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "公司名稱："
                }},
                {{
                    "type": "text",
                    "text": "{company}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "背景領域："
                }},
                {{
                    "type": "text",
                    "text": "{background}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "問題："
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "text",
                "text": "{question}",
                "margin": "lg",
                "wrap": true,
                "maxLines": 0,
                "adjustMode": "shrink-to-fit",
                "align": "start"
            }}
            ]
        }}
    }}
    '''.format(demand_id= demand_id, industry= industry, company= company, background= background, question= question)
    
    return bubble_json

def traffic_published_demands_content(published_demand):
    demand_id = str(published_demand['id'])
    start = published_demand['content']['start']
    end = published_demand['content']['end']
    date = published_demand['content']['date']
    time = published_demand['content']['time']
    additional_info = published_demand['content']['additional_info']

    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
        "type": "box",
        "layout": "vertical",
        "contents": [
            {{
            "type": "text",
            "text": "需求詳細資訊",
            "size": "lg",
            "color": "#4B0091",
            "weight": "regular"
            }},
            {{
            "type": "separator",
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "需求編號："
                }},
                {{
                "type": "text",
                "text": "{demand_id}",
                "align": "end"
                }}
            ],
            "margin": "xxl"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發地："
                }},
                {{
                "type": "text",
                "text": "{start}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "目的地："
                }},
                {{
                "type": "text",
                "text": "{end}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發日期："
                }},
                {{
                "type": "text",
                "text": "{date}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發時間："
                }},
                {{
                "type": "text",
                "text": "{time}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "備註："
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "text",
            "text": "{additional_info}",
            "margin": "lg",
            "wrap": true,
            "maxLines": 0,
            "adjustMode": "shrink-to-fit",
            "align": "start"
            }}
        ]
        }}
    }}
    '''.format(demand_id= demand_id, start= start, end= end, date= date, time= time, additional_info= additional_info)
    
    return bubble_json

def intern_helped_demands_content(helped_demand):
    demand_id = str(helped_demand['id'])
    industry = helped_demand['content']['industry']
    company = helped_demand['content']['company']
    background = helped_demand['content']['background']
    question = helped_demand['content']['question']
    
    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "需求詳細資訊",
                "size": "lg",
                "color": "#4B0091",
                "weight": "regular"
            }},
            {{
                "type": "separator",
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "需求編號："
                }},
                {{
                    "type": "text",
                    "text": "{demand_id}",
                    "align": "end"
                }}
                ],
                "margin": "xxl"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "產業類別："
                }},
                {{
                    "type": "text",
                    "text": "{industry}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "公司名稱："
                }},
                {{
                    "type": "text",
                    "text": "{company}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "背景領域："
                }},
                {{
                    "type": "text",
                    "text": "{background}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "問題："
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "text",
                "text": "{question}",
                "margin": "lg",
                "wrap": true,
                "maxLines": 0,
                "adjustMode": "shrink-to-fit",
                "align": "start"
            }}
            ]
        }}
    }}
    '''.format(demand_id= demand_id, industry= industry, company= company, background= background, question= question)
    
    return bubble_json

def traffic_helped_demands_content(helped_demand):
    demand_id = str(helped_demand['id'])
    start = helped_demand['content']['start']
    end = helped_demand['content']['end']
    date = helped_demand['content']['date']
    time = helped_demand['content']['time']
    additional_info = helped_demand['content']['additional_info']

    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
        "type": "box",
        "layout": "vertical",
        "contents": [
            {{
            "type": "text",
            "text": "需求詳細資訊",
            "size": "lg",
            "color": "#4B0091",
            "weight": "regular"
            }},
            {{
            "type": "separator",
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "需求編號："
                }},
                {{
                "type": "text",
                "text": "{demand_id}",
                "align": "end"
                }}
            ],
            "margin": "xxl"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發地："
                }},
                {{
                "type": "text",
                "text": "{start}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "目的地："
                }},
                {{
                "type": "text",
                "text": "{end}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發日期："
                }},
                {{
                "type": "text",
                "text": "{date}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "出發時間："
                }},
                {{
                "type": "text",
                "text": "{time}",
                "align": "end"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "備註："
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "text",
            "text": "{additional_info}",
            "margin": "lg",
            "wrap": true,
            "maxLines": 0,
            "adjustMode": "shrink-to-fit",
            "align": "start"
            }}
        ]
        }}
    }}
    '''.format(demand_id= demand_id, start= start, end= end, date= date, time= time, additional_info= additional_info)
    
    return bubble_json

def intern_help_confirm(intern_demands): # 實習需求匹配確認
    demand_id = str(intern_demands['id'])
    QuickReply_text_message = TextSendMessage(
        text = '您確定要協助 實習經驗一對一對談 ' + demand_id + '？',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    image_url = 'https://i.imgur.com/K5S5y6a.png',
                    action = PostbackAction(label = "沒錯", data = 'source=richmenu&flag=demand&info=intern_chat_help_' + str(demand_id))
                ),
                QuickReplyButton(
                    image_url = 'https://i.imgur.com/GyvJ3qT.png',
                    action = MessageAction(label = "先不要", text = '先不要')
                )
            ]
        )
    )
    return QuickReply_text_message

def traffic_help_confirm(traffic_demands): # 交通需求匹配確認
    demand_id = str(traffic_demands['id'])
    QuickReply_text_message = TextSendMessage(
        text = '您確定要協助 交通資訊 ' + demand_id + '？',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    image_url = 'https://i.imgur.com/K5S5y6a.png',
                    action = PostbackAction(label = "沒錯", data = 'source=richmenu&flag=demand&info=traffic_chat_help_' + str(demand_id))
                ),
                QuickReplyButton(
                    image_url = 'https://i.imgur.com/GyvJ3qT.png',
                    action = MessageAction(label = "先不要", text = '先不要')
                )
            ]
        )
    )
    return QuickReply_text_message

def complete_confirm(demand): # 需求匹配確認
    demand_id = str(demand['id'])
    if demand['type'] == 'intern_chat':
        demand_type = '實習經驗一對一對談 ' + demand_id
    elif demand['type'] == 'traffic_chat':
        demand_type = '交通資訊 ' + demand_id
    QuickReply_text_message = TextSendMessage(
        text = '您確定要完成' + demand_type + '？',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    image_url = 'https://i.imgur.com/K5S5y6a.png',
                    action = PostbackAction(label = "沒錯", data = 'source=richmenu&flag=demand&info=demand_complete_' + str(demand_id))
                ),
                QuickReplyButton(
                    image_url = 'https://i.imgur.com/GyvJ3qT.png',
                    action = MessageAction(label = "先不要", text = '先不要')
                )
            ]
        )
    )
    return QuickReply_text_message

def published_demands(published_demands): # 個人刊登需求
    demands_list = []

    data_blocks = []
    while len(published_demands) > 10:
        data_blocks.append(published_demands[0:10])
        published_demands = published_demands[10:len(published_demands)]
    data_blocks.append(published_demands)

    for block in data_blocks:
        columns = []
        for item in block:
            demand_id = item['id']

            if item['type'] == 'intern_chat':
                type_name = '實習經驗一對一對談 '
            elif item['type'] == 'traffic_chat':
                type_name = '交通資訊 '
            demand_title = type_name + str(demand_id)

            if item['status'] == 0:
                status = '刊登中'
            elif item['status'] == 1:
                status = '正在進行'
            elif item['status'] == 2:
                status = '已完成'

            demand_desc = '發佈時間：' + item['created_datetime'] + '\n狀態：' + status

            if len(item['match_info']) != 0 and item['status'] != 0:
                demand_url = item['match_info']['doc_url']
                action_list = [
                    PostbackTemplateAction(
                        label='顯示需求詳細資訊',
                        data='source=richmenu&flag=demand&info=published_demand_content_' + str(demand_id)
                    ),
                    URITemplateAction(
                        label='互動留言版',
                        uri=demand_url
                    ),
                    PostbackTemplateAction(
                        label='完成需求',
                        data='source=richmenu&flag=demand&info=demand_complete_confirm_' + str(demand_id)
                    )
                ]
            else:
                action_list = [
                    PostbackTemplateAction(
                        label='顯示需求詳細資訊',
                        data='source=richmenu&flag=demand&info=published_demand_content_' + str(demand_id)
                    ),
                    PostbackTemplateAction(
                        label='互動留言版',
                        data='source=richmenu&flag=demand&info=no_url'
                    ),
                    PostbackTemplateAction(
                        label='完成需求',
                        data='source=richmenu&flag=demand&info=no_match'
                    )
                ]
            
            col = CarouselColumn(
                title= demand_title,
                text= demand_desc,
                actions= action_list
            )
            columns.append(col)

        carousel_template = TemplateSendMessage(
            alt_text='刊登紀錄需求列表',
            template=CarouselTemplate(
                columns=columns
            )
        )
        demands_list.append(carousel_template)
    
    return demands_list

def helped_demands(helped_demands): # 個人協助需求
    demands_list = []

    data_blocks = []
    while len(helped_demands) > 10:
        data_blocks.append(helped_demands[0:10])
        helped_demands = helped_demands[10:len(helped_demands)]
    data_blocks.append(helped_demands)

    for block in data_blocks:
        columns = []
        for item in block:
            demand_id = item['id']
            
            if item['type'] == 'intern_chat':
                type_name = '實習經驗一對一對談 '
            elif item['type'] == 'traffic_chat':
                type_name = '交通資訊 '
            
            demand_title = type_name + str(demand_id)

            if item['status'] == 0:
                status = '刊登中'
            elif item['status'] == 1:
                status = '正在進行'
            elif item['status'] == 2:
                status = '已完成'
            
            demand_desc = '發佈時間：' + item['created_datetime'] + '\n狀態：' + status
            demand_url = item['match_info']['doc_url']

            col = CarouselColumn(
                title= demand_title,
                text= demand_desc,
                actions=[
                    PostbackTemplateAction(
                        label='顯示需求詳細資訊',
                        data='source=richmenu&flag=demand&info=helped_demand_content_' + str(demand_id)
                    ),
                    URITemplateAction(
                        label='互動留言版',
                        uri=demand_url
                    )
                ]
            )
            columns.append(col)

        carousel_template = TemplateSendMessage(
            alt_text='協助紀錄需求列表',
            template=CarouselTemplate(
                columns=columns
            )
        )
        demands_list.append(carousel_template)
    
    return demands_list

def match_success_result(demand_type, demand_id, doc_url): # 需求匹配成功
    template_list = []
    true = True
    bubble_json = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "需求配對成功",
                "size": "xl",
                "color": "#00A600",
                "weight": "regular"
            },
            {
                "type": "separator",
                "margin": "lg"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "需求類別："
                },
                {
                    "type": "text",
                    "text": demand_type,
                    "align": "end",
                    "wrap": true,
                    "maxLines": 0,
                    "adjustMode": "shrink-to-fit"
                }
                ],
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "需求編號："
                },
                {
                    "type": "text",
                    "text": demand_id,
                    "align": "end"
                }
                ],
                "margin": "lg"
            },
            {
                "type": "separator",
                "margin": "md"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "互動留言板",
                "uri": doc_url
                },
                "offsetTop": "md",
                "margin": "md",
                "adjustMode": "shrink-to-fit",
                "style": "secondary"
            }
            ]
        }
    }

    message = FlexSendMessage(alt_text='需求匹配成功',contents=bubble_json)
    text_template = TextSendMessage(text="您已獲得款項。\n請前往「個人資訊」->「協助紀錄」中查看。\n點選「互動留言板」就可以開始與對方對談囉！")
    template_list.append(message)
    template_list.append(text_template)

    return template_list

def match_fail_result(demand_type, demand_id): # 需求匹配失敗
    bubble_json = '''
    {{
        "type": "bubble",
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "需求配對失敗",
                "size": "xl",
                "color": "#CE0000",
                "weight": "regular"
            }},
            {{
                "type": "separator",
                "margin": "lg"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "需求類別："
                }},
                {{
                    "type": "text",
                    "text": "{demand_type}",
                    "align": "end"
                }}
                ],
                "margin": "xxl"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "需求編號："
                }},
                {{
                    "type": "text",
                    "text": "{demand_id}",
                    "align": "end"
                }}
                ],
                "margin": "lg"
            }},
            {{
                "type": "text",
                "align": "start",
                "margin": "md",
                "color": "#9D9D9D",
                "text": "  "
            }},
            {{
                "type": "separator",
                "margin": "md"
            }},
            {{
                "type": "text",
                "text": "請稍後再重新嘗試",
                "margin": "xl",
                "align": "center",
                "color": "#8E8E8E"
            }}
            ]
        }}
    }}
    '''.format(demand_type=demand_type, demand_id= demand_id)

    return bubble_json

def complete_message_to_Helper(demand):
    demand_id = str(demand['id'])
    if demand['type'] == 'intern_chat':
        demand_type = '實習經驗一對一對談 ' + demand_id
    elif demand['type'] == 'traffic_chat':
        demand_type = '交通資訊 ' + demand_id

    complete_message_to_Helper = '嗨！您協助的需求：\n' + demand_type + '\n，已被需求方確認完成囉！'
    text_template = TextSendMessage(text= complete_message_to_Helper)

    return text_template 

def help_message_to_publisher(demand):
    demand_id = str(demand['id'])
    if demand['type'] == 'intern_chat':
        demand_type = '實習經驗一對一對談 ' + demand_id
    elif demand['type'] == 'traffic_chat':
        demand_type = '交通資訊 ' + demand_id

    help_message_to_publisher = '嗨！您刊登的需求：\n' + demand_type + '\n，已被協助囉！' + '\n對方已獲得款項。' + '\n請前往「個人資訊」->「刊登紀錄」中查看。\n點選「互動留言板」就可以開始與對方對談囉！'
    text_template = TextSendMessage(text= help_message_to_publisher)

    return text_template

def personal_carousel(user_email, user_name, helped_time, published_time, amount):
    published_time = str(published_time) + ' 次'
    helped_time = str(helped_time) + ' 次'

    bubble_json = '''
    {{
        "type": "bubble",
        "header": {{
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#6b07e9",
        "offsetTop": "none",
        "offsetBottom": "none",
        "paddingTop": "xs"
        }},
        "body": {{
        "type": "box",
        "layout": "vertical",
        "contents": [
            {{
            "type": "text",
            "text": "個人資訊",
            "size": "xl",
            "weight": "bold"
            }},
            {{
            "type": "separator",
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "信箱",
                "color": "#999999",
                "align": "start",
                "gravity": "center",
                "position": "relative"
                }},
                {{
                "type": "text",
                "text": "{user_email}",
                "align": "center",
                "position": "absolute",
                "gravity": "bottom",
                "wrap": false,
                "adjustMode": "shrink-to-fit",
                "weight": "regular"
                }}
            ],
            "margin": "lg",
            "alignItems": "flex-end",
            "justifyContent": "flex-end"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "暱稱",
                "color": "#999999",
                "align": "start",
                "gravity": "center",
                "position": "relative"
                }},
                {{
                "type": "text",
                "text": "{user_name}",
                "align": "center",
                "position": "absolute",
                "gravity": "bottom",
                "wrap": false,
                "adjustMode": "shrink-to-fit",
                "weight": "regular"
                }}
            ],
            "margin": "lg",
            "alignItems": "flex-end",
            "justifyContent": "flex-end"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "刊登次數",
                "color": "#999999",
                "align": "start",
                "gravity": "center",
                "position": "relative"
                }},
                {{
                "type": "text",
                "text": "{published_time}",
                "align": "center",
                "position": "absolute",
                "gravity": "bottom",
                "wrap": false,
                "adjustMode": "shrink-to-fit",
                "weight": "regular"
                }}
            ],
            "margin": "lg",
            "alignItems": "flex-end",
            "justifyContent": "flex-end"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "協助次數",
                "color": "#999999",
                "align": "start",
                "gravity": "center",
                "position": "relative"
                }},
                {{
                "type": "text",
                "text": "{helped_time}",
                "align": "center",
                "position": "absolute",
                "gravity": "bottom",
                "wrap": false,
                "adjustMode": "shrink-to-fit",
                "weight": "regular"
                }}
            ],
            "margin": "lg",
            "alignItems": "flex-end",
            "justifyContent": "flex-end"
            }},
            {{
            "type": "separator",
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "text",
                "text": "Total",
                "align": "start",
                "gravity": "center",
                "color": "#999999",
                "size": "xl"
                }},
                {{
                "type": "text",
                "text": "{amount}",
                "align": "end",
                "gravity": "center",
                "size": "42px",
                "margin": "xxl",
                "wrap": true,
                "contents": []
                }},
                {{
                "type": "image",
                "url": "https://i.imgur.com/4o8Acos.png",
                "size": "xxs",
                "align": "center",
                "gravity": "center"
                }}
            ],
            "margin": "md"
            }},
            {{
            "type": "separator",
            "margin": "sm"
            }},
            {{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {{
                "type": "button",
                "action": {{
                    "type": "postback",
                    "label": "刊登紀錄",
                    "data": "source=richmenu&flag=point&info=published"
                }},
                "style": "secondary",
                "offsetEnd": "none",
                "gravity": "center",
                "margin": "none"
                }},
                {{
                "type": "button",
                "action": {{
                    "type": "postback",
                    "label": "協助紀錄",
                    "data": "source=richmenu&flag=point&info=helped"
                }},
                "style": "secondary",
                "margin": "md"
                }}
            ],
            "margin": "lg"
            }},
            {{
            "type": "box",
            "layout": "vertical",
            "contents": [
                {{
                "type": "button",
                "action": {{
                    "type": "postback",
                    "label": "我的成就徽章",
                    "data": "source=richmenu&flag=point&info=mybadge"
                }},
                "margin": "lg",
                "style": "secondary",
                "height": "md"
                }}
            ]
            }}
        ]
        }},
        "styles": {{
        "header": {{
            "backgroundColor": "#aaaaaa"
        }}
        }}
    }}
    '''.format(user_email= user_email, user_name= user_name, helped_time= helped_time
                            , published_time= published_time, amount= amount)

    return bubble_json

def latest_info():
    carousel_template = TemplateSendMessage(        
        alt_text = '最新資訊',
        template = CarouselTemplate(  
            columns = [
                # CarouselColumn(
                #     title = '校園情報員討論版',
                #     text = '點選下面連結前往校園情報員討論版吧！',
                #     thumbnail_image_url='https://i.imgur.com/cZrrldW.png',
                #     actions = [
                #         URITemplateAction(
                #             label='點我前往',
                #             uri='https://discord.gg/BrGAUeqAGj'
                #         )
                #     ]
                # ),
                CarouselColumn(
                    title = '每週挑戰',
                    text = '完成每週挑戰即可以獲得徽章！',
                    thumbnail_image_url='https://i.imgur.com/IMSXRm8.png',
                    actions = [
                        PostbackTemplateAction(
                            label='更多資訊',
                            data='source=richmenu&flag=point&info=weekly_challenge'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '什麼是時間銀行與清華幣？',
                    text = '點選更多資訊了解時間銀行與清華幣',
                    thumbnail_image_url='https://i.imgur.com/FADk14C.png',
                    actions = [
                        URITemplateAction(
                            label='什麼是時間銀行',
                            uri='https://telegra.ph/%E6%B8%85%E8%8F%AF%E5%B9%A3%E8%88%87%E6%99%82%E9%96%93%E9%8A%80%E8%A1%8C%E4%BB%8B%E7%B4%B9-06-10'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '問題回饋',
                    text = '有任何問題都可以在這邊告訴我們',
                    thumbnail_image_url='https://i.imgur.com/uy4EPc5.png',
                    actions = [
                        PostbackTemplateAction(
                            label='我要回饋',
                            data='source=richmenu&flag=point&info=comment'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template

def get_feedback():
    return TextSendMessage(text='請問您有什麼意見或問題呢？')

def tb_info():
    text_template = TextSendMessage(text=
    '''時間銀行的概念是指個體可以將用於解決他人問題的時間，轉換成另一種價值。

在這裡你可以獲得的價值－叫做「清華幣」，利用此貨幣能再驅動更多時間與價值的轉換，並將此力量永續地留在時間銀行中。

我們希望透過這個將「科技」與「社會創新」結合的媒合平台，解決學生的生活與學習困境，創造更美好的校園環境。'''
    )
    return text_template

def tb_info_welocome():
    text_template = TextSendMessage(text=
    '''時間銀行的概念是指個體可以將用於解決他人問題的時間，轉換成另一種價值。

在這裡你可以獲得的價值－叫做「清華幣」，利用此貨幣能再驅動更多時間與價值的轉換，並將此力量永續地留在時間銀行中。

我們希望透過這個將「科技」與「社會創新」結合的媒合平台，解決學生的生活與學習困境。

歡迎加入時間銀行，一同創造更美好的校園環境吧！'''
    )
    return text_template

def badges_menu():
    carousel_template = TemplateSendMessage(        
        alt_text = '最新資訊',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '成就徽章',
                    text = '根據你的付出會獲得不同的成就徽章唷！',
                    thumbnail_image_url='https://i.imgur.com/dOMH064.png',
                    actions = [
                        PostbackTemplateAction(
                            label='所有徽章',
                            data='source=richmenu&flag=point&info=allbadge'
                        ),
                        PostbackTemplateAction(
                            label='我的徽章',
                            data='source=richmenu&flag=point&info=mybadge'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template

def all_badges(all_badges, published_demands, helped_demands, helped_times, intern_times, traffic_times):
    contents = dict()
    contents['type'] = 'carousel'
    badges = []

    for i in all_badges:
        img_url = i['img_url']
        name = i['name']
        time = i['times']
        time_desc = ''
        progress = ''
        bgcolor = "#02C874"
        nameColor = "#000000"

        if i['type'] == 'weekly_publish2': # 第三週挑戰
            start_time_obj = datetime.strptime(i['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time_obj = datetime.strptime(i['end_time'], '%Y-%m-%d %H:%M:%S')
            created_time_obj = ''

            name = '【每週挑戰3】' + name   
            time_desc = i['start_time'][5:10] + ' ~ ' + i['end_time'][5:10] + ' 間協助 ' +  str(time) + ' 次'
            bgcolor = "#4545FF"

            if len(published_demands) == 0: # 從沒刊登過
                progress = '進度：' + '0' + ' / ' + str(time) + ' 次'
                bgcolor = "#a8a8a8"
                nameColor = "#a8a8a8"                
            else:
                for j in published_demands: # 判斷是否有在期間內刊登需求
                    created_time_obj = datetime.strptime(j['created_datetime'], '%Y-%m-%d %H:%M:%S')
                    if created_time_obj <= end_time_obj and created_time_obj >= start_time_obj:
                        progress = '進度：' + '1' + ' / ' + str(time) + ' 次'
                        bgcolor = "#4545FF"
                        nameColor = "#000000"
                        break
                    else:
                        progress = '進度：' + '0' + ' / ' + str(time) + ' 次'
                        bgcolor = "#a8a8a8"
                        nameColor = "#a8a8a8"

        elif i['type'] == 'weekly_help': # 第二週挑戰
            start_time_obj = datetime.strptime(i['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time_obj = datetime.strptime(i['end_time'], '%Y-%m-%d %H:%M:%S')
            created_time_obj = ''

            name = '【每週挑戰2】' + name   
            time_desc = i['start_time'][5:10] + ' ~ ' + i['end_time'][5:10] + ' 間協助 ' +  str(time) + ' 次'
            bgcolor = "#4545FF"

            if len(helped_demands) == 0: # 從沒協助過
                progress = '進度：' + '0' + ' / ' + str(time) + ' 次'
                bgcolor = "#a8a8a8"
                nameColor = "#a8a8a8"                
            else:
                for j in helped_demands: # 判斷是否有在時間前協助需求
                    created_time_obj = datetime.strptime(j['match_info']['created_datetime'], '%Y-%m-%d %H:%M:%S')
                    if created_time_obj <= end_time_obj and created_time_obj >= start_time_obj:
                        progress = '進度：' + '1' + ' / ' + str(time) + ' 次'
                        bgcolor = "#4545FF"
                        nameColor = "#000000"
                        break
                    else:
                        progress = '進度：' + '0' + ' / ' + str(time) + ' 次'
                        bgcolor = "#a8a8a8"
                        nameColor = "#a8a8a8"

        elif i['type'] == 'weekly_publish': # 第一週挑戰
            end_time_obj = datetime.strptime(i['end_time'], '%Y-%m-%d %H:%M:%S')
            created_time_obj = ''

            name = '【每週挑戰1】' + name
            time_desc = i['end_time'][0:10] + ' 前刊登 ' +  str(time) + ' 次需求'
            bgcolor = "#4545FF"
            
            if len(published_demands) == 0: # 從沒刊登過
                progress = '進度：' + '0' + ' / ' + str(time) + ' 次'
                bgcolor = "#a8a8a8"
                nameColor = "#a8a8a8"
            else:
                for j in published_demands: # 判斷是否有在時間前刊登需求
                    created_time_obj = datetime.strptime(j['created_datetime'], '%Y-%m-%d %H:%M:%S')
                    print(created_time_obj)
                    if created_time_obj <= end_time_obj:
                        progress = '進度：' + '1' + ' / ' + str(time) + ' 次'
                        break
                    else:
                        progress = '進度：' + '0' + ' / ' + str(time) + ' 次'
                        bgcolor = "#a8a8a8"
                        nameColor = "#a8a8a8"

        elif i['type'] == 'helping':
            time_desc = '資格：協助次數 ' +  str(time) + ' 次'
            if helped_times >= time:
                progress = '進度：' + str(time) + ' / ' + str(time) + ' 次'
            else:
                progress = '進度：' + str(helped_times) + ' / ' + str(time) + ' 次'
                bgcolor = "#a8a8a8"
                nameColor = "#a8a8a8"
        elif i['type'] == 'intern':
            time_desc = '資格：實習協助次數 ' +  str(time) + ' 次'
            if intern_times >= time:
                progress = '進度：' + str(time) + ' / ' + str(time) + ' 次'
            else:
                progress = '進度：' + str(intern_times) + ' / ' + str(time) + ' 次'
                bgcolor = "#a8a8a8"
                nameColor = "#a8a8a8"
        elif i['type'] == 'traffic':
            time_desc = '資格：交通協助次數 ' +  str(time) + ' 次'
            if traffic_times >= time:
                progress = '進度：' + str(time) + ' / ' + str(time) + ' 次'
            else:
                progress = '進度：' + str(traffic_times) + ' / ' + str(time) + ' 次'
                bgcolor = "#a8a8a8"
                nameColor = "#a8a8a8"
        
        badge_json = {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "paddingTop": "xs"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": img_url,
                    "size": "xl"
                },
                {
                    "type": "separator",
                    "margin": "xl"
                },
                {
                    "type": "text",
                    "text": name,
                    "margin": "lg",
                    "size": "lg",
                    "align": "center",
                    "weight": "bold",
                    "color": nameColor
                },
                {
                    "type": "text",
                    "text": time_desc,
                    "margin": "md",
                    "align": "center",
                    "color": "#9D9D9D"
                },
                {
                    "type": "text",
                    "text": progress,
                    "margin": "sm",
                    "color": "#9D9D9D",
                    "align": "center"
                }
                ]
            },
            "styles": {
                "header": {
                "backgroundColor": bgcolor
                }
            }
        }

        badges.append(badge_json)

    contents['contents'] = badges

    message = FlexSendMessage(alt_text='我的徽章',contents=contents)

    return message

def my_badges(personal_badges):
    contents = dict()
    contents['type'] = 'carousel'
    badges = []

    for i in personal_badges:
        img_url = i['img_url']
        name = i['name']
        time = i['times']
        bgcolor = "#02C874"
        time_desc = ''

        if i['type'] == 'weekly_publish': # 第一週挑戰
            name = '【每週挑戰1】' + name
            time_desc = i['end_time'][0:10] + ' 前刊登 1 次需求'
            bgcolor = "#4545FF"
        elif i['type'] == 'weekly_help': # 第二週挑戰
            name = '【每週挑戰2】' + name
            time_desc = i['start_time'][5:10] + ' ~ ' + i['end_time'][5:10] + ' 間協助 ' +  str(time) + ' 次'
            bgcolor = "#4545FF"
        elif i['type'] == 'weekly_publish2': # 第三週挑戰
            name = '【每週挑戰3】' + name
            time_desc = i['start_time'][5:10] + ' ~ ' + i['end_time'][5:10] + ' 間刊登 ' +  str(time) + ' 次'
            bgcolor = "#4545FF"
        elif i['type'] == 'helping':
            time_desc = '協助次數 ' +  str(time) + ' 次'
        elif i['type'] == 'intern':
            time_desc = '實習協助次數 ' +  str(time) + ' 次'
        elif i['type'] == 'traffic':
            time_desc = '交通協助次數 ' +  str(time) + ' 次'
        
        badge_json = {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "paddingTop": "xs"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": img_url,
                    "size": "xl"
                },
                {
                    "type": "separator",
                    "margin": "xl"
                },
                {
                    "type": "text",
                    "text": name,
                    "margin": "lg",
                    "size": "lg",
                    "align": "center",
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": time_desc,
                    "margin": "md",
                    "align": "center",
                    "color": "#9D9D9D"
                }
                ]
            },
            "styles": {
                "header": {
                "backgroundColor": bgcolor
                }
            }
        }

        badges.append(badge_json)

    contents['contents'] = badges

    message = FlexSendMessage(alt_text='我的徽章',contents=contents)

    return message

    # single_badge = '''
    # {
    #   "type": "bubble",
    #   "size": "kilo",
    #   "header": {
    #     "type": "box",
    #     "layout": "vertical",
    #     "contents": [],
    #     "paddingTop": "xs"
    #   },
    #   "body": {
    #     "type": "box",
    #     "layout": "vertical",
    #     "contents": [
    #       {
    #         "type": "image",
    #         "url": "https://i.imgur.com/YIfT47Z.png",
    #         "size": "xl"
    #       },
    #       {
    #         "type": "separator",
    #         "margin": "xl"
    #       },
    #       {
    #         "type": "text",
    #         "text": "好心人士",
    #         "margin": "lg",
    #         "size": "lg",
    #         "align": "center",
    #         "weight": "bold"
    #       },
    #       {
    #         "type": "text",
    #         "text": "協助次數 ( 1 / 1 )",
    #         "margin": "md",
    #         "align": "center",
    #         "color": "#9D9D9D"
    #       }
    #     ]
    #   },
    #   "styles": {
    #     "header": {
    #       "backgroundColor": "#02C874"
    #     }
    #   }
    # }
    # '''

def weekly_badge(all_badges):
    contents = dict()
    contents['type'] = 'carousel'
    badges = []

    for i in all_badges:
        img_url = i['img_url']
        bgcolor = "#4545FF"
        name = i['name']
        time_desc = ''

        if i['type'] == 'weekly_publish2': # 第三週挑戰
            name = '【每週挑戰3】' + name
            time_desc = i['start_time'][5:10] + ' ~ ' + i['end_time'][5:10] + ' 間刊登 1 次'
        
            badge_json = {
                "type": "bubble",
                "size": "kilo",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "paddingTop": "xs"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": img_url,
                        "size": "xl"
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "text",
                        "text": name,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": time_desc,
                        "margin": "md",
                        "align": "center",
                        "color": "#9D9D9D"
                    }
                    ]
                },
                "styles": {
                    "header": {
                    "backgroundColor": bgcolor
                    }
                }
            }

            badges.append(badge_json)

        elif i['type'] == 'weekly_help': # 第二週挑戰
            name = '【每週挑戰2】' + name
            time_desc = i['start_time'][5:10] + ' ~ ' + i['end_time'][5:10] + ' 間協助 1 次'
        
            badge_json = {
                "type": "bubble",
                "size": "kilo",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "paddingTop": "xs"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": img_url,
                        "size": "xl"
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "text",
                        "text": name,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": time_desc,
                        "margin": "md",
                        "align": "center",
                        "color": "#9D9D9D"
                    }
                    ]
                },
                "styles": {
                    "header": {
                    "backgroundColor": bgcolor
                    }
                }
            }

            badges.append(badge_json)

        elif i['type'] == 'weekly_publish': # 第一週挑戰
            name = '【每週挑戰1】' + name
            time_desc = i['end_time'][0:10] + ' 前刊登 1 次需求'

            badge_json = {
                "type": "bubble",
                "size": "kilo",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "paddingTop": "xs"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": img_url,
                        "size": "xl"
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "text",
                        "text": name,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": time_desc,
                        "margin": "md",
                        "align": "center",
                        "color": "#9D9D9D"
                    }
                    ]
                },
                "styles": {
                    "header": {
                    "backgroundColor": bgcolor
                    }
                }
            }

            badges.append(badge_json)

    contents['contents'] = badges

    message = FlexSendMessage(alt_text='每週挑戰',contents=contents)

    return message

def no_badges():
    text_template = TextSendMessage(text="您目前沒有任何成就徽章唷！")
    return text_template

def badges_template():
    bubble_json = '''
    {{
    "type": "carousel",
    "contents": [
        {{
        "type": "bubble",
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "image",
                "url": "https://i.imgur.com/auiYHIw.png",
                "size": "lg",
                "offsetTop": "md"
            }},
            {{
                "type": "separator",
                "margin": "32px"
            }},
            {{
                "type": "text",
                "text": "實習達人",
                "margin": "xl",
                "align": "center",
                "weight": "regular",
                "size": "lg"
            }}
            ]
        }}
        }},
        {{
        "type": "bubble",
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "image",
                "url": "https://i.imgur.com/0uWHohU.png",
                "size": "xl"
            }},
            {{
                "type": "separator",
                "margin": "lg"
            }},
            {{
                "type": "text",
                "text": "安全嚮導",
                "margin": "xl",
                "align": "center",
                "size": "lg"
            }}
            ]
        }}
        }}
    ]
    }}
    '''.format()

    return bubble_json