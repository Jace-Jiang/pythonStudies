# https://www.runoob.com/python3/python3-add-number.html

num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')

# 为什么要加float？
# 因为使用内置函数input()来获取用户的输入，返回的是字符串，需要float转为数字
sum = float(num1) + float(num2)
# {*}为占位符，.format的作用？
print('数字{0}和{1}相加的结果为：{2}'.format(num1,num2,sum))


