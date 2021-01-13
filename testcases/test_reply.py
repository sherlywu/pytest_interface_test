"""
评论回帖相关API
"""
import requests
import pytest
from config.config_data import test_data, test_token, base_url


# ${reply_id} 作为变量为下次运行使用 类似于jmeter
test_reply_data =[
    ({"accesstoken": test_token, "content": 'pytest的接口自动化测试'}, 200, {'success': True, 'reply_id': '${reply_id}'}),
    ({"accesstoken": test_token, "content": '回复评论的回帖', 'reply_id': '${reply_id}'}, 200, {'success': True, 'reply_id': '${reply_id}'})
]

@pytest.mark.parametrize('reply_data,status_code,except_val', test_reply_data)
@pytest.mark.run(order=-1)
@pytest.mark.tmp
def test_reply_topic(reply_data, status_code, except_val):
    topic_id = test_data['tid']
    url = base_url + f"/topic/{topic_id}/replies"
    # 如果有reply_id
    if reply_data.get('reply_id'):
        reply_data['reply_id'] = test_data['reply_id']

    r = requests.post(url=url, json=reply_data)
    print('reply:', r.json())
    if except_val.get('reply_id') == '${reply_id}':
        test_data['reply_id'] = r.json()['reply_id']  # 将第一次接口中reply_id 赋给变量

    except_val['reply_id'] = r.json()['reply_id']
    assert r.status_code == status_code
    assert r.json() == except_val


# # 为评论点赞
# def test_reply_ups():
#     reply_ups_url = f"http://49.233.108.117:3000/api/v1/reply/{test_rid['rid']}/ups"
#     # reply_ups_url = f"http://49.233.108.117:3000/api/v1/reply/5ff32accf5359a22db35aa05/ups"
#     reply_ups_data = {
#         "accesstoken": test_token
#     }
#     r = requests.post(url=reply_ups_url, json=reply_ups_data)
#
#     assert r.status_code == 200
#     assert r.json()['success'] == True