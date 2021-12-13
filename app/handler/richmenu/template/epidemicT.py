from linebot.models import *

def epidemic_feedback():
    return TextSendMessage(text='你對疫情還有什麼提問，是我們沒有捕捉到的呢？告訴本汪，盡快為你處理！')

def epidemic_info_carousel():
    carousel_template = TemplateSendMessage(        
        alt_text = '讓狗狗情報員來告訴你校園防疫資訊！',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '新冠病毒防疫專區',
                    text = '學校發布之最新公告以及防疫措施都可以在這裡找到',
                    actions = [
                        URIAction(
                            label = '點我進入',
                            uri = 'https://2019-ncov.site.nthu.edu.tw/?Lang=zh-tw'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '全體學生相關懶人包',
                    text = '疫情與學生相關的資訊。如開學、校園場所、校園消毒、口罩供應等',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=epidemic&info=students'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '住宿生注意事項',
                    text = '身為住宿生的你，趕緊來關注一下關於宿舍的防疫資訊',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=epidemic&info=boarders'
                        )
                    ]
                ),
                # CarouselColumn(
                #     title = '自陸港澳返台學生注意事項',
                #     text = '若同學剛從陸港澳地區返台，請必須查看此資訊',
                #     actions = [
                #        PostbackTemplateAction(
                #             label='取得資訊',
                #             data='source=richmenu&flag=epidemic&info=backtw'
                #         )
                #     ]
                # ),
                CarouselColumn(
                    title = '什麼樣的人必須居家隔離？',
                    text = '本汪告訴你，哪些人必須或是需要自主在家隔離',
                    actions = [
                       PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=epidemic&info=isolation'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '非本國生注意事項',
                    text = '防疫期間，非本國生相關注意事項及資訊都可以在這裡找到',
                    actions = [
                       PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=epidemic&info=foreign'
                        )
                    ]
                ),
                # CarouselColumn(
                #     title = '陸生注意事項',
                #     text = '防疫期間，陸生相關注意事項及資訊都可以在這裡找到',
                #     actions = [
                #        PostbackTemplateAction(
                #             label='取得資訊',
                #             data='source=richmenu&flag=epidemic&info=chinastudent'
                #         )
                #     ]
                # ),
                # CarouselColumn(
                #     title = '港澳生注意事項',
                #     text = '防疫期間，港澳生相關注意事項及資訊都可以在這裡找到',
                #     actions = [
                #        PostbackTemplateAction(
                #             label='取得資訊',
                #             data='source=richmenu&flag=epidemic&info=tkm'
                #         )
                #     ]
                # ),
                CarouselColumn(
                    title = '陸港澳交換計畫相關',
                    text = '若有陸港澳交換計畫的同學，趕緊來看',
                    actions = [
                       PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=epidemic&info=change2tkm'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '相關資訊發布與聯絡管道',
                    text = '類似症狀通報、校方疫情公告、學生會等資訊',
                    actions = [
                       PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=epidemic&info=contact'
                        )
                    ]
                ),
                # CarouselColumn(
                #     title = '疫情相關提問',
                #     text = '若沒有找到你想要的資訊，本汪會立即轉達校方！',
                #     actions = [
                #        MessageTemplateAction(
                #             label='疫情相關提問',
                #             text='!疫情相關提問'
                #         )
                #     ]
                # ),
            ]
        )
    )

    return carousel_template

