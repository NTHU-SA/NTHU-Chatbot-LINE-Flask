from API.baseAPI import API
import requests

class PhoneAPI(API):
    def __init__(self):
        super().__init__()
        self.phone_url = self.URL + '/phone/list'
        
    def getPhonelist(self):
        ''' 取得校園單位電話
            Return:
                - lists: 電話列表
                - err
        '''

        lists = []
        err = None

        url = self.phone_url
        
        try:
            r = requests.get(url)
            r_json = r.json()

            lists = []
            err = None
            if r.status_code == 200:
                lists = r_json['result']
                return lists, err
            elif r.status_code == 404:
                    err = 'api not found'
                    return lists, err
            elif r.status_code == 503:
                err = 'Service Unavailable'
                return lists, err
        except:
            err = 'phone lists get error'
            return lists, err

