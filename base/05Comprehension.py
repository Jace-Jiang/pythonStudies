#https://www.runoob.com/python3/python-comprehensions.html

print("===============1、列表推导式==================")
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

print("===============2、字典推导式==================")
listdemo = ['Google','Runoob', 'Taobao']
 #将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)
dic = {x: x**2 for x in (2,4,6)}
print(dic)
print(type(dic))

print("===============3、集合推导式==================")
setnew = {i**2 for i in (1,2,3)}
print(setnew)
a = {x for x in 'sdfsdaweeegbbacssdccsaxddfwehx' if x not in 'abc'}
print(a)
print(type(a))

print("===============4、元组推导式==================")
a = (x for x in range(1,10))
# 返回的是生成器对象
print(a)
# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a))





