# 1、对字符串"Welcome To The Python World"进行如下操作：
# （1）输出"welcome to the python world"
# （2）输出 ['welcome', 'to', 'the', 'python', 'world']
# （3）在（1）的基础上，把字符串中的o全部替换成a
# （4）在（1）的基础上，把字符串中的第一个o替换成a
# （5）在（1）的基础上，把字符串中的空格全部去掉，变成"welcometothepythonworld"
# 2、对列表num_list = [1, 5, 8, 1, 3, 12]进行如下操作：
# （1）在num_list后面追加一个数字100（变成[1, 5, 8, 1, 3, 12, 100]）
# （2）在（1）的基础上，在后面追加一个列表[1, 2, 3, 4, 5]（变成[1, 5, 8, 1, 3, 12, 100, 1, 2, 3, 4, 5]）
# （3）在（2）的基础上，对列表进行反向排序（变成[100, 12, 8, 5, 5, 4, 3, 3, 2, 1, 1, 1]）
# （4）在（3）的基础上，把数字4从列表中去除（变成[100, 12, 8, 5, 5, 3, 3, 2, 1, 1, 1]）
# 3、有一个字典info = {'name': 'xiaoli', 'age': 18, 'height': 170}，进行如下操作：
# （1）输出info中所有的key（即['name', 'age', 'height']）
# （2）输出info中所有的value（即['xiaoli', 18, 170]）
# （3）输出info中所有的key-value对（即[('name', 'xiaoli'), ('age', 18), ('height', 170)]）
# （4）把age这一项从info中去掉（即 {'name': 'xiaoli', 'height': 170}）

str1 = 'Welcome To The Python World'
str1_1 = str1.lower()
print(str1_1)
print(str1.split(' '))
print(str1_1.replace('o', 'a'))
print(str1_1.replace('o', 'a', 1))
print(str1_1.replace(' ', ''))


num_list = [1, 5, 8, 1, 3, 12]
num_list.append(100)
print(num_list)
num_list_new = [1, 2, 3, 4, 5]
num_list_new2 = num_list + num_list_new
print(num_list_new2)
num_list_new2.sort(reverse=True)
print(num_list_new2)
num_list_new2.remove(4)
print(num_list_new2)

info = {'name': 'xiaoli', 'age': 18, 'height': 170}
key_list = info.keys()
print(key_list)
value_lsit = info.values()
print(value_lsit)
item_list = info.items()
print(item_list)
del info['age']
print(info)


