"""
1、定义一个函数，找出一个列表中第二大的数字
2、有一个环境配置的txt文件，内容如下所示，定义一个函数，接收env（环境）和key（需要获取项）这2个参数，或会对应环境对应项的内容
demo: {"api_url": "https://api-demo.chumanapp.com", "user_id": 1}
api2: {"api_url": "https://api-api2.chumanapp.com", "user_id": 2}
api: {"api_url": "https://api.chumanapp.com", "user_id": 3}
3、定义一个函数，这个函数的作用是返回某个目录下所有的文件名（包括子目录下的文件）
"""
import os

def second_max(num_list):
    lenth = len(num_list)
    for i in range(lenth - 1):
        for j in range(lenth - 1 - i):
            if num_list[j] < num_list[j + 1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list[1]

def read_config_file():
    path = './config.txt'
    new_list = []
    with open(path, 'r') as file:
        env_list = file.readlines()
        for line in env_list:
            line = line.strip('\n')
            new_list.append(line)
    return new_list


def get_env_key(env, key):
    env_list = read_config_file()
    print(env_list)
    for i in env_list:
        if i[:4] == 'demo' or i[:4] == 'api2':
            i = '{"' + i[:4] + '"' + i[4:] + '}'
        else:
            i = '{"' + i[:3] + '"' + i[3:] + '}'
        info = eval(i)
        if env in info.keys():
            return info.get(env).get(key)


def res_file(path):
    file_list = []
    file = os.listdir(path)
    # print(file)
    for f in file:
        # print(f)
        if os.path.isfile(f) == True:
            print(os.path.isfile(f))
            file_list.append(f)
        elif os.path.isdir(f):
            path = path + '/' + f
            res_file(path)

def count_file(path):
    file_name_list = []
    # path = '/Users/wushujin/Desktop/触漫'
    file_list = os.listdir(path)
    print(file_list)
    for f in file_list:
        if os.path.isfile(f) == True:
            file_name_list.append(f)
        elif os.path.isdir(f) == True:
            son_dir = path + '/' + f
            son_list = os.listdir(son_dir)
            file_name_list = file_name_list +son_list
    return  file_name_list


# count_file('/Users/wushujin/Desktop/触漫')
print(count_file('/Users/wushujin/Desktop/触漫'))


# print(second_max([9, 87,9078,635,0,223,645,876]))
# print(get_env_key('api', 'api_url'))