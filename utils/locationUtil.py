from linebot.models import *
from random import choice

def create_location_list(location):
    item = []
    location_list = []
    for i in location:
        item.append(i)
    if len(item) != 10: #補齊至10個地點
        random_location = ['第一綜合大樓','第二綜合大樓','第三綜合大樓','學務處','總務處','註冊組','人文社會學院','水木生活中心','學生住宿組'
                            ,'小吃部','體育館','校友體育館','機車塔','清交小徑','奕園停車場','北校門口','南校門口','圖書館','風雲樓','駐警隊']
        while len(item) != 10:
            re = ''
            l = choice(random_location)
            for i in item:
                if l == i:
                    re = 'repeat'          
            if re != 'repeat':
                item.append(l)
    for loc in item:
        location_button = QuickReplyButton(
            action = MessageAction(label = loc, text = loc),
        )
        location_list.append(location_button)

    return location_list