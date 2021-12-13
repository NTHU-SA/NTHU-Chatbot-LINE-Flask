from linebot.models import *
import json

from utils import busUtil

def main_campus_bus_img(): #校本部公車
    template_list = []

    img_1_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/wG0w8QR.jpg', 
        preview_image_url='https://i.imgur.com/wG0w8QR.jpg'
    )
    # img_2_template = ImageSendMessage(
    #     original_content_url='https://i.imgur.com/ACiFM4x.png', 
    #     preview_image_url='https://i.imgur.com/ACiFM4x.png'
    # )
    template_list.append(img_1_template)
    # template_list.append(img_2_template)

    return template_list

def minor_campus_bus_img(): #南大專車
    template_list = []

    img_1_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/5EGMffM.jpg', 
        preview_image_url='https://i.imgur.com/5EGMffM.jpg'
    )
    # img_2_template = ImageSendMessage(
    #     original_content_url='https://i.imgur.com/2JTOjMK.png', 
    #     preview_image_url='https://i.imgur.com/2JTOjMK.png'
    # )

    template_list.append(img_1_template)
    # template_list.append(img_2_template)

    return template_list

def et_bus_img(): #83路線公車
    template_list = []

    text_template = TextSendMessage(text="清華大學校內各站(含清大北校門、第二綜合大樓、生科館/人社院、台積館)不開放校外人下車，乘客如持清大證件可以下車。")

    img_1_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/hARN9Y5.png', 
        preview_image_url='https://i.imgur.com/hARN9Y5.png'
    )

    template_list.append(text_template)
    template_list.append(img_1_template)

    return template_list

def bus_route_template(): #公車路線清單
    template_list = []
    bus_route_template = TemplateSendMessage(
        alt_text='公車路線清單',
        template=ButtonsTemplate(
            title='公車路線',
            text='請選擇你要查詢的公車路線',
            actions=[
                URITemplateAction(
                    label='公車資訊公告',
                    uri='http://affairs.site.nthu.edu.tw/p/406-1165-206830,r1065.php?Lang=zh-tw'
                ),
                PostbackTemplateAction(
                    label='校本部公車',
                    data='source=richmenu&flag=bus&info=main_campus'
                ),
                PostbackTemplateAction(
                    label='南大專車',
                    data='source=richmenu&flag=bus&info=minor_campus'
                ),
                PostbackTemplateAction(
                    label='83路線公車',
                    data='source=richmenu&flag=bus&info=83_bus'
                )
                # # TODO: 動態校車
                # PostbackTemplateAction(
                #     label='校本部校車動態查詢',
                #     data='source=richmenu&flag=bus&info=dyn_search'
                # )
            ]
        )
    )
    template_list.append(bus_route_template)
    return template_list

