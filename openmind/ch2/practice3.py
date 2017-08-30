'''
Weather Seach
'''
__version__ = "V17.8.16.2102"
__author__ = "hu.wu"
__lisence__ = "MIT@2017-05"

import os
import sys
import requests
import ast

url = "https://api.seniverse.com/v3/weather/now.json"
UserInput = input('请输入所要查询的天气>>> ')

SeachLog = {}
def SearchWeather(UserInput):
    while True:
        paramsdict ={'key': 'lom0ftfaihx65jh0','location':UserInput ,'language': 'zh-Hans','unit': 'c'} 
        req = requests.get(url,params=paramsdict,timeout =1)
        m = ast.literal_eval(req.text)
        print('%s的天气为%s' %(UserInput,m['results'][0]['now']['text'])) 
        print('风向为%s,温度为%s摄氏度'%(m['results'][0]['now']['wind_direction'],m['results'][0]['now']['temperature']))
        print('更新时间为:%s' %m['results'][0]['last_update'])
        SeachLog[UserInput] = m['results'][0]['now']['text']
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
         
            print('{}的天气为：{}'.format(LogKey,SeachLog[LogKey]))
            
        UserInput = input('请重新输入城市名称>> ')
        SearchWeather(UserInput)
                
    else:
        print("该城市目前没有被收录")
        UserInput = input('请重新输入城市名称>> ')
        SearchWeather(UserInput)
            
SearchWeather(UserInput)

