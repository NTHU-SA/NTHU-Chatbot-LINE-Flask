from API.baseAPI import API
import requests

class TokenAPI(API):
    def __init__(self):
        super().__init__()
        self.token_url = self.URL + '/token'
        
    def getAuth(self, mode):
        ''' 取得LINE的token & webhook
            Params:
                - mode: APP的模式(official/beta)
            Return:
                - token
                - webhook
                - err
        '''
        token = ''
        webhook = ''
        err = None

        url = self.token_url + '/auth'
        payload = {'mode': mode}

        try:
            r = requests.get(url, params=payload)
            r_json = r.json()

            if r.status_code == 200:
                token = r_json['result']['token']
                webhook = r_json['result']['webhook']
                return token, webhook, err
            elif r.status_code == 404:
                err = 'api not found，404'
                return token, webhook, err
            elif r.status_code == 503:
                err = 'Service Unavailable，503'
                return token, webhook, err
        except:
            err = 'get LINE auth token & webhook error'
            return token, webhook, err