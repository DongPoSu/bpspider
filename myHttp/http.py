# coding=utf-8

import requests
from requests import RequestException

from constant import METHOD_GET


class HttpLib:


    def __init__(self, bean):
        self.bean = bean

    def request(self):
        if METHOD_GET == self.bean.method:
            return self.get()
        else:
            return self.post()

    def get(self):
        try:
            response = requests.get(self.bean.url, headers=self.bean.headers, timeout=self.bean.timeout)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return response.text
            else:
                raise Exception(response.content)
        except RequestException as err:
            print(err)

    def post(self):
        try:
            response = requests.post(self.bean.url, headers=self.bean.headers, data=self.bean.data,
                                     timeout=self.bean.timeout)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return response.text
            else:
                return response.status_code
        except RequestException as err:
            print(err)
