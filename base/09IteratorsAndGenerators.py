# https://www.runoob.com/python3/python3-iterator-generator.html

print("===============1、迭代器==================")
list = [1,2,3,4]
it = iter(list) # 创建迭代器对象
print(next(it))
print(next(it))

list2 = [1,2,3,4]
it = iter(list2)
for x in it:
    print(x,end=" ")  # print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。


from re import A
import sys
list3 = [1,2,3,4]
it = iter(list3)
while True:
    try:
        print (next(it))
    except StopIteration:
        sys:exit()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x= self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = MyNumbers()
myiter = iter(myClass)
for x in myiter:
    print(x)


print("===============2、生成器==================")

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
            return
        yield a
        a,b = a, a+b
        counter += 1
f = fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()



