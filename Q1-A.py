# 1、把一个字符串转成一个列表，然后再把这个列表转成字符串
# "abcdefg" -> ['a', 'b', 'c', 'd', 'e', 'f', 'g'] -> "abcdefg"
# 2、有一个列表my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，在这个列表的基础上生成如下列表：
# [3, 4, 5, 6, 7, 8]
# [1, 4, 7, 10]
# [10, 8, 6, 4, 2]
# 3、有一个字典info = {"name": "xiaoming", "age": 18}，把它变成如下的列表：
# [('name', 'xiaoming'), ('age', 18)]

str = 'abcdefg'
list1 = list(str)
print(list1)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[2:-2])
print(my_list[::2])
print(my_list[::-2])

info = {"name": "xiaoming", "age": 18}
lst = []
for key, value in info.items():
    lst.append((key, value))
print(lst)
