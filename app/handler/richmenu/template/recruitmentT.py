from linebot.models import *

def recruitment_carousel(data:list):
    template_list = []

    data_blocks = []
    while len(data) > 10:
        data_blocks.append(data[0:10])
        data = data[10:len(data)]
    data_blocks.append(data)

    
    for block in data_blocks:
        columns = []
        for item in block:
            # check title len < 40
            item['title'] = item['title'].replace('本校', '')
            if len(item['title']) > 40:
                item['title'] = item['title'][0:37] + '...'

            col = CarouselColumn(
                title=item['title'],
                text='發佈日期：' + item['date'],
                actions=[
                    URITemplateAction(
                        label='更多資訊',
                        uri=item['url']
                    )
                ]
            )
            columns.append(col)

        Carousel_template = TemplateSendMessage(
            alt_text='清華校內工讀',
            template=CarouselTemplate(
                columns=columns
            )
        )
        template_list.append(Carousel_template)

    return template_list