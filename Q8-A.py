"""
1、定义一个函数print_days()，接收2个参数year和month，其中year是年份，month是月份，输出year年month月的天数
2、定义一个函数remove_duplicate_digit_and_letter()，接收一个字符串word，去除掉字符串中重复的数字和字母，非字母和数字的字符即保留，例如 "1211abccd&&e8fe$$g" -> "12abcd&&e8f$$g"
3、定义一个排序函数sort_num()，接收2个参数num_list和reverse，其中num_list是一个数字列表，reverse代表排序规则，默认是从小到大排序，reverse为True是从大到小排序，返回排好序的数字列表（注：不能使用内置的排序函数）
"""

def print_days(year, month):
    month_days_31 = [1, 3, 5, 7, 8, 10, 12]
    month_days_30 = [4, 6, 9, 11]
    if month in month_days_31:
        return "%d年%d月有31天" % (year, month)
    elif month in month_days_30:
        return "%d年%d月有30天" % (year, month)
    elif year % 4 == 0 or year % 400 == 0:
        return "%d年2月有29天" % year
    else:
        return "%d年2月有28天" % year

def remove_duplicate_digit_and_letter(word):
    word = str(word)
    word_info = {}
    word_list = []
    for ste in word:
        word_info[ste] = word.count(ste)
    for info in word:
        if info.isalnum() == False:
            word_list.append(info)
        elif word_info[info] == 1 and info.isalnum() == True:
            word_list.append(info)
        elif word_info[info] != 1 and info.isalnum() == True  and info not in word_list:
            word_list.append(info)
        else:
            pass
    return "".join(word_list)


def sort_num(num_list, reverse):
    # 传了排序参数的情况下从大到小
    if reverse == True:
        for t in range(len(num_list) - 1):
            for n in range(len(num_list) - 1 - t):
                if num_list[n] < num_list[n+1]:
                    num_list[n], num_list[n + 1] = num_list[n + 1], num_list[n]
        return num_list

    # 默认从小到大排序
    elif reverse != True or reverse == "":
        for t in range(len(num_list) - 1):
            for n in range(0, len(num_list) - 1 - t):
                if num_list[n] > num_list[n+1]:
                    num_list[n], num_list[n + 1] = num_list[n + 1], num_list[n]
        return num_list



print(print_days(2008, 2))
print(remove_duplicate_digit_and_letter("msdajhgroapjjashfye7463#%$^&DFFSG90284fhdsjaSJFAsd"))
print(sort_num([4,9,8,0,3,5,2,1,6], ''))
