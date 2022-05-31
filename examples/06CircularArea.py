# https://www.runoob.com/python3/python3-area-of-a-circle.html

def findArea(r):
    PI = 3.142
    return PI * (r*r)

print("面积为 %.6f" %findArea(6))


# 引入math

import math

pi = math.pi

def area_circle():

    r = input('请输入圆的半径:')
    
    while r.isdigit() == False or float(r) <= 0:
         print("请输入大于 0 的数字！")
         r = input('请输入圆的半径:')
        
    else:
        r = float(r)
        area = r * r * pi
        print ('圆的面积为 %d' %area)

area_circle()

