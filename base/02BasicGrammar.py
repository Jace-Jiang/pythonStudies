# Page in https://www.runoob.com/python3/python3-basic-syntax.html

# 第一个注释
from ast import keyword


print("Hello Python!") # 第一个注释

import keyword
keyword.kwlist


# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
print ("Hello, Python!")


'''
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
'''
if True:
    print ("True")
else:
    print ("False")


print('------------行与缩进-------------')
item_one="sss";item_two="1";item_three="2";
total = item_one + \
        item_two + \
        item_three
print("字符串拼接：" + total)

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

num1=12;num2=13;num3=14;
sum = num1+num2+num3
# 打印的类型
print(sum)
print('------------行与缩进-------------')



print('------------字符串(String)-------------')
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('------------字符串(String)-------------')



print('------------等待用户输入-------------')
# input("\n\n按下 enter 键后退出。")
print('------------等待用户输入-------------')

print('------------同一行显示多条语句-------------')
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
print('------------同一行显示多条语句-------------')


print('------------print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：-------------')
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
print('------------print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：-------------')


help(max)
help("print")


print('==========打印dict类的使用==========')
def getPairs(dict):
    for k,v in dict.items():
        print(k,v,sep=':')

print('==========当字符串内容为浮点型要转换为整型时，无法直接用 int() 转换：==========')
a='2.1' # 这是一个字符串
#print(int(a))
print(int(float(a)))

