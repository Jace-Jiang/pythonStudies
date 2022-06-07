import math
import cmath

print('=========00-python基础-字符串和编码=========')
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
score001 = 72
score002 = 85
total00 = 100
r00 = (score002 - score001) / total00
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

print('=========02-python基础-条件判断=========')
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
'''
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height02 = 1.75
weight02 = 80.5
if weight02 < 18.5:
    print('过轻')
elif 18.5 < weight02 < 25:
    print('正常')
elif 25 < weight02 < 28:
    print('过重')
elif 28 < weight02 < 32:
    print('肥胖')
else:
    print('严重肥胖')

print('=========03-python基础-循环=========')
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L03 = ['Bart', 'Lisa', 'Adam']
for i in L03:
    print('Hello,{0}'.format(i))
sum03 = 0
for x in range(101):
    sum03 += x
print(sum03)
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
n03 = 11
while n03 <= 100:
    if n03 > 10:
        break  # 满足条件结束循环；同理 continue
    print(n03)
    n03 += 1
print(n03)

print('=========04-python基础-使用dict和set=========')
d04 = {'Politics': 72, 'English': 81, 'Major': 243}
sum04 = d04['Politics'] + d04['English'] + d04['Major']
print(sum04)
s04 = set([72, 81, 243])  # 不加列表[]报错，
other04 = set([12, 72, 88])
print(s04 & other04)  # 交集&和并集|

print('=========05-函数-调用函数=========')
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n105 = 255
n205 = 1000
# 常见占位符： %d,整数；%f,浮点数；%s,字符串；%x,十六进制整数
# print('整数{.0x}'.format((n105)))
# hex()是python自带的函数
print(hex(n105))
print(hex(n205))

print('=========06-函数-定义函数=========')
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0ax
# 2
#  +bx+c=0 的两个解。


def quadratic(a, b, c):
    judge = (b ** 2) - (4 * a * c)
    if judge > 0:
        print('该函数有两个解')
        x1 = (-b + math.sqrt(judge)) / (2 * a)
        x2 = (-b - math.sqrt(judge)) / (2 * a)
        print('x1={:.0f}和x2={:.0f}'.format(x1, x2))
    elif judge == 0:
        print('此方程只有一个解')
        x3 = (-b + math.sqrt(judge)) / (2 * a)
        print('x={:.0f}'.format(x3))
    elif judge < 0:
        x4 = (-b + cmath.sqrt(judge)) / (2 * a)
        x5 = (-b - cmath.sqrt(judge)) / (2 * a)
        print('x4={:.0f}和x5={:.0f}'.format(x4, x5))


print(quadratic(5, 12, 3))

print('=========07-函数-函数的参数=========')
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：


def mul(x07, y07):
    return x07 * y07


def mul07(*num):
    n = 1
    for x07 in num:
        n = n * x07
    return n


print('多个数的乘积=', mul07(5, 6, 7, 8, 9))

print('=========08-函数-递归函数=========')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
print(fact(50))

# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：


def move08(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        move08(n-1, a, c, b)
        move08(1, a, b, c)
        move08(n-1, b, a, c)


print(move08(3, 'A', 'B', 'C'))

print('=========09-高级特性-切片=========')





