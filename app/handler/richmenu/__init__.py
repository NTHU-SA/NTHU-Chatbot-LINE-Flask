from datetime import datetime
from linebot.models import *
import json

from app import app
from API import UserAPI, BusAPI, DataAPI, TimebankAPI
from app.handler.richmenu.template import busT, epidemicT, locationT, stopT, affairT, recnewsT, linggleT, usrT, phoneT, recruitmentT, pointT
from app.handler.command.template import IntroTemplate
from utils import busUtil, locationUtil, recnewUtil, schoolRecruitUtil


class RichmenuHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance
    
    def detect(self, msg):
        '''判斷是否為選單事件
            Params:
                - msg
            Return:
                - isRichmenu(bool): 若開頭為 [選單]
        '''

        if msg[0:4] == '[選單]':
            return True
        else:
            return False

    def extract_msg(self, msg):
        return msg[4:]

    def run(self, event, msg):
        em = self.extract_msg(msg)
        user_id = event.source.user_id
        reply_token = event.reply_token

        user = UserAPI()

        location = []
        items = []
        recnews = []
        news = []

        if em == "校園公車時間表": #回覆公車路線template
            self.line_bot_api.reply_message(reply_token, busT.bus_route_template())
        elif em == "校園地圖查詢":
            location,err = user.getMapRecord(user_id)
            if err:
                self.line_bot_api.reply_message(reply_token, TextSendMessage(text=err))
            elif not location:  #若取得map record為空
                self.line_bot_api.reply_message(reply_token, locationT.intro())
            elif location:
                items = locationUtil.create_location_list(location)
                self.line_bot_api.reply_message(reply_token, locationT.personal_intro(items))
            self.user.setFlag(user_id, 'mapping')
        # elif em == "新增新型冠狀病毒相關問題":  #ˋ4/5先拔除
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_feedback())
        #     self.user.setFlag(user_id, 'epidemic_feedback')
        elif em == "防疫Q&A":
            self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
            self.user.setFlag(user_id, 'epidemic_qa')
        elif em == "新型冠狀病毒相關公告":
            self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_info_carousel())
        elif em == "校務專區":
            self.line_bot_api.reply_message(reply_token, affairT.affair_info_carousel())
        elif em == "哈哈":
            self.line_bot_api.link_rich_menu_to_user(user_id, "richmenu-40a91b3a104119f90757b48253ab9c11")
        # TODO: USR專區
        # elif em == '清華大學USR':
        #     self.line_bot_api.reply_message(reply_token, usrT.usr_carousel())

        # TODO: 校內工讀
        elif em == '清華校內工讀':
            recruitment_list = schoolRecruitUtil.get_list()
            self.line_bot_api.reply_message(reply_token, recruitmentT.recruitment_carousel(recruitment_list))



class PostbackHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def run(self, event, param):
        user_id = event.source.user_id
        reply_token = event.reply_token

        user = UserAPI()
        _data = DataAPI()

        if param.get('flag') == 'epidemic':
            if param.get('info') == 'qa':  
                self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
                self.user.setFlag(user_id, 'epidemic_qa')
            if param.get('info') == 'students':
                epid_content, err = _data.getEpid('students')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得防疫資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                else:
                    self.line_bot_api.reply_message(reply_token, epidemicT.students_carousel_render(epid_content))
                    # self.line_bot_api.reply_message(reply_token, epidemicT.students_info())

            # 屬於純text的防疫category
            else:
                epid_category = param.get('info')
                epid_content, err = _data.getEpid(epid_category)
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得防疫資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                else:
                    self.line_bot_api.reply_message(reply_token, epidemicT.epid_content_render(epid_content))

            # elif param.get('info') == 'boarders':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.boarders_info())
            # elif param.get('info') == 'backtw':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.backtw_info())
            # elif param.get('info') == 'isolation':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.isolation_info())
            # elif param.get('info') == 'foreign':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.foreign_info())
            # elif param.get('info') == 'chinastudent':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.chinastudent_info())
            # elif param.get('info') == 'tkm':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.tkm_info())
            # elif param.get('info') == 'change2tkm':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.change2tkm_info())
            # elif param.get('info') == 'contact':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.contact_info())

        elif param.get('flag') == 'affair':
            if param.get('info') == 'qa':
                self.line_bot_api.reply_message(reply_token, affairT.qa_info())
                self.user.setFlag(user_id, 'affair_qa')
            elif param.get('info') == 'recnews':
                    self.line_bot_api.reply_message(reply_token, affairT.recNew_type())
            elif param.get('info') == 'speech':
                recnews, err = _data.getrecNews('speech')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                elif recnews == []:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='目前沒有任何演講！'))
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(reply_token, recnewsT.recnew_carousel(news))
            elif param.get('info') == 'exhibition':
                recnews, err = _data.getrecNews('exhibition')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                elif recnews == []:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='目前沒有任何展覽！'))
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(reply_token, recnewsT.recnew_carousel(news))
            elif param.get('info') == 'activity':
                recnews, err = _data.getrecNews('activity')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                elif recnews == []:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='目前沒有任何活動！'))
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(reply_token, recnewsT.recnew_carousel(news))
            elif param.get('info') == 'phone':
                self.line_bot_api.reply_message(reply_token, phoneT.qa_info())
                self.user.setFlag(user_id, 'phone_qa')
        elif param.get('flag') == 'intro':
            if param.get('info') == 'share':
                self.line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text="分享QRcode", contents=json.loads(IntroTemplate.share_template())))
        elif param.get('flag') == 'bus':
            if param.get('info') == 'main_campus':
                self.line_bot_api.reply_message(reply_token, busT.main_campus_bus_img())
            elif param.get('info') == 'minor_campus':
                self.line_bot_api.reply_message(reply_token, busT.minor_campus_bus_img())
            elif param.get('info') == '83_bus':
                self.line_bot_api.reply_message(reply_token, busT.et_bus_img())
            # elif param.get('info') == 'dyn_search':
            #     self.line_bot_api.reply_message(reply_token, busT.dynbus_geton_loc_template())
        # elif param.get('flag') == 'dynbus_geton':
        #     geton_loc = param.get('info') # 上車地點
        #     self.line_bot_api.reply_message(reply_token, busT.dynbus_getoff_loc_template(geton_loc))
        # elif param.get('flag') == 'dynbus_getoff':
        #     info = param.get('info')
        #     info_list = info.split('~')
        #     geton_loc = info_list[0] # 上車地點
        #     getoff_loc = info_list[1] # 下車地點
            
        #     print('geton_loc:', geton_loc)
        #     print('getoff_loc:', getoff_loc)
            
        #     # 判斷 climb||descend(str) 及 line[]
        #     direction, line = busUtil.check_direction_and_line(busUtil.BUS_LOC_MAP_EN[geton_loc], busUtil.BUS_LOC_MAP_EN[getoff_loc])

        #     print('direction:', direction)
        #     print('line:', line)

        #     # 現在時間
        #     theTime = datetime.now()
        #     theTime = theTime.strftime('%H:%M:%S')
            
        #     # request to BusAPI
        #     bus = BusAPI()

        #     flex_contents = []
        #     arriveTime_list = []
        #     for l in line:
        #         arriveTime, waitTime, err = bus.schedule(theTime, 'campus', direction, l, busUtil.BUS_LOC_MAP_EN[geton_loc])
        #         if err:
        #             self.line_bot_api.reply_message(reply_token, TextSendMessage(text='動態校車查詢失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                
        #         if arriveTime=='' and waitTime=='':
        #             print('此刻沒有班次')
        #             break
                
        #         print('arriveTime:', arriveTime)
        #         print('waitTime:', waitTime)
        #         arriveTime_list.append(arriveTime)

        #         dync_bus_flex_content = busT.dync_result_flex_json_content(busUtil.BUS_LOC_MAP_EN[geton_loc], busUtil.BUS_LOC_MAP_EN[getoff_loc], l, arriveTime, waitTime)
        #         flex_contents.append(dync_bus_flex_content)

        #     # 排序arriveTime, 快的車排前面
        #     if len(arriveTime_list) > 1:
        #         t0 = datetime.strptime(arriveTime_list[0], '%H:%M:%S')
        #         t1 = datetime.strptime(arriveTime_list[1], '%H:%M:%S')
                
        #         if t1 < t0:
        #             temp = flex_contents[0]
        #             flex_contents[0] = flex_contents[1]
        #             flex_contents[1] = temp
        #             print('sort flex_contents')
            
        #     if len(flex_contents) == 0:
        #         self.line_bot_api.reply_message(reply_token, TextSendMessage(text='此時段沒有班次呦，嗷嗷！'))
        #     else:
        #         self.line_bot_api.reply_message(reply_token, busT.dync_result_flex_carousel_template(flex_contents))

        # elif param.get('flag') == 'stop':
        #     if param.get('info') == 'qa':
        #         self.line_bot_api.reply_message(reply_token, stopT.stop_qa())
        #     if param.get('info') == 'signin':
        #         self.line_bot_api.reply_message(reply_token, stopT.cancel_sign())


