from API.baseAPI import API
import requests
from datetime import datetime

class BusAPI(API):
    def __init__(self):
        super().__init__()
        self.bus_url = self.URL + '/bus'

    def schedule(self, time, busType, direction, line, dep):
        ''' 查詢動態校車時刻
            Params:
                - time: 查詢時刻 (7:12:55)
                - busType: 校車類型 (campus)
                - direction: 校車方向 (climb/descend)
                - line: 校車路線 (red/green)
                - dep: 出發站名
            Return:
                - arriveTime: 抵達時間
                - waitTime: 等待時間
                - err
        '''

        data = []
        err = None

        url = self.bus_url + '/schedule'
        payload = {
            'time': time,
            'busType': busType,
            'direction': direction,
            'line': line,
            'dep': dep
        }

        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                data = r_json['result']
                arriveTime = data['arriveTime']
                waitTime = data['waitTime']
                return arriveTime, waitTime, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return data, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return data, err
        except:
            err = 'data get qa data error'
            return data, err