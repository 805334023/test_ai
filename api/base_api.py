import jmespath
import requests
import json


class BaseApi:
    def __init__(self):
        self.header = {"Content-Type": "application/json;charset=UTF-8",
                       "Authorization": self.get_token()}

    def send(self, data):
        r = requests.request(**data)
        return r

    def get_token(self):
        data = {'method': 'post',
                'url': 'http://123.56.138.96:3012/api/ainews-user/user/login',
                'json': {"name": "lsj1", "password": "123123"},
                'headers': {"Content-Type": "application/json;charset=UTF-8"}}
        return jmespath.search('access_token', self.send(data).json())
