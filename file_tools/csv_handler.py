import csv
import json
from config.config_data import test_token

def write_to_csv(test_data, csvfile):
    f = open(csvfile, mode='w', encoding='utf8', newline='')
    csvfile = csv.writer(f)
    for data in test_data:
        tmp = []
        tmp.append(json.dumps(data[0]))  # 将字典转换为字符串
        tmp.append(data[1])
        tmp.append(json.dumps(data[2]))
        csvfile.writerow(tmp)

def read_csv_to_dict(csvfile):
    f = open(csvfile, mode='r', encoding='utf8', newline='')
    csvfile = csv.reader(f)

    data = []
    for line in csvfile:
        tmp = []
        tmp.append(json.loads(line[0]))  # 字符串转换为 python对象
        tmp.append(int(line[1]))  # 字符串转化为int
        tmp.append(json.loads(line[2]))
        data.append(tuple(tmp))

    return data


if __name__ == '__main__':
    test_data = [
        ({"accesstoken": "", "title": "学习接口测试", "tab": "ask", "content": "abcdfeg"}, 401,
         {'success': False, 'error_msg': '错误的accessToken'}),
        ({"accesstoken": test_token, "title": "", "tab": "ask", "content": "abcdfeg"}, 400,
         {'success': False, 'error_msg': '标题不能为空'}),
        ({"accesstoken": test_token, "title": "1234567", "tab": "", "content": "abcdfeg"}, 400,
         {'success': False, 'error_msg': '必须选择一个版块'}),
        ({"accesstoken": test_token, "title": "1234567", "tab": "ask", "content": ""}, 400,
         {'success': False, 'error_msg': '内容不可为空'})
    ]
    write_to_csv(test_data=test_data,csvfile='data.csv')  # 测试写入文件

    data = read_csv_to_dict(csvfile='data.csv')
    print(data)

    assert test_data == data
