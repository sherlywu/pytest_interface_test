# # 写入文件
# f = open('01.txt', mode='w', encoding='utf8')
# f.write('helloword\n')
# f.write('小明')
#
# # 读取文件
# f = open('01.txt', mode='r', encoding='utf8')
# print(f.read())

# csv写入文件
# 导入csv模块
import csv
# f = open('csv_data.csv', mode='w', encoding='utf8', newline='') # newline 换行的时候默认有回车
# csvfile = csv.writer(f)
# csvfile.writerow(['token', 'title', 'tab', 'content'])  # 传入list 格式的数据
# csvfile.writerow(['', '这是标题', 'ask', 'xxxxxxxx']) # 一次写入 一行数据
# csvfile.writerow(['', 'helloworld', 'ask','xxxxxxxxxx'])
# csvfile.writerows([('01', 'helloworld', 'ask', 'xxxxxxxxxx'), ('02', 'helloworld', 'ask', 'xxxxxxxxxx')]) # 一次写入2行数据
#
# f = open('csv_data.csv', mode='r', encoding='utf8')
# csvfile = csv.reader(f)
# for line in csvfile:
#     print(line)

# 将数据写入的csv文件
from config.config_data import test_token
test_data = [
    ({"accesstoken": "", "title": "学习接口测试", "tab": "ask","content": "abcdfeg"}, 401, {'success': False, 'error_msg': '错误的accessToken'}),
    ({"accesstoken": test_token, "title": "", "tab": "ask", "content": "abcdfeg"}, 400, {'success': False, 'error_msg': '标题不能为空'}),
    ({"accesstoken": test_token, "title": "1234567", "tab": "", "content": "abcdfeg"}, 400, {'success': False, 'error_msg': '必须选择一个版块'}),
    ({"accesstoken": test_token, "title": "1234567", "tab": "ask", "content": ""}, 400, {'success': False, 'error_msg': '内容不可为空'})
]
# 写入到csv文件
f = open('test_data.csv', mode='w', encoding='utf8', newline='')
csvfile = csv.writer(f)
# 写第一行
csvfile.writerow(["test_data", "status_code", "except_val"])
# 写第二行
csvfile.writerows(test_data)

f = open('test_data.csv', mode='r', encoding='utf8')
csvfile = csv.reader(f)
# 去掉第一行
next(csvfile)
test_data = []
for line in csvfile:
    test_data.append(line)
    print(test_data)
