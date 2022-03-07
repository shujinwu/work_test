"""
1、有一个数列2/1，3/2，5/3，8/5，13/8，21/13...，求这个数列的前20项之和
2、定义一个函数create_verification_code，接收2个参数length、num，随机生成num个长度为length的数字、字母混合验证码，且生成的验证码不能重复，例如：create_verification_code(3, 4) -> ('a13', 'b7f', '7rr', '84s')
3、编写一个猜数字小游戏，运行的时候随机产生一个答案（1-100之间），效果如下：
请输入你猜测的数字：（1-100之间）
38
你猜的答案偏小，请输入你的答案: （38-100之间）
68
你猜的答案偏大，请输入你的答案: （38-68之间）
53
你猜的答案偏大，请输入你的答案: （38-53之间）
46
回答正确，正确答案就是46，你一共猜了4次
"""

# noinspection PyUnresolvedReferences
import string
# noinspection PyUnresolvedReferences
import random

def create_verification_code(length, num):
    cod_list = []
    str_list = string.ascii_letters + string.digits
    for i in range(0, num):
        code = ''.join(random.sample(str_list, length))
        if code in cod_list:
            pass
        else:
            cod_list.append(code)
    return cod_list


def digital_bomb():
    x = random.randint(1, 100)
    i = 1
    c = 1
    d = 100
    while i < 100:
        y = int(input("输入一个数字：(%d，%d之间)" % (c, d)))
        if y > 100:
            print("输入的数字超过100，重新输入")
        elif y > x:
            d = y
            print("猜的答案偏大，输入你的答案（%d, %d）" % (c, d))
            i = i + 1
        elif y < x:
            c = y
            print("猜的答案偏大，输入你的答案（%d, %d）" % (c, d))
            i = i + 1
        elif y == x:
            print("回答正确，答案就是%d，一共猜了%d次" % (x, i))
            break


def sum():
    x = 1
    y = 2
    sum = 0
    for i in range(20):
        sum = sum + y / x
        x = y
        y = x + y
    return sum

print(sum())
print(create_verification_code(5, 5))
digital_bomb()
