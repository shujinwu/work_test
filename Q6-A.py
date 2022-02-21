"""
1、把数字123变成['1', '2', '3']，再变成'1,2,3'
2、dic = {'k1: 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
(1)给dic添加一个键值对k5=v5
(2)给dic添加一个字典{'k6': 'v6', 'k7': 'v7'}
(3)从dic中获取'k4'对应的值
(4)从dic中获取'k8'对应的值，不存在时不报错，返回None
(5)从dic中删除'k1'这一项
(6)从dic中删除'k10'这一项，不存在时不报错，返回None
3、fruits = ['apple', 'banana', 'orange', 'banana', '苹果']
（1）'orange'在列表中的索引
（2）列表中'banana'的数量
（3）把'葡萄'追加到末尾
（4）把['西瓜', '芒果']加到列表中
（4）把'车厘子'插入到第1位
（5）删除列表中第3个元素
（6）对列表进行排序s
（7）对列表进行反转
"""

# str = "123"
# num_list = []
# for num in str:
#     num_list.append(num)
# new_str = ','.join(num_list)
# print(new_str)

# dic = {
#     'k1': 'v1',
#     'k2': 'v2',
#     'k3': 'v3',
#     'k4': 'v4'
# }
# dic['k5'] = 'v5'
# print(dic)
#
# add_dic = {
#     'k6': 'v6',
#     'k7': 'v7'
# }
# new_dic = {}
# new_dic.update(dic)
# new_dic.update(add_dic)
# print(new_dic)
#
# print(new_dic['k4'])
#
# for key in new_dic.keys():
#     if key == 'k8':
#         print(new_dic[key])
# print('None')
#
# del new_dic['k1']
# print(new_dic)
#
# for key in new_dic.keys():
#     if key == 'k10':
#         del new_dic[key]
# print('None')

fruits = ['apple', 'banana', 'orange', 'banana', '苹果']
print(fruits.index('orange'))
print(fruits.count('banana'))
fruits.append('葡萄')
print(fruits)
add_fruits = ['西瓜', '芒果']
fruits = fruits + add_fruits
print(fruits)
fruits.insert(1, '车厘子')
print(fruits)
del fruits[2]
print(fruits)
fruits.sort(reverse=True)
print(fruits)
sort_fruits = fruits[::-1]
print(sort_fruits)