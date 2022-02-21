"""
1、word = "1g21gf232123ijh3987dh498fnt49dj47f8"，统计word中各个数字出现的次数
2、num = 567，判断num是不是质数（质数：大于1的自然数中除了能被1和本身整除之外，不能被其他的数整除的数）
3、user_list = {"list":[{"nickname":"茶香谜语","club_info":{"club_id":4,"club_name":"一起玩"}},{"nickname":"风信子","club_info":{}},{"nickname":"西风","club_info":{}},{"nickname":"可爱美丽","club_info":{"club_id":8,"club_name":"西风和"}}]}
（1）输出没有加入社团的用户的昵称
（2）对于没有加入社团的用户，随机生成社团信息，要求是club_id在100以内且不能和已存在的club_id重复，club_name和用户的昵称一致，最后打印user_list
# 随机生成club_id (利用random)
# club_id 在100以内
# club_Id不能存在的重复
"""

# word = "1g21gf232123ijh3987dh498fnt49dj47f8"
# word_info_count = {}
# for num in word:
#     word.count(num)
#     word_info_count[num] = word.count(num)
# print(word_info_count)

# num = 567
# num_list = list(range(2, 567))
# for i in num_list:
#     if num % i != 0:
#         pass
#     else:
#         break
#         print("num不是质数" )
# print("num是质数")

user_list = {"list":[{"nickname":"茶香谜语","club_info":{"club_id":4,"club_name":"一起玩"}},{"nickname":"风信子","club_info":{}},{"nickname":"西风","club_info":{}},{"nickname":"可爱美丽","club_info":{"club_id":8,"club_name":"西风和"}}]}
print(user_list["list"])
no_club_user = []
for item in user_list["list"]:
    if item["club_info"] == { }:
        no_club_user.append(item["nickname"])
print(no_club_user)

