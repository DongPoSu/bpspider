# coding=utf-8


class TestBean:
    def __init__(self, test_id, test_name, catagory_id, type=None, delete_flag=None,sort_index=None):
        self.test_id = test_id
        self.test_name = test_name
        self.catagory_id = catagory_id
        self.type = type
        self.delete_flag = delete_flag
        self.sort_index = sort_index

class TestSubject:
    def __init__(self, test_id, content, right_answer=None, sort_index=None,delete_flag=None):
        self.test_id = test_id
        self.content = content
        self.right_answer = right_answer
        self.sort_index = sort_index
        self.delete_flag = delete_flag
