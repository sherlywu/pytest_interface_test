"""
主要是演示fixture脚手架的用法

因为很多接口都依赖发布话题--topic_id
"""
from config.config_data import test_token,base_url
import requests
import pytest


@pytest.fixture()
def get_topic_id():
    create_url = " http://49.233.108.117:3000/api/v1/topics"
    create_data = {
        "accesstoken": test_token,
        "title": "学习接口测试",
        "tab": "ask",
        "content": "使用requests第三方库做post请求的接口测试"
    }
    r = requests.post(url=create_url, json=create_data)
    return r.json()['topic_id']  # 将id返回

def test_update_topic(get_topic_id):
    url = base_url + '/topics/update'
    testdata = {
        "accesstoken": test_token,
        "topic_id": get_topic_id,
        "tab": "ask",
        "title": "这是编辑主题标题",
        "content": "这是编辑主题的具体内容"
    }
    print(testdata)

def test_reply_topic(get_topic_id):
    print(get_topic_id)