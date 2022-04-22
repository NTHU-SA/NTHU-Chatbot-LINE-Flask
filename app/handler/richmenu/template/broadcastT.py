from linebot.models import *
import json

# TODO: Implement broadcast toggle template

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