# 動態公車: 上車地點
def dynbus_geton_loc_template():
    dynbus_geton_loc_template = TemplateSendMessage(
        alt_text='動態上車選單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='您要在哪站上車呢？',
                    text='請選擇您要上車的站名',
                    actions=[
                        PostbackTemplateAction(
                            label='北校門口',
                            text='北校門口',
                            data='source=richmenu&flag=dynbus_geton&info=north_main_gate'
                        ),
                        PostbackTemplateAction(
                            label='綜二館',
                            text='綜二館',
                            data='source=richmenu&flag=dynbus_geton&info=general_building'
                        ),
                        PostbackTemplateAction(
                            label='楓林小徑',
                            text='楓林小徑',
                            data='source=richmenu&flag=dynbus_geton&info=maple_path'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='您要在哪站上車呢？',
                    text='請選擇您要上車的站名',
                    actions=[
                        PostbackTemplateAction(
                            label='奕園停車場',
                            text='奕園停車場',
                            data='source=richmenu&flag=dynbus_geton&info=yi_pavilion_parking_lot'
                        ),
                        PostbackTemplateAction(
                            label='南門停車場',
                            text='南門停車場',
                            data='source=richmenu&flag=dynbus_geton&info=south_gate_parking_lot'
                        ),
                        PostbackTemplateAction(
                            label='人社院',
                            text='人社院',
                            data='source=richmenu&flag=dynbus_geton&info=college_of_human_building'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='您要在哪站上車呢？',
                    text='請選擇您要上車的站名',
                    actions=[
                        PostbackTemplateAction(
                            label='台積館',
                            text='台積館',
                            data='source=richmenu&flag=dynbus_geton&info=tsmc_building'
                        ),
                        PostbackTemplateAction(
                            label=' ',
                            text=' ',
                            data='source=richmenu&flag=none&info=none'
                        ),
                        PostbackTemplateAction(
                            label=' ',
                            text=' ',
                            data='source=richmenu&flag=none&info=none'
                        ),
                    ]
                )
            ]
        )
    )


    # dynbus_geton_loc_template = TemplateSendMessage(
    #     alt_text='請輸入你的上車站名',
    #     template=ButtonsTemplate(
    #         title='公車路線',
    #         text='請輸入你的上車站名',
    #         actions=[
    #             PostbackTemplateAction(
    #                 label='北校門口',
    #                 data='source=richmenu&flag=dynbus&info=north_main_gate'
    #             ),
    #             PostbackTemplateAction(
    #                 label='綜二館',
    #                 data='source=richmenu&flag=dynbus&info=general_building'
    #             ),
    #             PostbackTemplateAction(
    #                 label='楓林小徑',
    #                 data='source=richmenu&flag=dynbus&info=maple_path'
    #             ),
    #             PostbackTemplateAction(
    #                 label='奕園停車場',
    #                 data='source=richmenu&flag=dynbus&info=yi_pavilion_parking_lot'
    #             ),
    #             PostbackTemplateAction(
    #                 label='南門停車場',
    #                 data='source=richmenu&flag=dynbus&info=south_gate_parking_lot'
    #             ),
    #             PostbackTemplateAction(
    #                 label='人社院',
    #                 data='source=richmenu&flag=dynbus&info=college_of_human_building'
    #             ),
    #             PostbackTemplateAction(
    #                 label='台積館',
    #                 data='source=richmenu&flag=dynbus&info=tsmc_building'
    #             )
    #         ]
    #     )
    # )
    return dynbus_geton_loc_template

# 動態公車: 下車地點
def dynbus_getoff_loc_template(geton_loc):
    getoff_list = busUtil.geton_map_getoff(geton_loc)

    actions_template = []
    for item in getoff_list:
        info = geton_loc + '~' + busUtil.BUS_LOC_MAP_CH[item]

        template = PostbackTemplateAction(
            label=item,
            text=item,
            data='source=richmenu&flag=dynbus_getoff&info='+info
        )
        actions_template.append(template)

    carousel_columns = []
    carousel_actions = []
    for idx, item in enumerate(actions_template):
        carousel_actions.append(item)

        if len(carousel_actions) == 3:
            carousel_col = CarouselColumn(
                title='您要在哪站下車呢？',
                text='請選擇您要下車的站名',
                actions=carousel_actions
            )
            carousel_columns.append(carousel_col)
            carousel_actions = []
            
    
    dynbus_getoff_loc_template = TemplateSendMessage(
        alt_text='請輸入你的下車站名',
        template=CarouselTemplate(
            columns=carousel_columns
        )
    )
    return dynbus_getoff_loc_template

# 動態公車: flex content
def dync_result_flex_json_content(geton, getoff, line, arriveTime, waitTime):
    # line色碼
    bgColor = ''
    if line == 'red':
        bgColor = '#EF5350'
    elif line == 'green':
        bgColor = '#7CB342'

    bubble_json = '''
    {{
        "type": "bubble",
        "size": "mega",
        "header": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "box",
                "layout": "vertical",
                "contents": [
                {{
                    "type": "text",
                    "text": "FROM",
                    "color": "#ffffff66",
                    "size": "sm"
                }},
                {{
                    "type": "text",
                    "text": "{geton}",
                    "color": "#ffffff",
                    "size": "xl",
                    "flex": 4,
                    "weight": "bold"
                }}
                ]
            }},
            {{
                "type": "box",
                "layout": "vertical",
                "contents": [
                {{
                    "type": "text",
                    "text": "TO",
                    "color": "#ffffff66",
                    "size": "sm"
                }},
                {{
                    "type": "text",
                    "text": "{getoff}",
                    "color": "#ffffff",
                    "size": "xl",
                    "flex": 4,
                    "weight": "bold"
                }}
                ]
            }}
            ],
            "paddingAll": "20px",
            "backgroundColor": "{bgColor}",
            "spacing": "md",
            "height": "154px",
            "paddingTop": "22px"
        }},
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "發車時間：{arriveTime}",
                "color": "#757575",
                "size": "md"
            }},
            {{
                "type": "text",
                "text": "等待時間：{waitTime}",
                "color": "#757575",
                "size": "md",
                "offsetTop": "3px"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "text",
                    "text": "{arriveTime}",
                    "size": "sm",
                    "gravity": "center",
                    "wrap": false,
                    "flex": 2,
                    "align": "start"
                }},
                {{
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {{
                        "type": "filler"
                    }},
                    {{
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {{
                            "type": "filler"
                        }}
                        ],
                        "cornerRadius": "30px",
                        "height": "12px",
                        "width": "12px",
                        "borderColor": "#EF454D",
                        "borderWidth": "2px"
                    }},
                    {{
                        "type": "filler"
                    }}
                    ],
                    "flex": 0
                }},
                {{
                    "type": "text",
                    "text": "{geton}",
                    "gravity": "center",
                    "flex": 4,
                    "size": "sm"
                }}
                ],
                "spacing": "lg",
                "cornerRadius": "30px",
                "margin": "xxl"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {{
                        "type": "filler"
                    }}
                    ],
                    "flex": 2
                }},
                {{
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {{
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {{
                            "type": "filler"
                        }},
                        {{
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {{
                                "type": "filler"
                            }}
                            ],
                            "width": "2px",
                            "backgroundColor": "#B7B7B7"
                        }},
                        {{
                            "type": "filler"
                        }}
                        ],
                        "flex": 1
                    }}
                    ],
                    "width": "12px"
                }},
                {{
                    "type": "text",
                    "text": " ",
                    "gravity": "center",
                    "flex": 4,
                    "size": "xs",
                    "color": "#8c8c8c"
                }}
                ],
                "spacing": "lg",
                "height": "64px"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {{
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {{
                        "type": "text",
                        "text": " ",
                        "gravity": "center",
                        "size": "sm"
                    }}
                    ],
                    "flex": 2
                }},
                {{
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {{
                        "type": "filler"
                    }},
                    {{
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {{
                            "type": "filler"
                        }}
                        ],
                        "cornerRadius": "30px",
                        "width": "12px",
                        "height": "12px",
                        "borderWidth": "2px",
                        "borderColor": "#6486E3"
                    }},
                    {{
                        "type": "filler"
                    }}
                    ],
                    "flex": 0
                }},
                {{
                    "type": "text",
                    "text": "{getoff}",
                    "gravity": "center",
                    "flex": 4,
                    "size": "sm"
                }}
                ],
                "spacing": "lg",
                "cornerRadius": "30px"
            }}
            ]
        }}
        }}
    '''.format(bgColor=bgColor, geton=geton, getoff=getoff, arriveTime=arriveTime, waitTime=waitTime)

    return bubble_json


# 動態公車: flex template
def dync_result_flex_carousel_template(flex_contents):
    # print(flex_contents)

    carousel_json = ''

    if len(flex_contents) == 1:
        carousel_json = '''
            {{
                "type": "carousel",
                "contents": [{content}]
            }}
        '''.format(content=flex_contents[0])
    elif len(flex_contents) == 2:
        carousel_json = '''
            {{
                "type": "carousel",
                "contents": [{content1}, {content2}]
            }}
        '''.format(content1=flex_contents[0], content2=str(flex_contents[1]))

    flex_message_template = FlexSendMessage(alt_text="動態公車查詢", contents=json.loads(carousel_json))
    return flex_message_template