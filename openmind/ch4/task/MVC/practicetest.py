'''
天气查询程序
'''

import os
import sys
import requests
import ast

url = "https://api.seniverse.com/v3/weather/now.json" #知心天气API

def SearchWeather(UserInput):

    try:
        paramsdict ={'key': 'lom0ftfaihx65jh0','location':UserInput ,'language': 'zh-Hans','unit': 'c'}
        req = requests.get(url,params=paramsdict,timeout =5)
        m= req.json()#知心天气接口返回值为str，需要转为dict
        weather =m['results'][0]['now']['text']
        wind =m['results'][0]['now']['wind_direction']#风向
        temperature =m['results'][0]['now']['temperature']#温度
        lasttime =m['results'][0]['last_update']#更新时间
        weather_str =f'{UserInput}的天气为{weather},风向为{wind},温度为{temperature}摄氏度,更新时间为:{lasttime}'
        return weather_str

    except KeyError:
        return "该城市目前没有被收录,请重新输入"
    

if __name__ == "__main__":
    UserInput = input('请输入所要查询的天气>>> ')
    SearchWeather(UserInput)
