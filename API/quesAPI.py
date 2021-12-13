from API.baseAPI import API
import requests

class QuesAPI(API):
    def __init__(self):
        super().__init__()
        self.affair_url = self.URL + '/affair'
        
    def ques(self, ques):
        ''' 取得校務問題的回答
            Params:
                - ques: 校務問題
            Return:
                - ans: 校務回答
                - err
        '''

        ans = ''
        err = None

        url = self.affair_url + '/ques'
        payload = {'ques': ques}
        
        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                ans = r_json['result']['ans']
                return ans, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return ans, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return ans, err
        except:
            err = 'affair ques error'
            return ans, err


