# https://www.runoob.com/python3/python3-check-is-number.html

def is_number(str):
    try:
        float(str)
        return True
    except ValueError: # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass

    try:
        import unicodedata # 处理ASCii码的包
        unicodedata.numeric(str)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass

    return False

str = input("请输入数字或字符串")
print("结果是：{0}".format(is_number(str)))

