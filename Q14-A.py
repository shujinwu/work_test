"""
1、定义一个函数，接收一个整数列表和一个和值sum，在这个列表中找出和为sum的两个整数，返回这两个整数的下标（注：列表中同一个元素不能使用两遍）
例如：nums = [1, 3, 6, 8] sum = 9 -> [0, 3]
2、定义一个函数，接收两个参数file_path和content，把指定内容写入到指定路径的文件中（如果文件存在，则以追加形式写入）
例如：file_path = 'demo/abc.txt' content = '今天天气好晴朗aa'，在当前路径的demo目录下的abc.txt文件中写入内容：今天天气好晴朗aa
3、熟悉json模块，把字典user_info = {'username': '一级棒','password': '333'}写入文件中，再从文件中读取内容并打印出来。
文件的内容和打印的内容格式如下：
{
    "username": "一级棒",
    "password": "333"
}
"""
import os
import json


def sum_list(num_list, sum):
    substrip_list = []
    lenth = len(num_list)
    for i in range(lenth):
        for j in range(lenth):
            if num_list[i] + num_list[j] == sum and i != j:
                substrip_list.append(i)
                substrip_list.append(j)
                return substrip_list


def write_info(path, content):
    if os.path.exists(path):
        pass
    elif not os.path.exists(path):
        file = open(path, 'w+')
        file.close()
    with open(path, 'a') as file:
        file.write(content)


def json_write():
    info = {'username': '一级棒', 'password': '333'}
    file = open('./user.json', 'w')
    json.dump(info, file, ensure_ascii=False)
    file.close()
    with open('./user.json', 'r') as fl:
        res = json.load(fl)
    return res

print(sum_list([1, 2, 3], 3))
# print(json_write())
# write_info('./abc.txt', '今天天气好晴朗aa')
