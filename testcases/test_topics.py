"""
主题相关的测试用例
"""
# 1、导入requests库
import requests
# 2、导入pytest库
import pytest
from config.config_data import test_data, test_token

# 发送get 请求
# 主题首页
def test_index_page():
    index_page_url = "http://49.233.108.117:3000/api/v1/topics"
    query_param = {
        "page": 1,
        "tab": "ask",
        "limit": 1
    }
    # 使用requests 发送get 请求
    r = requests.get(url=index_page_url, params=query_param)
    print(r)
    print('状态码为：', r.status_code)
    print('结果为(text)格式：', type(r.text), r.text)
    print('结果为(json)格式：', type(r.json()), r.json())

# 发送post请求
# 新建主题
@pytest.mark.tmp
@pytest.mark.run(order=1)
@pytest.mark.regression
@pytest.mark.smoke
def test_create_topic():
    create_url = " http://49.233.108.117:3000/api/v1/topics"
    create_data = {
        "accesstoken": test_token,
        "title": "学习接口测试",
        "tab": "ask",
        "content": "使用requests第三方库做post请求的接口测试"
    }
    r = requests.post(url=create_url, json=create_data)
    # 更新外部参数变量 tid 值
    test_data["tid"] = r.json()["topic_id"]
    print(r.status_code)
    # 判断状态码为200
    assert r.status_code == 200
    print(r.json())
    # 判断topic_id值不为空
    assert r.json()['topic_id'] != None
    print('请求头：', r.request.headers)

@pytest.mark.run(order=2)
# 编辑主题
def test_update_topic():
    update_topic_url = "http://49.233.108.117:3000/api/v1/topics/update"
    update_topic_data = {
        "accesstoken": test_token,
        "topic_id": test_data["tid"],
        "tab": "ask",
        "title": "这是编辑主题标题",
        "content": "这是编辑主题的具体内容"
    }
    r = requests.post(url=update_topic_url, json=update_topic_data)
    assert r.status_code == 200
    assert r.json()['topic_id'] != None

# 主题详情
@pytest.mark.regression
@pytest.mark.unittest
def test_query_topic():
    # 取最新的tid的值
    id = test_data["tid"]
    query_url = f"http://49.233.108.117:3000/api/v1/topic/{id}"
    print(query_url)


