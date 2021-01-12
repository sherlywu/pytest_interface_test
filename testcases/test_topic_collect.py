import requests
import pytest
from config.config_data import test_data, test_token, loginname

# 收藏主题
@pytest.mark.run(order=3)
@pytest.mark.smoke
def test_collect_topic():
    collect_url = "http://49.233.108.117:3000/api/v1/topic_collect/collect"
    collect_data = {
        "accesstoken": test_token,
        "topic_id": test_data["tid"]
    }
    r = requests.post(url=collect_url, json=collect_data)
    assert r.status_code == 200
    assert r.json()["success"] == True

# 取消收藏

def test_de_collect_topic():
    de_collect_url = "http://49.233.108.117:3000/api/v1/topic_collect/de_collect"
    de_collect_data = {
        "accesstoken": test_token,
        "topic_id": test_data["tid"]
    }
    r = requests.post(url=de_collect_url, json=de_collect_data)
    assert r.status_code == 200
    assert r.json()["success"] == True

# 用户所有收藏的主题
def test_all_collect_topic():
    all_collect_url = f"http://49.233.108.117:3000/api/v1/topic_collect/{loginname}"
    r = requests.get(all_collect_url)
    assert r.status_code == 200
    assert r.json()['success'] == True

