'''
天气查询文档专用
'''
__version__ = "V17.8.16.2102"
__author__ = "hu.wu"
__lisence__ = "MIT@2017-05"



import os
import sys

dic ={}
with open ("weather_info.txt","r",encoding = 'utf-8') as NewWeather:


#    for i in range(2554):  #for循环必须在with open函数底下=，否则会报错，大概是文件没有关闭

        NewWeather1 = NewWeather.read.strip('\n').split(',')
        dic[NewWeather1[0]] = NewWeather1[1]
        NewWeather2 =[]



UserInput = input('请输入城市名称>> ')
SeachLog = {}
def SearchWeather(UserInput):
    while UserInput in dic.keys():
        print(dic[UserInput])
        SeachLog[UserInput] = dic[UserInput]
        UserInput = input('请输入城市名称>> ')
    if UserInput == 'help':
        print('''
        输入城市名称，查询该城市的的天气
        输入help，获取帮助文档
        输入history，获取查询历史
        输入quit，退出天气查询系统
        ''')
        UserInput = input('请输入城市名称>> ')
        SearchWeather(UserInput)
    elif UserInput == 'quit':

    	os._exit(1)
    elif UserInput =='history':
        for LogKey in SeachLog:
            #print(LogKey)
            #print(SeachLog[LogKey])
            print('{}的天气为：{}'.format(LogKey,SeachLog[LogKey]))

        UserInput = input('请重新输入城市名称>> ')
        SearchWeather(UserInput)

    else:
        print("该城市目前没有被收录")
        UserInput = input('请重新输入城市名称>> ')
        SearchWeather(UserInput)
    return
SearchWeather(UserInput)