def qa_info():
    '''防疫Q&A'''
    QuickReply_text_message = TextSendMessage(
        text = '請問想詢問什麼防疫資訊呢？',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    action = MessageAction(label = "本校行事曆有哪些更動？", text = "本校行事曆有哪些更動？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "學生社團活動可不可以舉辦？", text = "學生社團活動可不可以舉辦？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "在防疫期間，住宿區域的清潔衛生原則為何？", text = "在防疫期間，住宿區域的清潔衛生原則為何？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "宿舍區的集中檢疫區域範圍為何？", text = "宿舍區的集中檢疫區域範圍為何？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "集中檢疫區域的設施有哪些？", text = "集中檢疫區域的設施有哪些？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "校慶是否取消？", text = "校慶是否取消？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "梅竹賽是否照常舉行？", text = "梅竹賽是否照常舉行？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "集中檢疫管理區域管理方式為何？", text = "集中檢疫管理區域管理方式為何？"),
                ),
                QuickReplyButton(
                    action = MessageAction(label = "集中檢疫管理區域的封閉程度如何？", text = "集中檢疫管理區域的封閉程度如何？"),
                )
            ]
        )
    )
    return QuickReply_text_message


def students_info():
    '''全體學生相關懶人包
        Return: 
            - template_list (list): 包含圖片、文字訊息的模板 
    '''
    template_list = []

    image_carousel_template = TemplateSendMessage(        
        alt_text = '新型冠狀病毒相關公告: 全體學生相關懶人包資訊',
        template = ImageCarouselTemplate(  
            columns = [
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/S10id0U.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/4I6s7rx.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/Ewk8KZF.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/V1yqlsF.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/arayCid.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/YOc1tBK.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/uRHHq7M.png',
                    action=PostbackTemplateAction(
                        label='@nthuchatbot',
                        data='source=none&flag=none&info=none'
                    )
                )
            ]
        )
    )

    text_template = TextSendMessage(text='''🐾最後更新時間：109.03.27，接到新情報本汪會再告訴大家呦✨''')

    template_list.append(image_carousel_template)
    template_list.append(text_template)
    return template_list


def boarders_info():
    '''住宿生注意事項
        Return: 
            - template_list (list): 包含文字訊息的模板 
    '''
    template_list = []

    text_1_template = TextSendMessage(text='''🐶防疫期間規定
1.開學前有發燒或身體不適，暫不要返校住宿，要返校住宿先告知宿舍管理中心。
2.近期出入國境的台生及境外生，抵台14天內每日量測體溫（各宿舍管理中心可借體溫計）。
3.有發燒或身體不適通知宿舍管理中心
4.有發燒症狀至衛保組網站 http://0rz.tw/Dh91e 填表，以利疫情管理。
    ''')

    text_2_template = TextSendMessage(text='''🐶清潔消毒相關
 1.清潔人員每日上下班自主量體溫，有發燒則主動換人
 2.每日至少兩次對人體會接觸之區域進行消毒（如電梯按鍵、門把、交誼廳等）
3.每日至少清潔兩次廁所，並改用洗衣粉加稀釋過漂白水。
    ''')

    text_3_template = TextSendMessage(text='''🐶因應新型冠狀病毒肺炎疫情的急遽升溫，住宿組為因應健康管理、檢疫等緊急需求而規劃的應變空間範圍如下（共70房、120床）：
● 清齋10樓清華會館：37房、59床（男/女）
● 清齋1樓A/B棟：21房、37床（男）
● 學齋1樓A/C棟：12房、24床（女）
    ''')

    text_4_template = TextSendMessage(text='''🐾此資訊最後更新時間是3/26，接到新情報本汪會再告訴大家呦✨''')

    template_list.append(text_1_template)
    template_list.append(text_2_template)
    template_list.append(text_3_template)
    template_list.append(text_4_template)
    return template_list


def backtw_info():
    '''自陸港澳返台學生注意事項
        Return: 
            - template_list (list): 包含文字訊息的模板 
    '''
    template_list = []

    text_1_template = TextSendMessage(text='''🐶14天內，依政府規定在家休息停止上課，請假不扣分，將以補考或其他補救措施處理成績，補考成績按實際成績計算。
🐶14天內，不論有無症狀皆需每日早晚量測及通報體溫至http://0rz.tw/kZFPt 。
🐶若有發燒或呼吸道不適等類流症狀，通報衛保組03-5743000(上班時間)或生輔組03-5711814(24小時)，協助連絡1922轉送醫院治療。
    ''')

    text_2_template = TextSendMessage(text='''🐾此資訊最後更新時間是2/2，會視情況調整，接到新情報本汪會馬上告訴大家呦✨''')

    template_list.append(text_1_template)
    template_list.append(text_2_template)
    return template_list


