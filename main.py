
import math


print('=========00-python基础-字符串和编码=========')
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
score001 = 72
score002 = 85
total00 = 100
r00 = (score002-score001)/total00
print('提升的百分点：{0:.1f}'.format(r00))


print('=========01-python基础-使用list和tuple=========')
# 请用索引取出下面list的指定元素：打印Apple，打印Python，打印Lisa
L01 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L01[0][0])
print(L01[1][1])
print(L01[2][2])
list01 = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
L01.append(list01)  # 插入一个list
print(L01)
city01 = 'Hangzhou'
list01.insert(4, city01)  # 在第几个位置插入城市（对象）
print(list01)
list01.pop()  # 删除末尾的元素，需删除某个指定的元素需要加上索引号，如.pop(1)
print(list01)
# tuple的注意事项：
'''
1、元组一旦初始化就不能修改，因此没有列表的增删改查
2、元组不可变所以代码更安全，可联想E6中的const和let的用法
3、定义元组的时候尽量先确定好元组的元素，空tuple ()
'''

print('=========03-python基础-条件判断=========')
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
'''
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height03 = 1.75
weight03 = 80.5
if weight03 < 18.5:
    print('过轻')
elif 18.5 < weight03 < 25:
    print('正常')
elif 25 < weight03 < 28:
    print('过重')
elif 28 < weight03 < 32:
    print('肥胖')
else:
    print('严重肥胖')

print('=========04-python基础-循环=========')
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L04 = ['Bart', 'Lisa', 'Adam']
for i in L04:
    print('Hello,{0}'.format(i))
sum04 = 0
for x in range(101):
    sum04 += x
print(sum04)
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
n04 = 11
while n04 <= 100:
    if n04 > 10:
        break  # 满足条件结束循环；同理 continue
    print(n04)
    n04 += 1
print(n04)

print('=========05-python基础-使用dict和set=========')
d05 = {'Politics': 72, 'English': 81, 'Major': 243}
sum05 = d05['Politics'] + d05['English'] + d05['Major']
print(sum05)
s05 = set([72, 81, 243])  # 不加列表[]报错，
other05 = set([12, 72, 88])
print(s05 & other05)  # 交集&和并集|

