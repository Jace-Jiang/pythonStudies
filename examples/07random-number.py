# https://www.runoob.com/python3/python3-random-number.html

'''
该程序会在字符终端 1~24 之间的位置随机打印出一个星号 * ，
并提示“请输入一个移动星号的指令(L/l or R/r)):”，如果用户输入 L 并回车，
星号就会向左移动一个字符的位置，并被重新输出；如果用户输入 R 并回车，
星号则会向右移动一个字符的位置，程序会循环提示用户输入，直至用户输入 “EXIT”，程序退出。
'''

import random
class computer(object):

    # __***__ 代表什么？
    # 魔法函数 https://www.zhihu.com/question/46973549/answer/1682758202
    def __init__(self):
        pass

    # 可复习函数这一章，命名空间和作用域（局部->全局->内置）
    g_num = 0
    def ger_num(start,end):
        return random.randint(start,end)

    def contrl(ctl_str):
        global g_num
        if ctl_str == '1' or ctl_str == 'L':
            g_num -= 1
            if g_num < 0 :
                g_num = 23
        elif ctl_str == 'r' or ctl_str == 'R':
            g_num += 1
            if g_num > 23:
                g_num = 0
        return g_num

    # staticmethod？ 返回函数的静态方法。https://www.runoob.com/python/python-func-staticmethod.html
    @staticmethod
    def print_space(space_num):
        print_content = ['-']*24
        print_content = ''.join(print_content)
        l_content = list(print_content)
        l_content[space_num] = '*'
        l_content = ''.join(l_content)
        print(l_content)

if __name__ == '__main__':
    g_num = computer.ger_num(0,24)
    computer.print_space(g_num)
    while True:
        ctrl_str = input("请输入移动星星的指令（L/l OR R/r）")
        if ctrl_str == 'EXIT' or ctrl_str == 'exit':
            break
        g_num = computer.contrl(ctrl_str)
        computer.print_space(g_num)
