"""
用户相关
"""
import requests
from config.config_data import loginname

def test_loginname():

    loginname_url = f"http://49.233.108.117:3000/api/v1/user/{loginname}"
    r = requests.get(url=loginname_url)
    assert r.status_code == 200
    assert r.json()['success'] == True


