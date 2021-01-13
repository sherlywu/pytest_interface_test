import pytest
import requests

def session():
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4e8dd5b2-bf4c-4f04-9dd1-c225f5f142b2"
    data = {
        "msgtype": "text",
        "text":  {
            "content": "大家注意了！开始运行所有TestCases"
                  },
    }
    requests.post(url=url, json=data)
    yield
    # 所有用例执行完毕的操作
    data['text'] = {'content':"所有的用例已经执行完毕"}
    requests.post(url, json=data)