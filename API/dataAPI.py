from API.baseAPI import API
import requests

class DataAPI(API):
    def __init__(self):
        super().__init__()
        self.data_url = self.URL + '/data'

    def getQA(self, category):
        ''' 取得QA資料
            Params:
                - category: QA類別
            Return:
                - data [{ques, ans}]
                - err
        '''

        data = []
        err = None

        url = self.data_url + '/qa'
        payload = {'category': category}

        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                data = r_json['result']
                return data, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return data, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return data, err
        except:
            err = 'data get qa data error'
            return data, err


    def getEpid(self, category):
        ''' 取得Epid資料
            Params:
                - category: epid類別
            Return:
                - data []string
                - err
        '''

        data = []
        err = None

        url = self.data_url + '/epidemic'
        payload = {'category': category}

        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                data = r_json['result']
                return data, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return data, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return data, err
        except:
            err = 'data get epid data error'
            return data, err
    
    def getrecNews(self, category):
        ''' 取得近期活動資訊
            Return:
                - data: [{title, category, date, time, location, imgUrl, content}]
                - err
        '''

        data = []
        err = None

        url = self.data_url + '/recNews'
        payload = {'category': category}

        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                data = r_json['result']
                return data, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return data, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return data, err
        except:
            err = 'data get recnews error'
            return data, err