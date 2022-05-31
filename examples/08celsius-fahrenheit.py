# https://www.runoob.com/python3/python3-celsius-fahrenheit.html

celsius = float(input('请输入摄制温度：'))

fahrenheit = (celsius * 1.8) + 32
# 为什么这里没有标明是第几个参数照样可以在占位符写入值，如03Sqrt.py中提到 {1:0.3f}
print("%0.1f 摄氏温度转为华氏温度为 %0.1f" %(celsius,fahrenheit))


# 摄氏度和华氏度相互转换
a = int(input('摄氏度转换为华氏温度请按1\n华氏温度转化为摄氏度请按2\n'))
while a != 1 and a != 2:
    a = int(input('你选择不正确，请重新输入。\n摄氏度转换为华氏温度请按1\n华氏温度转换为摄氏度请按2\n'))
if a == 1:
    celsius = float(input('输入摄氏度:'))
    fahrenheit = (celsius*1.8)+32 #计算华氏温度
    print('%.1f摄氏度转为华氏温度为%.1f' %(celsius,fahrenheit))
else:
    fahrenheit = float(input('输入华氏度:'))
    celsius = (fahrenheit - 32)/1.8 #计算摄氏度
    print('%.1f华氏度转为摄氏度为%.1f' %(fahrenheit,celsius))