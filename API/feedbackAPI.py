from API.baseAPI import API
import requests

class FeedbackAPI(API):
    def __init__(self):
        super().__init__()
        self.feedback_url = self.URL + '/feedback'
        
    def insertOne(self, category, user_id, content):
        ''' 使用者回饋
            Params:
                - category: 回饋的類型 (normal, epidemic)
                - user_id: 賴使用者的id
                - content: 回饋內容
            Return:
                - err
        '''

        err = None

        url = self.feedback_url + '/insertOne'
        data = {
            'userID': user_id,
            'category': category,
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
            err = 'feedback insertOne error'
            return err

