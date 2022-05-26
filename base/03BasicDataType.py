# https://www.runoob.com/python3/python3-data-type.html

print('============0、python3基本数据类型================')
counter = 1000  #整型变量
miles = 1000.0  #浮点型变量
name = "runoob" #字符串
print(counter)
print(miles)
print(name)

'''
六种标准数据类型：(不可变数据&可变数据)
Number(数字)
String(字符串)
List(列表)
Tuple(元组)
Set(集合)
Dictionary(字典)
'''

print('============1、Number（数字）================')
a, b, c, d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
print(isinstance(a,int))


print('============2、string（字符串）================')
str = 'Runoob'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串
print('Ru\noob')
print(r'Ru\noob')


print('============3、list（列表）================')
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


print('============4、Tuple（元组）================')
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组


print('============5、Set（集合）================')
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素


print('============6、Dictionary（字典）================')
dict = {}
dict['one'] = "1-人生巅峰"
dict[2] = "2-财务自由"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值


# 笔记
print('============6、笔记================')
class father(object):
    pass
class son(father):
    pass
if __name__=='__main__':
    print(type(son())==father)
    print(isinstance(son(),father))
    print(type(son()))
    print(type(son))


#coding=utf8  
''''' 
复数是由一个实数和一个虚数组合构成，表示为：x+yj 
一个负数时一对有序浮点数(x,y)，其中x是实数部分，y是虚数部分。 
Python语言中有关负数的概念： 
1、虚数不能单独存在，它们总是和一个值为0.0的实数部分一起构成一个复数 
2、复数由实数部分和虚数部分构成 
3、表示虚数的语法：real+imagej 
4、实数部分和虚数部分都是浮点数 
5、虚数部分必须有后缀j或J 
 
复数的内建属性： 
复数对象拥有数据属性，分别为该复数的实部和虚部。 
复数还拥有conjugate方法，调用它可以返回该复数的共轭复数对象。 
复数属性：real(复数的实部)、imag(复数的虚部)、conjugate()（返回复数的共轭复数） 
'''  
class Complex(object):  
    '''''创建一个静态属性用来记录类版本号'''  
    version=1.0  
    '''''创建个复数类，用于操作和初始化复数'''  
    def __init__(self,rel=15,img=15j):  
        self.realPart=rel  
        self.imagPart=img  
         
    #创建复数  
    def creatComplex(self):  
        return self.realPart+self.imagPart  
    #获取输入数字部分的虚部  
    def getImg(self):  
        #把虚部转换成字符串  
        img=str(self.imagPart)  
        #对字符串进行切片操作获取数字部分  
        img=img[:-1]   
        return float(img)    
                         
def test():  
    print ("run test...........") 
    com=Complex() 
    Cplex= com.creatComplex()  
    if Cplex.imag==com.getImg():  
        print #com.getImg() 
    else:  
        pass  
    if Cplex.real==com.realPart:  
        print #com.realPart 
    else:  
        pass  
    #原复数  
    print ("the religion complex is :"),Cplex  
    #求取共轭复数  
    print ("the conjugate complex is :"),Cplex.conjugate()  
      
if __name__=="__main__":  
    test()


