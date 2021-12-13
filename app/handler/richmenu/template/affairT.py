from linebot.models import *

def affair_info_carousel():
    carousel_template = TemplateSendMessage(        
        alt_text = '讓狗狗情報員來告訴你校園防疫資訊！',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '2021清華新生領航營',
                    text = '點擊下方按鈕，即可註冊與進入2021清華新生領航營專區！',
                    actions = [
                        MessageTemplateAction(
                            label='進入2021清華新生領航營',
                            text='[選單]2021清華新生領航營'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '校園電話查詢',
                    text = '點擊「查詢電話」輸入校園單位，本汪可以直接告訴你喔！',
                    actions = [
                        PostbackTemplateAction(
                            label='查詢電話',
                            data='source=richmenu&flag=affair&info=phone'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '校園活動資訊',
                    text = '點擊「更多資訊」，本汪可以直接告訴你喔！',
                    actions = [
                        PostbackTemplateAction(
                            label='更多資訊',
                            data='source=richmenu&flag=affair&info=recnews'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '校務Q&A',
                    text = '點擊「我要提問」輸入想問的校務問題，本汪可以直接告訴你喔！',
                    actions = [
                        PostbackTemplateAction(
                            label='我要提問',
                            data='source=richmenu&flag=affair&info=qa'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '109學年度第1學期行事曆',
                    text = '點擊「點我進入」開啟行事曆',
                    actions = [
                        URIAction(
                            label = '點我進入',
                            uri = 'https://reurl.cc/7yV3gD'

                        )
                    ]
                ),
                CarouselColumn(
                    title = '簡易選課系統',
                    text = '點擊「點我進入」進入簡易選課系統',
                    actions = [
                        URIAction(
                            label = '點我進入',
                            uri = 'https://nthu-courses.github.io/#/'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template

def recNew_type():

    buttons_template = TemplateSendMessage(
        alt_text='查詢活動類型',
        template=ButtonsTemplate(
            title='查詢活動類型',
            text='請選擇你想查詢的活動類型',
            actions=[
                PostbackTemplateAction(
                    label='演講訊息',
                    text='演講訊息',
                    data='source=richmenu&flag=affair&info=speech'
                ),
                PostbackTemplateAction(
                    label='藝術展覽',
                    text='藝術展覽',
                    data='source=richmenu&flag=affair&info=exhibition'
                ),
                PostbackTemplateAction(
                    label='各類活動',
                    text='各類活動',
                    data='source=richmenu&flag=affair&info=activity'
                )
            ]
        )
    )
    return buttons_template

def qa_info():
    '''校務Q&A'''
    QuickReply_text_message = TextSendMessage(
        text = '請問想詢問什麼校務資訊呢？',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    action = MessageAction(label = "查詢場地使用狀況/我想借場地", text = "查詢場地使用狀況/我想借場地"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "怎麼申請交換", text = "怎麼申請交換"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "運動場地如何申請/租借/借用", text = "運動場地如何申請/租借/借用"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "怎麼申請獎學金", text = "怎麼申請獎學金"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "學分學程資訊查詢", text = "學分學程資訊查詢"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "校際選課的規定有哪些", text = "校際選課的規定有哪些"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "宿舍使用的規定", text = "宿舍使用的規定"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "怎麼申請海外姊妹校交換？", text = "怎麼申請海外姊妹校交換？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "如何申請雙主修？", text = "如何申請雙主修？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "如何申請輔系？", text = "如何申請輔系？"),
                )
            ]
        )
    )
    return QuickReply_text_message