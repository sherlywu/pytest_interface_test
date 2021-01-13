import requests
import pytest
from file_tools.csv_handler import read_csv_to_dict

import os
# 使用os模块进行路径拼接
topics_data_file = os.path.join(os.path.dirname(__file__), '../test_data_files/data.csv')

# __file__ 内置的全局变量，表示当前文件的绝对路径
print(__file__)  # /Users/wuyanjiao/2020/python进阶班/projects/pytest_interface_test/testcases/test_ddt_csv_example.py
# 当前文件目录的绝对路径
print(os.path.dirname(__file__))  # /Users/wuyanjiao/2020/python进阶班/projects/pytest_interface_test/testcases
current_dir = os.path.dirname(__file__)
# 将路径进行拼接  # /Users/wuyanjiao/2020/python进阶班/projects/pytest_interface_test/testcases/../test_data.files/data.csv
print(os.path.join(current_dir, '../test_data.files/data.csv'))


testdata = read_csv_to_dict(topics_data_file)
print(testdata)

@pytest.mark.parametrize('test_data,status_code,except_val', testdata)
def test_create_topic(test_data, status_code, except_val):
    create_url = "http://49.233.108.117:3000/api/v1/topics"
    r = requests.post(url=create_url, json=test_data)
    print(r.json(), r.status_code)
    assert r.json() == except_val
    assert r.status_code == status_code