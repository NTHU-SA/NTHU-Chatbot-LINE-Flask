from fuzzywuzzy import fuzz, process

from qa_engine.loader import data_loader

class QA_Engine:
    def __init__(self):
        pass

    def load_data(self, category):
        self.data = data_loader(category)

    def _get_data_ques_list(self):
        ques_list = []
        for qa in self.data:
            ques_list.append(qa['ques'])

        return ques_list

    def _get_index_of_ques(self, q):
        for idx, qa in enumerate(self.data):
            if qa['ques'] == q:
                return idx

    def _get_ans(self, q):
        q_idx = self._get_index_of_ques(q)
        return self.data[q_idx]['ans']

    def match_ans(self, q):
        ques_list = self._get_data_ques_list()
        result = process.extractOne(q, ques_list, scorer=fuzz.token_sort_ratio, score_cutoff=5)

        if result == None:
            none_msg = '''汪汪，說目前找不到答案，如有我們沒有捕捉到的資訊。你可以到「神奇海螺」→「問題回饋」新增你想詢的問題，我們會盡快找到答案！'''
            return none_msg
        else:
            ans = self._get_ans(result[0])
            return ans
