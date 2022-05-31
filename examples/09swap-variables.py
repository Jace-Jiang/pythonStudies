# https://www.runoob.com/python3/python3-swap-variables.html


x = input('输入x值：')
y = input('输入y值：')
temp = x
x = y
y = temp

# 不适用临时变量
# x,y = y,x

print('交换后的X值为：{}'.format(x))
print("交换后的Y值为：{}".format(y))
