# coding=utf-8


class Bean:
    headers = {}
    data = {}
    url =""
    timeout = 10
    is_stream = False
    method = 1

    def __init__(self,):
        pass

    def set_attr(self, url=None,headers=None,data=None,method=None):
        self.url = url
        self.headers = headers
        self.data = data
        self.method = method
