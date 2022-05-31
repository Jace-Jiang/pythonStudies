# https://www.runoob.com/python3/python3-area-triangle.html

a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 半周长
s = (a + b + c) / 2
# 面积
# 三角形面积计算公式：
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 # 海伦公式
# area前多了%是什么意思？  %操作符 https://www.php.cn/python-tutorials-424360.html
'''
    %s    字符串 (采用str()的显示)
    %r    字符串 (采用repr()的显示)
    %c    单个字符
    %b    二进制整数
    %d    十进制整数
    %i    十进制整数
    %o    八进制整数
    %x    十六进制整数
    %e    指数 (基底写为e)
    %E    指数 (基底写为E)
    %f    浮点数
    %F    浮点数，与上相同
    %g    指数(e)或浮点数 (根据显示长度)
    %G    指数(E)或浮点数 (根据显示长度)
    %%    字符"%"
'''
print('三角形面积为 %0.2f' %area)




# 通过用户输入三角形三边长度，并计算三角形的面积
# 已知三角形三边a,b,c，则
# （海伦公式）（p=(a+b+c)/2）
# S=sqrt[p(p-a)(p-b)(p-c)]
# =sqrt[(1/16)(a+b+c)(a+b-c)(a+c-b)(b+c-a)]
# =1/4sqrt[(a+b+c)(a+b-c)(a+c-b)(b+c-a)]

import math
import unicodedata
# 定义函数判断输入数据是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.digit(s)    # digit 把一个合法的数字字符串转换为数字值
        return True
    except (TypeError, ValueError):
        pass
    return False
def calculate(a, b, c):
    if is_number(a) and is_number(b) and is_number(c):
        a = float(a)
        b = float(b)
        c = float(c)
        if a > 0  and b > 0 and c >0:
            while a+b<=c or a+c<=b or b+c<=a:
                print("输入的边长无法构成三角形！！！")
                a = input('输入三角形边长a: ')
                b = input('输入三角形边长b: ')
                c = input('输入三角形边长c: ')
                calculate(a,b,c)
            p = (a+b+c)/2
            area = math.sqrt(p*(p - a)*(p - b)*(p - c))
            print("三角形面积为：%0.2f" %area)
        else:
            print("三角形的边长必须大于0，请输入大于0的数！！！")
    else:
        print('请输入数字类型！！！')
a = input('输入三角形边长a: ')
b = input('输入三角形边长b: ')
c = input('输入三角形边长c: ')
calculate(a,b,c)