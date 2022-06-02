import os
import math
import cmath


def mx(a, b, c):
    mm = (b ** 2) - (4 * a * c)
    if mm > 0:
        print('此函数有两个解')
        x1 = (-b + math.sqrt(mm)) / (2 * a)
        x2 = (-b - math.sqrt(mm)) / (2 * a)
        print("{:.0f}x**2+{:.0f}x+{:.0f}的"
              "结果为：x={:.0f} 和 x={:.0f}".format(a, b, c, x1, x2))
    elif mm == 0:
        print('此方程只有一个解')
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f}".format(a, b, c, (-b + math.sqrt(mm)) / (2 * a)))
    elif mm < 0:
        x1 = (-b + cmath.sqrt(mm)) / (2 * a)
        x2 = (-b - cmath.sqrt(mm)) / (2 * a)
        print("{:.0f}x**2+{:.0f}x+{:.0f}的结果为：x={:.0f} 和 x={:.0f}".format(a, b, c, x1, x2))
    else:
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
    if is_number(xx):
        return xx
    else:
        while not is_number(xx):
            print('不是数字，请再次输入')
            cc = input("请输入第一个数:")
            if is_number(cc):
                break
        return print('此程序用于计算一元二次方程解,请依次输入三个数')


zz = input("是否要开始计算:yes/no——:")
while zz == 'yes':
    a = float(panduan(input("请输入第一个数:")))
    b = float(panduan(input("请输入第二个数:")))
    c = float(panduan(input("请输入第三个数:")))
    mx(a, b, c)
    zz = input("是否还要继续计算:yes/no——:")
print('感谢使用。', end="")
