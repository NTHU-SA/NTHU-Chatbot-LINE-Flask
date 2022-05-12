from API.baseAPI import API
import requests

class UserAPI(API):
    def __init__(self):
        super().__init__()
        self.user_url = self.URL + '/user'
        
    def insertOne(self, user_id):
        ''' 新增一位用戶
            Params:
                - user_id: 賴使用者的id
            Return:
                - err
        '''

        err = None

        url = self.user_url + '/insertOne'
        data = {
            'userID': user_id,
        }
        
        try:
            r = requests.post(url, data=data)
            r_json = r.json()

            if r.status_code == 200:
                return err
            elif r.status_code == 404:
                err = '新增ID失敗，404'
                return err
            elif r.status_code == 503:
                err = '新增ID失敗，503'
                return err
        except:
            err = 'user insertOne error'
            return err


    def isExist(self, user_id):
        ''' 用戶是否存在
            Params:
                - user_id: 賴使用者的id
            Return:
                - isExist(Boolean): 是否存在
                - err
        '''

        isExist = ''
        err = None

        url = self.user_url + '/isExist'
        payload = {'userID': user_id}
        
        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                isExist = r_json['result']['isExist']
                return isExist, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return isExist, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return isExist, err
        except:
            err = 'user isExist error'
            return isExist, err
    

    def getFlag(self, user_id):
        ''' 取得flag
            Params:
                - user_id: 賴使用者的id
            Return:
                - flag(String): 對話狀態
                - err
        '''

        flag = ''
        err = None

        url = self.user_url + '/getFlag'
        payload = {'userID': user_id}
        
        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                flag = r_json['result']['flag']
                return flag, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return flag, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return flag, err
        except:
            err = 'user getFlag error'
            return flag, err
    

    def initFlag(self, user_id):
        ''' 初始化flag
            Params:
                - user_id: 賴使用者的id
            Return:
                - err
        '''

        err = None

        url = self.user_url + '/initFlag'
        data = {
            'userID': user_id,
        }

        try:
            r = requests.post(url, data=data)
            r_json = r.json()

            if r.status_code == 200:
                return err
            elif r.status_code == 404:
                err = 'api not found，404'
                return err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return err
        except:
            err = 'user initFlag error'
            return err
    

    def setFlag(self, user_id, flag):
        ''' 設置flag
            Params:
                - user_id: 賴使用者的id
                - flag: 對話狀態
            Return:
                - err
        '''

        err = None

        url = self.user_url + '/setFlag'
        data = {
            'userID': user_id,
            'flag': flag
        }

        try:
            r = requests.post(url, data=data)
            r_json = r.json()

            if r.status_code == 200:
                return err
            elif r.status_code == 404:
                err = 'api not found，404'
                return err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return err
        except:
            err = 'user setFlag error'
            return err
    
    def mapRecordInsertOne(self, user_id, location):
        ''' 紀錄使用者查詢地點
            Params:
                - user_id: 賴使用者的id
                - location: 地點
            Return:
                - err
        '''

        err = None

        url = self.user_url + '/map/insert'
        data = {
            'userID': user_id,
            'location': location
        }

        try:
            r = requests.post(url, data=data)
            r_json = r.json()

            if r.status_code == 200:
                return err
            elif r.status_code == 404:
                err = 'api not found，404'
                return err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return err
        except:
            err = 'user location insert error'
            return err
    
    def getMapRecord(self, user_id):
        ''' 取得使用者地點查詢記錄
            Params:
                - user_id: 賴使用者的id
            Return:
                - location[]: 地點陣列
                - err
        '''
        location = []
        err = None

        url = self.user_url + '/map/record'
        payload = {'userID': user_id}
        
        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                location = r_json['result']
                return location, None
            elif r.status_code == 404:
                err = 'api not found，404'
                return None, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return None, err
        except:
            err = 'user location record error'
            return None, err
    
    def updateBroadcastTag(self, user_id, tag):
        '''設定使用者的上次被推播的時間戳
            Params:
                - user_id: 賴使用者的id
                - tag: Timestamp
            Return:
                - err
        '''
        err = None

        url = self.user_url + '/updateBroadcastTag'
        data = {
            'userID': user_id,
            'tag': tag
        }

        try:
            r = requests.post(url, data=data)
            r_json = r.json()

            if r.status_code == 200:
                return err
            elif r.status_code == 404:
                err = 'api not found，404'
                return err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return err
        except:
            err = 'user broadcast tag update error'
            return err

    def getBroadcastAudienceIds(self, user_id):
        '''取得要被推播的使用者 id
            Params:
                - user_id: 賴使用者的id (Optional)
            Return:
                - [userID]
                - err
        '''
        err = None

        url = self.user_url + '/getBroadcastAudienceIds'
        data = { 'userID': user_id }

        try:
            r = requests.get(url, data=data)
            r_json = r.json()
            ids = r_json['result']

            if r.status_code == 200:
                err = None
            elif r.status_code == 404:
                err = 'api not found，404'
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
        except:
            err = 'get user broadcast tag error'
            ids = []
        finally:
            return ids, err