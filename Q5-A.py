"""
1、给定n=10，计算1! + 2! + 3! + ... + n!的值
# 2、给一个数字字符串13543897565，把每一位对应的数字转换成英文数字（例如：“123” -> "one-two-three"）
# 3、我的关注列表follow_list = {"status":"ok","data":{"follow_list":[{"user_id":"32804516","nickname":"羽秋璃1111233","is_friend":0,"is_vip":1},{"user_id":"35742446","nickname":"我是你的宝贝哦","is_friend":1,"is_vip":1},{"user_id":"264844","nickname":"大鱼噢大鱼","is_friend":0,"is_vip":1},{"user_id":"34362681","nickname":"薛一十三","is_friend":0,"is_vip":0}]}}
# （1）如果用户是vip，对用户说“土豪xxx，我关注了你，给个打赏吧”(xxx是用户昵称)
# （2）如果用户不是好友关系但是vip（is_friend=0, is_vip=1），对用户说“土豪xxx，我关注了你，给个好友位吧”
"""

# noinspection PyUnresolvedReferences
import math


n = 1
sum = 0
while n <= 10:
    sum = sum + math.factorial(n)
    n = n + 1
print(sum)

str = '13543897565'
str_list = []
num_str = {
    "0": "zero",
    "1": 'one',
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "sevev",
    '8': "eight",
    "9": "nine"
}
for num in str:
    value = num_str[num]
    str_list.append(value)
new_str = '-'.join(str_list)
print(new_str)

follow_list = {"status":"ok","data":{"follow_list":[{"user_id":"32804516","nickname":"羽秋璃1111233","is_friend":0,"is_vip":1},{"user_id":"35742446","nickname":"我是你的宝贝哦","is_friend":1,"is_vip":1},{"user_id":"264844","nickname":"大鱼噢大鱼","is_friend":0,"is_vip":1},{"user_id":"34362681","nickname":"薛一十三","is_friend":0,"is_vip":0}]}}
print(follow_list['data']['follow_list'])
for item in follow_list['data']['follow_list']:
    if item['is_vip'] == 1:
        print("土豪%s，我关注了你，给个打赏吧" % (item['nickname']))

for item in follow_list['data']['follow_list']:
    if item['is_vip'] == 1 and item['is_friend'] == 0:
        print("土豪%s，我关注了你，给个好友位吧" % (item['nickname']))
