from linebot.models import *

def create_news_list(recnews): #date有問題
    news_list = []

    for i in recnews:

        # 檢查是否都有https
        token = 'https'
        if token not in i['imgUrl'] and token not in i['sourceUrl']:
            continue
        

        date = i['date'] 
        if len(date) > 1: # 判斷是單一日期或時段
            date_str = date[0] + '~' + date[1]
        else:
            date_str = date[0]
        
        if i['imgUrl']:
            url = i['imgUrl']
        else:
            url = 'https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2018/09/23/realtime/5303778.jpg&x=0&y=0&sw=0&sh=0&exp=3600'
        
        if i['sourceUrl']:
            url_text = str(i['sourceUrl'])
        else:
            url_text = 'https://reurl.cc/yZLVpq'

        # # 縮網址
        # BITLY_ACCESS_TOKEN ="21f4a9c20e4a14cea450bb8f86c67d4c7e8f04f8" 
        # b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN) 
        # uri = b.shorten(str(i['sourceUrl']))

        recnew_text = str()
        recnew_text = '活動類型：' + i['category'] + '\n' + '日期：' + date_str
        if i['time']:
            recnew_text = recnew_text + '\n' + '時間：' + i['time']
        
        if len(recnew_text) > 60:
            recnew_text = recnew_text[0:57] + '...'
        
        if len(i['title']) > 40:
            i['title'] = i['title'][0:37] + '...'

        news = CarouselColumn(
                thumbnail_image_url= url, 
                title= i['title'],
                text= recnew_text,
                actions =[
                    URITemplateAction(
                        label='更多資訊',
                        uri=url_text
                    )
                ]
            )
        
        news_list.append(news)

    return news_list