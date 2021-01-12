"""
使用pytest 进行数据驱动 样例文件
"""
import pytest
import requests
from config.config_data import test_token

@pytest.mark.skip
@pytest.mark.parametrize('x, y', [(1, 2), (4, 2), (5, 6), (6, 6), (10.1, 9.1)])
def test_xy(x, y):
    assert x < y


test_ddt_data = [
    ({"accesstoken": "", "title": "学习接口测试", "tab": "ask","content": "abcdfeg"}, 401, {'success': False, 'error_msg': '错误的accessToken'}),
    ({"accesstoken": test_token, "title": "", "tab": "ask", "content": "abcdfeg"}, 400, {'success': False, 'error_msg': '标题不能为空'}),
    ({"accesstoken": test_token, "title": "1234567", "tab": "", "content": "abcdfeg"}, 400, {'success': False, 'error_msg': '必须选择一个版块'}),
    ({"accesstoken": test_token, "title": "1234567", "tab": "ask", "content": ""}, 400, {'success': False, 'error_msg': '内容不可为空'})
]

@pytest.mark.parametrize('test_data,status_code,except_val', test_ddt_data)
def test_create_topic(test_data, status_code, except_val):
    create_url = "http://49.233.108.117:3000/api/v1/topics"
    r = requests.post(url=create_url, json=test_data)
    print(r.json(), r.status_code)
    assert r.json() == except_val
    assert r.status_code == status_code