def isolation_info():
    '''什麼樣的人必須居家隔離？
        Return: 
            - template_list (list): 包含文字訊息的模板 
    '''
    template_list = []

    text_1_template = TextSendMessage(text='''🐶確診病例接觸者之學生及教職員工
🐶學校確診病例之一起上課同學老師、共同參加社團或其他活動者
🐶自主隔離期間規定：14天內留在家中（或住宿地點）不可外出上班、上學、及出國。
    ''')

    text_2_template = TextSendMessage(text='''🐾此資訊最後更新時間是3/26，接到新情報本汪會再告訴大家呦✨''')

    template_list.append(text_1_template)
    template_list.append(text_2_template)
    return template_list

def foreign_info():
    '''非本國生注意事項
        Return: 
            - template_list (list): 包含文字訊息的模板 
    '''
    template_list = []

    text_1_template = TextSendMessage(text='''⚠️3/19日起，非本國籍人員一律限制入境⚠️
🐶受教權益維護措施，請見校方安心就學措施！
    ''')

    text_2_template = TextSendMessage(text='''🐾此資訊最後更新時間是3/26，接到新情報本汪會再告訴大家呦✨''')

    template_list.append(text_1_template)
    template_list.append(text_2_template)
    return template_list


# def chinastudent_info():
#     '''陸生注意事項
#         Return: 
#             - template_list (list): 包含文字訊息的模板 
#     '''
#     template_list = []

#     text_1_template = TextSendMessage(text='''🐶即日起至2/9暫緩來台，2/9後是否繼續禁止來台待教育部決議。
# 🐶1/26前返台陸生，未到過武漢地區者：
#  1.不論有無症狀皆需至 http://0rz.tw/kZFPt 填報。
#  2.未到過武漢地區者：戴口罩、進行早晚體溫監控、避免出入公共場所。
# 🐶1/26前返台陸生，到過武漢地區者：配合政府政策進行集中檢疫管理。
# 🐶如未確實遵守規定，可依法處新臺幣 6 萬至 30 萬元不等罰鍰。
# 🐶因應14天隔離政策，且為降低受影響需更換宿舍的住宿生，2/9日後抵台陸生將分3梯次抵台，每梯2週共6週。
# 🐶來臺時須詳實填寫「旅客入境健康聲明卡」
# 🐶開學註册最多可延6週，超過建議辦休學，休學不計入學則規定休學期限。
#     ''')

#     text_2_template = TextSendMessage(text='''🐾已返台陸生請注意🐾
# 🐶1/26前返台陸生，未到過武漢地區者：
#  1.不論有無症狀皆需至 http://0rz.tw/kZFPt 填報。
#  2.戴口罩、進行早晚體溫監控、避免出入公共場所。
# 1/26前返台陸生，到過武漢地區者：須配合政府政策進行集中檢疫管理。
# 🐶如未確實遵守規定，可依法處新臺幣 6 萬至 30 萬元不等罰鍰。
#     ''')

#     text_3_template = TextSendMessage(text='''🐾此資訊最後更新時間是3/5，接到新情報本汪會再告訴大家呦✨''')

#     template_list.append(text_1_template)
#     template_list.append(text_2_template)
#     template_list.append(text_3_template)
#     return template_list


# def tkm_info():
#     '''港澳生注意事項
#         Return: 
#             - template_list (list): 包含文字訊息的模板 
#     '''
#     template_list = []

