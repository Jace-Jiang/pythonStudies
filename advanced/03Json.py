# https://www.runoob.com/python3/python3-json.html

import json

# 定义一个元组
data = {
    'num' : 1,
    'name': 'Jace',
    'url' : 'http://www.google.com'
}
json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("Json 对象：", json_str)
# 单引号变双引号？ 随机字母排序 moingodb 创建数据库




