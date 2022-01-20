import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://root:Aa123456!@123.57.149.19:10003/job/AutoApi/allure/widgets/suites.json"
        self.ding = "https://oapi.dingtalk.com/robot/send?access_token=3a26b22b2d86dd60c336511be1cfc93baccec11bab4b1a19e8d3a320f3215e75"
        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "秦至诚账号root,密码Aa123456！",
                    "title": "秦至诚" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://root:Aa123456!@123.57.149.19:10003/job/AutoApi/allure/"
                }
            }
            requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