#     text_1_template = TextSendMessage(text='''【2/11起禁止港澳地區民眾、包括港澳學生入境】
# 🐶尚未返台港澳生請注意
# 🐶港澳生返校的具體時程仍待政府政策決定
# 開學註册最多可延6週，超過建議辦休學，休學不計入學則規定休學期限。
#     ''')

#     text_2_template = TextSendMessage(text='''🐶已返台港澳生請注意
# 港澳生若於2/7至2/10間入境及2/10起經中港澳轉機之僑外生，均須進行居家檢疫14天。
# 港澳生居家檢疫措施相關規定：https://reurl.cc/ex58ob
# 🐶如未確實遵守規定，可依法處新臺幣 6 萬至 30 萬元不等罰鍰。
# 🐶14天內，依政府規定在家休息停止上課，請假不扣分，將以補考或其他補救措施處理成績，補考成績按實際成績計算。
# 🐶14天內，不論有無症狀皆需每日早晚量測及通報體溫至http://0rz.tw/kZFPt 。
# 🐶若有發燒或呼吸道不適等類流症狀，通報衛保組03-5743000(上班時間)或生輔組03-5711814(24小時)，協助連絡1922轉送醫院治療。
#     ''')

#     text_3_template = TextSendMessage(text='''🐾此資訊最後更新時間是3/5，接到新情報本汪會再告訴大家呦✨''')

#     template_list.append(text_1_template)
#     template_list.append(text_2_template)
#     template_list.append(text_3_template)
#     return template_list


def change2tkm_info():
    '''陸港澳交換計畫相關
        Return: 
            - template_list (list): 包含文字訊息的模板 
    '''
    template_list = []

    text_1_template = TextSendMessage(text='''🐶2020春季陸生至我校交流：計畫暫停，已申請的陸籍同學可延至2020秋季班再來清華交流。
🐶2020年春季至大陸地區交流的我校學生：強力建議暫時不要前往，強力建議不要前往，大多數同學已暫緩交換。
    ''')

    text_2_template = TextSendMessage(text='''🐾此資訊最後更新時間是3/26，會視情況調整，接到新情報本汪會馬上告訴大家呦✨''')

    template_list.append(text_1_template)
    template_list.append(text_2_template)
    return template_list


def contact_info():
    '''相關資訊發布與聯絡管道
        Return: 
            - template_list (list): 包含文字訊息的模板 
    '''
    template_list = []

    text_1_template = TextSendMessage(text='''🐶類似症狀通報：衛保組 03-5743000 (上班時間) 或 生輔組 03-5711814 (24 小時)
🐶清華大學安心就學措施：http://2019-ncov.site.nthu.edu.tw/var/file/499/1499/img/420369121.pdf
🐶校方疫情公告專區：http://2019-ncov.site.nthu.edu.tw/
🐶學生會粉專公告：https://www.facebook.com/nthusa/
    ''')

    template_list.append(text_1_template)
    return template_list


# NOTE: 全體學生相關懶人包(students)專用, render成為image carousel模板
def students_carousel_render(content):
    image_carousel_column_list = []
    
    for img_url in content:
        col = ImageCarouselColumn(
                image_url=img_url,
                action=PostbackTemplateAction(
                    label='@nthuchatbot',
                    data='source=none&flag=none&info=none'
                )
            )
        image_carousel_column_list.append(col)

    image_carousel_template = TemplateSendMessage(        
        alt_text = '新型冠狀病毒相關公告: 全體學生相關懶人包資訊',
        template = ImageCarouselTemplate(  
            columns = image_carousel_column_list
        )
    )

    return image_carousel_template


# NOTE: 取得epid content(list), render成為文字模板
def epid_content_render(content):
    '''將防疫資訊渲染成line文字模板
        Params:
            - content (list): 文字訊息
        Return: 
            - template_list (list): 包含文字訊息的模板
    '''

    template_list = []

    for ctx in content:
        template_list.append(TextSendMessage(text=ctx))

    return template_list