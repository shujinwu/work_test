"""
1、定义一个函数，接收2个参数num_list、num，其中num_list是一个已经排好序的数字列表，函数的作用是把num按照排序规律插入到num_list中并返回num_list，例如[1, 4 , 7, 8, 12], 5 -> [1, 4, 5, 7, 8, 12]（注：不要使用内置的排序方法）
2、定义一个函数custom_replace()，实现的是str.replace()的功能，例如custom_replace('good good study, good or bad', 'good', 'haha')，返回的是‘haha haha study, haha or bad’
3、定义一个函A数，接收一个正整数num，把这个正整数num分解质因数。例如：num=110，输出110=2*5*11
"""

def insert_and_sort(num_list, num):
    num_list.append(num)
    lenth = len(num_list)
    if num_list[0] > num_list[-2]:
        for i in range(lenth - 1):
            for j in range(lenth - 1 - i):
                if num_list[j] < num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    elif num_list[0] < num_list[-2]:
        for i in range(lenth - 1):
            for j in range(lenth - 1 - i):
                if num_list[j] > num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    elif num_list[0] == num_list[-2]:
        pass

    return num_list


def custom_replace(charater, old, new):
    charater = str(charater)
    if old not in charater:
        pass
    elif old in charater:
        times = charater.count(old)
        while times > 0:
            index = charater.find(old)
            charater = charater[:index] + new + charater[index + len(old):]
            times = times - 1
    return charater

def resolve_num(num):
    num_list = []
    final = num
    for i in range(2, final):
        if final % i == 0 and i not in num_list:
            num_list.append(i)
            final = final / i
    return num_list



# print(insert_and_sort([99,99,99,99,99,99,99],108))
# print(custom_replace('good good study, good or bad', 'good', 'haha'))
print(resolve_num(110))