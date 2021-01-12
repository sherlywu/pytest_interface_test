"""
评论回帖相关
"""
import requests
import pytest
from config.config_data import test_data, test_token, test_rid

# 新建评论
@pytest.mark.run(order=4)
def test_reply_topic():

    reply_topic_url = f"http://49.233.108.117:3000/api/v1/topic/{test_data['tid']}/replies"
    # reply_topic_url = "http://49.233.108.117:3000/api/v1/topic/5ff32684f5359a22db35a9f3/replies"
    reply_topic_data = {
        "accesstoken": test_token,
        "content": "这是评论接口自动发送的评论"
    }
    r = requests.post(url=reply_topic_url, json=reply_topic_data)
    test_rid['rid'] = r.json()['reply_id']

    assert r.status_code == 200
    assert r.json()['reply_id'] != None


# 为评论点赞
def test_reply_ups():
    reply_ups_url = f"http://49.233.108.117:3000/api/v1/reply/{test_rid['rid']}/ups"
    # reply_ups_url = f"http://49.233.108.117:3000/api/v1/reply/5ff32accf5359a22db35aa05/ups"
    reply_ups_data = {
        "accesstoken": test_token
    }
    r = requests.post(url=reply_ups_url, json=reply_ups_data)

    assert r.status_code == 200
    assert r.json()['success'] == True