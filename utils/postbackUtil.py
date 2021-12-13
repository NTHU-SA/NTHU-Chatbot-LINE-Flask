''' 處理 postback event 的工具包 '''

class Param:
    def __init__(self, source=None, flag=None, info=None):
        self.source = source
        self.flag = flag
        self.info = info

    def get(self, k):
        if k == 'source':
            return self.source
        elif k == 'flag':
            return self.flag
        elif k == 'info':
            return self.info


def parse(data):
    '''解析 postback data
        Params:
            - data string. source=richmenu&flag=epidemic&info=students
        Return:
            - p Param
    '''

    param_obj = {
        'source': '',
        'flag': '',
        'info': ''
    }

    and_split = data.split('&')
    for item in and_split:
        key_value_split = item.split('=')
        k = key_value_split[0]
        v = key_value_split[1]

        param_obj[k] = v


    return Param(param_obj['source'], param_obj['flag'], param_obj['info'])


    


