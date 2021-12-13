from linebot.models import *

def linggle_carousel():
    carousel_template = TemplateSendMessage(        
        alt_text = '【清大資工 AI+英語暑期工作坊】活動懶人包',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '活動集合時間及地點',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=linggle&info=timeplace'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '2日課程流程表',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=linggle&info=schedule'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '攜帶物品清單',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=linggle&info=items'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '交通指南: 我如何到清華？',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=linggle&info=traffic'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '住宿指南：鄰近清華的住宿資訊',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        URITemplateAction(
                        label='取得資訊',
                        uri='https://reurl.cc/E7yYy0'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '活動取消及退費標準',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        PostbackTemplateAction(
                            label='取得資訊',
                            data='source=richmenu&flag=linggle&info=cancel'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '使用Linggle應用程式',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        URITemplateAction(
                        label='取得資訊',
                        uri='http://home.linggle.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '聯絡我們：Linggle by nlplab',
                    text = '【清大資工 AI+英語暑期工作坊】',
                    actions = [
                        URITemplateAction(
                        label='取得資訊',
                        uri='https://www.facebook.com/Lingglebynlplab/'
                        )
                    ]
                ),
            ]
        )
    )

    return carousel_template