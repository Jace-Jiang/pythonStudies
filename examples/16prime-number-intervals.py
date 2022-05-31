# https://www.runoob.com/python3/python3-prime-number-intervals.html

lower = int(input("请输入区间最小的值："))
upper = int(input("请输入区间最大的值："))

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
