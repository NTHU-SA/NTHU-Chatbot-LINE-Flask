import requests

class API:
    def __init__(self):
        self.URL = 'http://34.120.176.132/api/v1'
        #self.URL = 'http://127.0.0.1:5000/api/v1'
        self.liff_URL = 'https://liff-nthu-chatbot.ml/api/v1'
        
    def ping(self):
        url = self.URL + '/ping'
        
        try:
            r = requests.get(url).json()

            if r.status_code == 200:
                print(r['msg'])
        except:
            print('ping error')