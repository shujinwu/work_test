"""
1、有一个文件列表file_list = ["chuman.png", "wechat.exe", "qq.dmg", "a.pngbcd.png", "mumu.exe", "dingding.jpg", "a.png" ]
（1）从中取出所有png文件，组成新的列表png_list
（2）去掉png_list中包含字母'u'的文件
2、生成一个包含1到100的数字列表num_list = [1, 2, ..., 100]，计算列表中所有偶数的和
3、sum = 1 + 2 + 3 + ... + n，输出当sum第一次大于100时，对应的sum和n的值
4、有一个服装店资源字典resource_dict = {"status":"ok","data":{"list":[{"id":"15243","title":"Q版音茵百褶","has_buy":1,"price_type":2},{"id":"14990","title":"Q版粉兔小睡衣","has_buy":0,"price_type":1},{"id":"15046","title":"Q版木烟风","has_buy":0,"price_type":1},{"id":"15037","title":"Q版神森儿","has_buy":0,"price_type":2},{"id":"15025","title":"Q版赤阴阳和服","has_buy":0,"price_type":1},{"id":"14769","title":"鬼狱链服","has_buy":1,"price_type":1},{"id":"14552","title":"Q版藤兰校服-男","has_buy":0,"price_type":2}],"act_id":""}}
（1）打印所有已购买资源的id（has_buy字段的值为1）
（2）打印所有价格类型为金币的资源id（price_type字段的值为2）
"""

file_list = ["chuman.png", "wechat.exe", "qq.dmg", "a.pngbcd.png", "mumu.exe", "dingding.jpg", "a.png"]
png_list = []
for i in file_list:
    if i.endswith('.png'):
        png_list.append(i)
print(png_list)

png_list_withoutu = []
for s in png_list:
    if s.find('u') == -1:
        png_list_withoutu.append(s)
print(png_list_withoutu)

num_list = list(range(1, 101))
total = 0
for num in num_list:
    if num % 2 == 0:
        total = total + num
print(total)

n = 1
sum = 0
while n > 0:
    sum = sum + n
    if sum > 100:
        print(sum, n)
        break
    n = n + 1


resource_dict = {"status":"ok","data":{"list":[{"id":"15243","title":"Q版音茵百褶","has_buy":1,"price_type":2},{"id":"14990","title":"Q版粉兔小睡衣","has_buy":0,"price_type":1},{"id":"15046","title":"Q版木烟风","has_buy":0,"price_type":1},{"id":"15037","title":"Q版神森儿","has_buy":0,"price_type":2},{"id":"15025","title":"Q版赤阴阳和服","has_buy":0,"price_type":1},{"id":"14769","title":"鬼狱链服","has_buy":1,"price_type":1},{"id":"14552","title":"Q版藤兰校服-男","has_buy":0,"price_type":2}],"act_id":""}}
print(resource_dict['data']['list'])
has_buy_id = []
coins_id = []
for item in resource_dict['data']['list']:
    if item['has_buy'] == 1:
        has_buy_id.append(item['id'])

for ite in resource_dict['data']['list']:
    if ite['price_type'] == 2:
        coins_id.append(ite['id'])

print(has_buy_id, coins_id)