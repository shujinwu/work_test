"""
1、有一个文件user.txt，里面记录的是用户的触漫号和手机号，把文件中的触漫号转换成用户id（截取触漫号第二位到末尾的字符串，16进制转10进制），并保存到新的文件中。
user.txt文件的内容如下：
42E7496A 13875884676
42E74968 15876483743
42E74967 15768465847
42E74966 14897434534
2、有一个列表[1,20,30,[1,44,[4,37,[15,24,33,[18,[22,12,45,[37,15]]]]]]]，用递归的思想打印出所有的值
3、定义一个函数，判断一个key是否在某个字典中（注：字典有可能是嵌套字典）
"""

def change_chumanid():
    with open('./user.txt', 'r') as file:
        obj_list = file.readlines()
        new_obj_list = []
        for i in obj_list:
            change_id = i[1:8]
            user_id = int(change_id, 16)
            new_info = str(user_id) + i[8:]
            new_obj_list.append(new_info)
    with open('./new_user.txt', 'w') as f:
        for info in new_obj_list:
            f.write(info)


def recursion_list(num_list):
    for i in num_list:
        if isinstance(i, int):
            print(i)
        elif isinstance(i, list):
            recursion_list(i)


def recursion_dic(dic_info, keys):
    for key, value in dic_info.items():
        if key == keys:
            print('%s在里面' % keys)
        elif isinstance(value, dict):
            recursion_dic(value, keys)
    # print('%s不在里面' % keys)


# change_chumanid()
# recursion([1,20,30,[1,44,[4,37,[15,24,33,[18,[22,12,45,[37,15]]]]]]])
recursion_dic({"data":{"user_id": 123456,"name": "大小哈哈哈","setting_info":{"name":"我是来搞笑的","sex":1,"age":18}}}, 'age')
# test_dic = {"data":{"user_id": 123456,"name": "大小哈哈哈","setting_info":{"name":"我是来搞笑的","sex":1,"age":18}}}