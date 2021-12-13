from linebot.models import *

def timeplace():
    template_list = []
    text_template_1 = TextSendMessage(text="8/15(六) 09:30 前於清華教育館3F報到")
    place_template_1 = LocationSendMessage(title='清華教育館', address='清華教育館', latitude=24.795727, longitude=120.993952)
    text_template_2 = TextSendMessage(text="8/16(日) 09:30 前於清大計算機中心集合")
    place_template_2 = LocationSendMessage(title='清大計算機中心', address='清大計算機中心', latitude=24.794308, longitude=120.993361)

    template_list.append(text_template_1)
    template_list.append(place_template_1)
    template_list.append(text_template_2)
    template_list.append(place_template_2)

    return template_list

def schedule():
    template_list = []
    schedule_1_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/eEHZAhO.png', 
        preview_image_url='https://i.imgur.com/eEHZAhO.png'
    )
    schedule_2_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/fQYlhpL.png', 
        preview_image_url='https://i.imgur.com/fQYlhpL.png'
    )

    template_list.append(schedule_1_template)
    template_list.append(schedule_2_template)

    return template_list

def traffic(): 
    template_list = []

    text_template_1 = TextSendMessage(text='''1. 高鐵接駁：國光客運182\n
2. 市區公車：從火車站→清華大學校本部門口\n   新竹客運公車號碼 ：藍1區市區公車、2路\n
3. 計程車：從火車站→清華大學校本部門口，車資約200~250元''')
    bus_1_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/rvOk16m.jpg', 
        preview_image_url='https://i.imgur.com/rvOk16m.jpg'
    )
    text_template_2 = TextSendMessage(text="2. 市區公車：從火車站→清華大學校本部門口\n新竹客運公車號碼 ：藍1區市區公車、2路")
    bus_2_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/z91Pjnc.jpg', 
        preview_image_url='https://i.imgur.com/z91Pjnc.jpg'
    )
    bus_3_template = ImageSendMessage(
        original_content_url='https://i.imgur.com/TbGEtNI.jpg', 
        preview_image_url='https://i.imgur.com/TbGEtNI.jpg'
    )

    text_template_3 = TextSendMessage(text="3. 計程車:：從火車站→清華大學校本部門口，車資約200~250元")

    template_list.append(text_template_1)
    template_list.append(bus_1_template)
    template_list.append(bus_2_template)
    template_list.append(bus_3_template)

    return template_list

def items():
    text_template = TextSendMessage(text='''✅ 筆電(平板)、充電線\n
✅ 個人環保餐具、吸管\n
✅ 口罩\n
✅ 個人文具用品\n
✅ 個人住宿之衣物及用品\n
✅ 個人藥品''')

    return text_template

def cancel():
    text_template = TextSendMessage(text='''1. 因不可抗力或不可歸責之因素而須取消活動，將擇期辦理；擇期無法參加者或是活動無法擇期辦理將全額退費。\n
2. 2020年8月1日（含）前取消可全額退費。\n
3. 2020年8月2日～2020年8月14日（含）取消可退50%。\n
4. 2020年8月15日～16日活動當天未到取消，或無法全程參與，恕不退費。\n
5. 如因生病、健康或其他不可抗力歸責之因素無法參加活動，需提出相關證明後評估是否予以退費。''')

    return text_template
