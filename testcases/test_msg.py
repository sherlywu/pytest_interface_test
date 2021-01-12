"""
消息通知相关API
"""
import requests
from config.config_data import test_token, msg_id

# 获取未读消息
def test_unread_msg():
    unread_msg_url = "http://49.233.108.117:3000/api/v1/message/count"
    unread_msg_params = {
        "accesstoken": test_token
    }
    r = requests.get(url=unread_msg_url, params=unread_msg_params)

    assert r.status_code == 200
    assert r.json()['success'] == True

# 获取已读消息和未读消息
def test_all_msg():
    all_msg_url = "http://49.233.108.117:3000/api/v1/messages"
    all_msg_params = {
        "accesstoken": test_token
    }
    r = requests.get(url=all_msg_url, params=all_msg_params)
    assert r.status_code == 200
    assert r.json()['success'] == True

# 标记全部已读
def test_mark_all_read():
    mark_all_read_url = "http://49.233.108.117:3000/api/v1/message/mark_all"
    mark_all_read_data = {
        "accesstoken": test_token
    }
    r = requests.post(url=mark_all_read_url, json=mark_all_read_data)
    assert r.status_code == 200
    assert r.json()['success'] == True

# 标记单个已读
def test_mark_one_read():
    mark_one_read_url = f"http://49.233.108.117:3000/api/v1/message/mark_one/{msg_id}"
    mark_one_read_data = {
        "accesstoken": test_token
    }
    r = requests.post(url=mark_one_read_url, json=mark_one_read_data)

    assert r.status_code == 200
    assert r.json()['marked_msg_id'] == msg_id
