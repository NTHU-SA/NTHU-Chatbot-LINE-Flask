from API.baseAPI import API
import requests

class AndxAPI(API):
    def __init__(self):
        super().__init__()
        self.andx_url = self.URL + '/andx'
        
    def insertOne(self, user_id, content):
        ''' 新增一則笑話
            Params:
                - user_id: 賴使用者的id
                - content: 笑話內容
            Return:
                - err
        '''

        err = None

        url = self.andx_url + '/insertOne'
        data = {
            'userID': user_id,
            'content': content
        }
        
        try:
            r = requests.post(url, data=data)
            r_json = r.json()
            result = r_json['msg']

            if r.status_code == 200:
                return err
            elif r.status_code == 404:
                err = 'api not found'
                return err
            elif r.status_code == 503:
                err = 'Service Unavailable'
                return err
        except:
            err = 'andx insertOne error'
            return err
                
        
    def getOne(self):
        ''' 隨機取得笑話
            Return:
                - content: 笑話內容
                - err
        '''

        content = ''
        err = None

        url = self.andx_url + '/getOne'
        
        try:
            r = requests.get(url)
            r_json = r.json()

            content = ''
            err = None
            if r.status_code == 200:
                content = r_json['result']['content']
                return content, err
            elif r.status_code == 404:
                    err = 'api not found'
                    return content, err
            elif r.status_code == 503:
                err = 'Service Unavailable'
                return content, err
        except:
            err = 'anecdote get one error'
            return content, err




