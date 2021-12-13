from linebot.models import *

def recnew_carousel(news):
    template_list = []
    data_blocks = []

    while len(news) > 10:
        data_blocks.append(news[0:10])
        news = news[10:len(news)]
    data_blocks.append(news)

    for i in data_blocks:
        Carousel_template = TemplateSendMessage(
                alt_text='校園活動資訊',
                template=CarouselTemplate(
                columns= i
            )
        )
        template_list.append(Carousel_template)

    return template_list