import os
import sys
import requests
import ast
import time

url = "https://api.seniverse.com/v3/weather/now.json"
#UserInput = input('请输入所要查询的天气>>> ')

#SeachLog = {}
#def SearchWeather(UserInput):
#    try:
#while True:
paramsdict ={'key': 'lom0ftfaihx65jh0','location':'北京' ,'language': 'zh-Hans','unit': 'c'} 
req = requests.get(url,params=paramsdict,timeout =1)
#    m = ast.literal_eval(req.text)
m= req.json()
print(m)
weather =m['results'][0]['now']['text']
wind =m['results'][0]['now']['wind_direction']
temperature =m['results'][0]['now']['temperature']
lasttime =m['results'][0]['last_update']

print('北京的天气为%s' %weather) 
print('风向为%s,温度为%s摄氏度'%(wind,temperature))
print('更新时间为:%s' %lasttime)
#    time.sleep(3)#每隔3秒刷新一次
            
