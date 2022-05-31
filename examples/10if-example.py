# https://www.runoob.com/python3/python3-if-example.html

num = float(input("请输入一个数字："))
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

# 内嵌方式判断
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")
