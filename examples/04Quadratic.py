# https://www.runoob.com/python3/python3-quadratic-roots.html

'''
二次方程，是一种整式方程，其未知项的最高次数是2，且各项未知数的次数只能是自然数。
比如根号x加x的平方等于1 ，这样未知数的的次数含有非自然数，就不是一元二次方程了。
如果一个二次方程只含有一个未知数 x，那么就称其为一元二次方程，其主要内容包括方程求解、
方程图像、一元二次函数求最值三个方面；如果一个二次方程含有二个未知数x、y，那么就称其为二元二次方程，以此类推。
'''

# 导入复杂数学运算
import cmath

a = float(input('请输入 a:'))
b = float(input('请输入 b:'))
c = float(input('请输入 c:'))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('计算结果为 {0}和{1}'.format(sol1,sol2))


# 比较完整的一元二次方程判断，实数根，复数根，提醒用户输入数字类数据
import os
import math
import cmath
def mx(a,b,c):
    mm = (b ** 2) - (4 * a * c)
    if mm > 0:
        print('此函数有两个解')
        x1=(-b+math.sqrt(mm))/(2*a)
        x2 = (-b - math.sqrt(mm)) / (2 * a)
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f} 和 x={:.0f}".format(a,b,c,x1,x2))
    elif mm ==0:
        print('此方程只有一个解')
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f}".format(a, b, c, (-b+math.sqrt(mm))/(2*a)))
    elif mm <0:
        x1=(-b+cmath.sqrt(mm))/(2*a)
        x2 = (-b - cmath.sqrt(mm)) / (2 * a)
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f} 和 x={:.0f}".format(a, b, c, x1, x2))
    else :
        print('无解')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def panduan(xx):
    if is_number(xx)==True:
        return xx
    else:
        while is_number(xx)==False:
            print('不是数字，请再次输入')
            cc =input("请输入第一个数:")
            if is_number(cc)==True:
                break
        return print('此程序用于计算一元二次方程解,请依次输入三个数')

zz=input("是否要开始计算:yes/no——:")
while zz =='yes':
    a=float(panduan(input("请输入第一个数:")))
    b=float(panduan(input("请输入第二个数:")))
    c=float(panduan(input("请输入第三个数:")))
    mx(a,b,c)
    zz = input("是否还要继续计算:yes/no——:")
print('感谢使用。' ,end="")

