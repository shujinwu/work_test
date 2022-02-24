"""
1、定义一个函数，接收一个字符串，重新输出由字符串中的数字组成的一个最大的数字字符串（例如："15477239" -> "97754321"）
2、定义一个函数，接收一个参数（num >= 1000）,求100到num之间的水仙花数（水仙花数：如果这个数是m位数，则每个位上的数字的m次幂之和等于它本身）
3、定义一个函数记录学生信息，接收任意参数，但只记录name、age、height、weight、sex、address信息，address不传时，默认为广州市，对记录的信息进行打印。
如：
record_student_info(name='小王', sex='女')
record_student_info(name='小明', sex='男', address='北京市')
record_student_info(name='小陈', favorite='运动', height=170)
{'address': '广州市', 'name': '小王', 'sex': '女'}
{'address': '北京市', 'name': '小明', 'sex': '男'}
{'address': '广州市', 'name': '小陈', 'height': 170}
"""

import math

def reset_num(mess):
    mess = str(mess)
    num_list = []
    for i in mess:
        if i.isdigit() == True:
            num_list.append(i)
    for t in range(len(num_list) - 1):
        for s in range(len(num_list) - 1 - t):
            if num_list[s] < num_list[s+1]:
                num_list[s], num_list[s+1] = num_list[s+1], num_list[s]
    return ''.join(num_list)


def count_narcissistic_num(num):
    num_list = list(range(100, num))
    narcissistic_num = []
    total = 0
    for num in num_list:
        lenth = len(str(num))
        i = 1
        for s in range(lenth):
            i = i * 10
            total = total + math.pow(num % i, lenth)
            if total == num:
                narcissistic_num.append(num)
    return narcissistic_num


# print(reset_num("jdh864@$09.243,5+27"))
print(count_narcissistic_num(4056))