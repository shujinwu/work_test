# 1、输出字符串“dgfjkk”的长度
# 2、把字符串"Good good study! Day Day up"里的大写转小写，小写转大写
# 3、把字符串" you are here "中的空格去除
# 4、判断字符串"Good good study! Day Day up"是否以"Good"
# 5、统计字符串"dsh34kjh8sdfjk327jksdf034kl"中数字的个数

str1 = "dgfjkk"
print(len(str1))

str2 = "Good good study! Day Day up"
str2_1 = str2.swapcase()
print(str2_1)

str3 = " you are here "
# str3_1 = str3.strip()
str3_1 = str3.replace(' ', '')
print(str3_1)

str4 = 'Good good study! Day Day up'
print(str4.startswith('Good'))

str5 = 'dsh34kjh8sdfjk327jksdf034kl'
total = 0
for i in str5:
    if i.isdigit():
        total = total + 1

print(total)