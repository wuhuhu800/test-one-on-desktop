import os
import sys
import requests
import ast
import time

def C2F(c): # 温度转换函数 C 转F
    F = c * 1.8 +32
    return F




url = "https://api.seniverse.com/v3/weather/now.json"


while True:
    paramsdict ={'key': 'lom0ftfaihx65jh0','location':'北京' ,'language': 'zh-Hans','unit': 'c'}
    req = requests.get(url,params=paramsdict,timeout =1)
    m= req.json()
    weather =m['results'][0]['now']['text']
    wind =m['results'][0]['now']['wind_direction']
    temperature =m['results'][0]['now']['temperature']
    lasttime =m['results'][0]['last_update']
    Ftem = C2F(int(temperature))
    print('北京的天气为%s' %weather)
    print('风向为%s,温度为%s摄氏度,%.1f华氏度'%(wind,temperature,Ftem))

    print('更新时间为:%s' %lasttime)
    time.sleep(5)#每隔3秒刷新一次
