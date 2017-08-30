import os
import sys
import requests
import ast

url = "https://api.seniverse.com/v3/weather/now.json" #知心天气API
UserInput = input('请输入所要查询的天气>>> ')

SeachLog = {}
his1 = []
def SearchWeather(UserInput):
    try:
        while True:
            paramsdict ={'key': 'lom0ftfaihx65jh0','location':UserInput ,'language': 'zh-Hans','unit': 'c'}
            req = requests.get(url,params=paramsdict,timeout =1)
            m= req.json()#知心天气接口返回值为str，需要转为dict
            weather =m['results'][0]['now']['text']
            wind =m['results'][0]['now']['wind_direction']#风向
            temperature =m['results'][0]['now']['temperature']#温度
            lasttime =m['results'][0]['last_update']#更新时间
            SeachLog[UserInput] = weather
            #下面一行是将拼接字符串
            weather_str =f'{UserInput}的天气为{weather},风向为{wind},温度为{temperature}摄氏度,更新时间为:{lasttime}'
            print(weather_str)
            his1.append(weather_str)
            UserInput = input('请输入城市名称>> ')
    except KeyError: # keyerror抓取

        if UserInput in ('help','h'):
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
        elif UserInput == 'history':
            caculater = 0
            for historyLine in his1:
                caculater = caculater + 1
                print('第%d次查询:'%caculater)
                print(historyLine)
            UserInput = input('请重新输入城市名称>> ')
            SearchWeather(UserInput)
        else:
            print("该城市目前没有被收录")
            UserInput = input('请重新输入城市名称>> ')
            SearchWeather(UserInput)

#SearchWeather(UserInput)

if __name__ == "__main__":
    SearchWeather(UserInput)
    print("test11 %s" %__name__)

else:
    print("test22 %s" %__name__)
