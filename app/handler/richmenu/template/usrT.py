from linebot.models import *

def usr_carousel():
    template_list = []

    intro_button_template = TemplateSendMessage(
        alt_text='讓狗狗情報員來介紹清華大學USR計畫！',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/iR1tpkS.png',
            title='清大usr計畫-熟齡健康生活創新研究與實踐',
            text='以服務主導邏輯與運動科學概念，透過使用者需求探索與洞察，串連產學與民間單位，達到價值交換，建置創新熟齡健康服務系統',
            actions=[
                URITemplateAction(
                    label='FB粉絲專頁',
                    uri='https://reurl.cc/Ezabdk'
                ),
                URITemplateAction(
                    label='清華大學USR網站',
                    uri='https://usractiveageinglife.wixsite.com/nthu?fbclid=IwAR3cR2XyuLmSulX0AH86G-wYQamazqRoLNA99VG5FsTw0bN5msxaN39cO9c'
                )
            ]
        )
    )

    carousel_template = TemplateSendMessage(        
        alt_text = '讓狗狗情報員來告訴你清華大學USR計畫的活動資訊！',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/Ze2522r.png',
                    title = '世界咖啡館：未來全齡健康',
                    text = '時間：2020.11.08 (一) 14:30-17:30\n地點：清大教育館114',
                    actions = [
                        URIAction(
                            label = '報名表單',
                            uri = 'https://forms.gle/qLQiSE6EzJCAwQDX8'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/u9xtASR.png',
                    title = '活力健走迷你馬拉松',
                    text = '時間：2020.11.22 (日) 08:00-11:00\n地點：清大南大校區操場',
                    actions = [
                        URIAction(
                            label = '報名表單',
                            uri = 'https://forms.gle/hGQ53B1aGib7kyd16'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/69T75yw.jpg',
                    title = '設計工作坊：有溫度的無齡健康未來提案',
                    text = '時間：2020.12.05 (六) ~ 12.06 (日) 10:00-17:00\n地點：清大教育館114',
                    actions = [
                        MessageTemplateAction(
                            label='敬請期待',
                            text='報名表單於活動前兩週公布'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/69T75yw.jpg',
                    title = 'Ballroom Dance-Latin Party',
                    text = '時間：2020.01.11 (一) 19:00-20:30\n地點：(暫定) 實齋講堂',
                    actions = [
                        MessageTemplateAction(
                            label='敬請期待',
                            text='報名表單於活動前兩週公布'
                        ),
                    ]
                ),
            ]
        )
    )

    template_list.append(intro_button_template)

    return template_list