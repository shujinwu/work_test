# 1、把一个字符串转成一个列表，然后再把这个列表转成字符串
# "abcdefg" -> ['a', 'b', 'c', 'd', 'e', 'f', 'g'] -> "abcdefg"
# 2、有一个列表my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，在这个列表的基础上生成如下列表：
# [3, 4, 5, 6, 7, 8]
# [1, 4, 7, 10]
# [10, 8, 6, 4, 2]
# 3、有一个字典info = {"name": "xiaoming", "age": 18}，把它变成如下的列表：
# [('name', 'xiaoming'), ('age', 18)]
#
#
# 1、输出字符串“dgfjkk”的长度
# 2、把字符串"Good good study! Day Day up"里的大写转小写，小写转大写
# 3、把字符串" you are here "中的空格去除
# 4、判断字符串"Good good study! Day Day up"是否以"Good"开头
# 5、统计字符串"dsh34kjh8sdfjk327jksdf034kl"中数字的个数
#
#
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
#
#
# 1、有一个文件列表file_list = ["chuman.png", "wechat.exe", "qq.dmg", "a.pngbcd.png", "mumu.exe", "dingding.jpg", "a.png" ]
# （1）从中取出所有png文件，组成新的列表png_list
# （2）去掉png_list中包含字母'u'的文件
# 2、生成一个包含1到100的数字列表num_list = [1, 2, ..., 100]，计算列表中所有偶数的和
# 3、sum = 1 + 2 + 3 + ... + n，输出当sum第一次大于100时，对应的sum和n的值
# 4、有一个服装店资源字典resource_dict = {"status":"ok","data":{"list":[{"id":"15243","title":"Q版音茵百褶","has_buy":1,"price_type":2},{"id":"14990","title":"Q版粉兔小睡衣","has_buy":0,"price_type":1},{"id":"15046","title":"Q版木烟风","has_buy":0,"price_type":1},{"id":"15037","title":"Q版神森儿","has_buy":0,"price_type":2},{"id":"15025","title":"Q版赤阴阳和服","has_buy":0,"price_type":1},{"id":"14769","title":"鬼狱链服","has_buy":1,"price_type":1},{"id":"14552","title":"Q版藤兰校服-男","has_buy":0,"price_type":2}],"act_id":""}}
# （1）打印所有已购买资源的id（has_buy字段的值为1）
# （2）打印所有价格类型为金币的资源id（price_type字段的值为2）
#
#
# 1、给定n=10，计算1! + 2! + 3! + ... + n!的值
# 2、给一个数字字符串13543897565，把每一位对应的数字转换成英文数字（例如：“123” -> "one-two-three"）
# 3、我的关注列表follow_list = {"status":"ok","data":{"follow_list":[{"user_id":"32804516","nickname":"羽秋璃1111233","is_friend":0,"is_vip":1},{"user_id":"35742446","nickname":"我是你的宝贝哦","is_friend":1,"is_vip":1},{"user_id":"264844","nickname":"大鱼噢大鱼","is_friend":0,"is_vip":1},{"user_id":"34362681","nickname":"薛一十三","is_friend":0,"is_vip":0}]}}
# （1）如果用户是vip，对用户说“土豪xxx，我关注了你，给个打赏吧”(xxx是用户昵称)
# （2）如果用户不是好友关系但是vip（is_friend=0, is_vip=1），对用户说“土豪xxx，我关注了你，给个好友位吧”
#
#
# 1、把数字123变成['1', '2', '3']，再变成'1,2,3'
# 2、dic = {'k1: 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
# (1)给dic添加一个键值对k5=v5
# (2)给dic添加一个字典{'k6': 'v6', 'k7': 'v7'}
# (3)从dic中获取'k4'对应的值
# (4)从dic中获取'k8'对应的值，不存在时不报错，返回None
# (5)从dic中删除'k1'这一项
# (6)从dic中删除'k10'这一项，不存在时不报错，返回None
# 3、fruits = ['apple', 'banana', 'orange', 'banana', '苹果']
# （1）'orange'在列表中的索引
# （2）列表中'banana'的数量
# （3）把'葡萄'追加到末尾
# （4）把['西瓜', '芒果']加到列表中
# （4）把'车厘子'插入到第1位
# （5）删除列表中第3个元素
# （6）对列表进行排序
# （7）对列表进行反转
#
# -----------------------------------
# 1、word = "1g21gf232123ijh3987dh498fnt49dj47f8"，统计word中各个数字出现的次数
# 2、num = 567，判断num是不是质数（质数：大于1的自然数中除了能被1和本身整除之外，不能被其他的数整除的数）
# 3、user_list = {"list":[{"nickname":"茶香谜语","club_info":{"club_id":4,"club_name":"一起玩"}},{"nickname":"风信子","club_info":{}},{"nickname":"西风","club_info":{}},{"nickname":"可爱美丽","club_info":{"club_id":8,"club_name":"西风和"}}]}
# （1）输出没有加入社团的用户的昵称
# （2）对于没有加入社团的用户，随机生成社团信息，要求是club_id在100以内且不能和已存在的club_id重复，club_name和用户的昵称一致，最后打印user_list
# # 随机生成club_id (利用random)
# # club_id 在100以内
# # club_Id不能存在的重复
#
#
# 1、定义一个函数print_days()，接收2个参数year和month，其中year是年份，month是月份，输出year年month月的天数
# 2、定义一个函数remove_duplicate_digit_and_letter()，接收一个字符串word，去除掉字符串中重复的数字和字母，非字母和数字的字符即保留，例如 "1211abccd&&e8fe$$g" -> "12abcd&&e8f$$g"
# 3、定义一个排序函数sort_num()，接收2个参数num_list和reverse，其中num_list是一个数字列表，reverse代表排序规则，默认是从小到大排序，reverse为True是从大到小排序，返回排好序的数字列表（注：不能使用内置的排序函数）
#
#
# 1、定义一个函数，接收一个字符串，重新输出由字符串中的数字组成的一个最大的数字字符串（例如："15477239" -> "97754321"）
# 2、定义一个函数，接收一个参数（num >= 1000）,求100到num之间的水仙花数（水仙花数：如果这个数是m位数，则每个位上的数字的m次幂之和等于它本身）
# 3、定义一个函数记录学生信息，接收任意参数，但只记录name、age、height、weight、sex、address信息，address不传时，默认为广州市，对记录的信息进行打印。
# 如：
# record_student_info(name='小王', sex='女')
# record_student_info(name='小明', sex='男', address='北京市')
# record_student_info(name='小陈', favorite='运动', height=170)
# {'address': '广州市', 'name': '小王', 'sex': '女'}
# {'address': '北京市', 'name': '小明', 'sex': '男'}
# {'address': '广州市', 'name': '小陈', 'height': 170}
#
#
# 1、有一个数列2/1，3/2，5/3，8/5，13/8，21/13...，求这个数列的前20项之和
# 2、定义一个函数create_verification_code，接收2个参数length、num，随机生成num个长度为length的数字、字母混合验证码，且生成的验证码不能重复，例如：create_verification_code(3, 4) -> ('a13', 'b7f', '7rr', '84s')
# 3、编写一个猜数字小游戏，运行的时候随机产生一个答案（1-100之间），效果如下：
# 请输入你猜测的数字：（1-100之间）
# 38
# 你猜的答案偏小，请输入你的答案: （38-100之间）
# 68
# 你猜的答案偏大，请输入你的答案: （38-68之间）
# 53
# 你猜的答案偏大，请输入你的答案: （38-53之间）
# 46
# 回答正确，正确答案就是46，你一共猜了4次
#
#
# 1、定义一个函数，接收2个参数num_list、num，其中num_list是一个已经排好序的数字列表，函数的作用是把num按照排序规律插入到num_list中并返回num_list，例如[1, 4 , 7, 8, 12], 5 -> [1, 4, 5, 7, 8, 12]（注：不要使用内置的排序方法）
# 2、定义一个函数custom_replace()，实现的是str.replace()的功能，例如custom_replace('good good study, good or bad', 'good', 'haha')，返回的是‘haha haha study, haha or bad’
# 3、定义一个函数，接收一个正整数num，把这个正整数num分解质因数。例如：num=110，输出110=2*5*11
#
#
# 1、有一个文件user.txt，里面记录的是用户的触漫号和手机号，把文件中的触漫号转换成用户id（截取触漫号第二位到末尾的字符串，16进制转10进制），并保存到新的文件中。
# user.txt文件的内容如下：
# 42E7496A 13875884676
# 42E74968 15876483743
# 42E74967 15768465847
# 42E74966 14897434534
# 2、有一个列表[1,20,30,[1,44,[4,37,[15,24,33,[18,[22,12,45,[37,15]]]]]]]，用递归的思想打印出所有的值
# 3、定义一个函数，判断一个key是否在某个字典中（注：字典有可能是嵌套字典）
#
#
# 1、定义一个函数，找出一个列表中第二大的数字
# 2、有一个环境配置的txt文件，内容如下所示，定义一个函数，接收env（环境）和key（需要获取项）这2个参数，或会对应环境对应项的内容
# demo: {"api_url": "https://api-demo.chumanapp.com", "user_id": 1}
# api2: {"api_url": "https://api-api2.chumanapp.com", "user_id": 2}
# api: {"api_url": "https://api.chumanapp.com", "user_id": 3}
# 3、定义一个函数，这个函数的作用是返回某个目录下所有的文件名（包括子目录下的文件）
#
#
#
# 1、定义一个函数，接收一个整数列表和一个和值sum，在这个列表中找出和为sum的两个整数，返回这两个整数的下标（注：列表中同一个元素不能使用两遍）
# 例如：nums = [1, 3, 6, 8] sum = 9 -> [0, 3]
# 2、定义一个函数，接收两个参数file_path和content，把指定内容写入到指定路径的文件中（如果文件存在，则以追加形式写入）
# 例如：file_path = 'demo/abc.txt' content = '今天天气好晴朗aa'，在当前路径的demo目录下的abc.txt文件中写入内容：今天天气好晴朗aa
# 3、熟悉json模块，把字典user_info = {'username': '一级棒','password': '333'}写入文件中，再从文件中读取内容并打印出来。
# 文件的内容和打印的内容格式如下：
# {
#     "username": "一级棒",
#     "password": "333"
# }
#
#
#
# 1、有2个字典如下，从中找出价格小于1000，并且颜色不是红色的所有产品名称和颜色的组合
# name_price = {"test1":876,"test2":1653,"test3":15,"test4":2876}
# name_color = {"test1":"yellow","test2":"blue","test3":"red","test4":"orange"}
# 2、定义一个People类
# （1）包含属性name、age、phone、address属性，为People类提供带有所有成员变量的构造器
# （2）提供2个方法：eat(food)、print_user_info()
# （3）调用eat(food)方法时，输出“name正在吃food”
# （4）调用print_user_info()方法时，输出一个包含当前用户的所有属性信息的字典
# 3、定义一个Student类，继承自People类
# （1）新增属性school、grade、class，其中school默认是“广州市第一中学”，不可修改，grade第一次赋值后也不可以修改，class属性可以修改，但对象不能通过属性赋值的方式直接进行修改
# （2）Student类调用print_user_info()方法时，需要新增的属性也打印出来
# 4、新建一个py文件（和People类、Student类不在同一个文件），在该文件中调用各实例化一个People类和Student类的对象，并调用这些对象可以调用的方法
# 5、安装第三方库requests，熟悉并发送以下请求
# （1）m=Api&c=User&a=token（获取某个用户的install_token）
# （2）m=Api&c=User&a=user_profile（通过获得的install_token查询用户信息）
# （3）m=Api&c=User&a=user_edit（在用户当前签名的后面加上4个随机数字）
#
#
# 1、git熟悉
# （1）github上注册一个账号，本地生成SSH-KEY，并添加与github账号绑定
# （2）github上新建一个项目，把项目拉到本地，新增一个READ.md文件，进行第一次提交，push到远程仓库
# （3）本地新建一个dev分支，随意新增文件或内容，进行至少2次提交，并push到远程仓库
# （4）把dev分支的内容合并到master分支，并push到远程仓库
# 2、熟悉python中的异常处理，回顾之前的猜数字小游戏，对用户的输入进行异常处理，输入不合法时给出提示，但不中断游戏过程
# 3、定义一个函数，调用触漫相关接口，完成一个创建社团的业务场景
# 4、定义一个函数，接收一个字符串参数，判断字符串中的字符是不是都是唯一的
# 5、定义一个函数，传入一个参数，判断传入的参数是否是一个合法的ip地址