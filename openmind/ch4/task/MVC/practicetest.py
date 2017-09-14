'''
天气查询程序
'''

import os
import sys
import requests
import ast

url1 = "https://api.seniverse.com/v3/weather/daily.json" #知心天气API可以查三天
#url2 = "https://api.seniverse.com/v3/weather/now.json"#可以查当天的

def SearchWeather(UserInput):

    try:
        paramsdict ={'key': 'lom0ftfaihx65jh0','location':UserInput ,'language': 'zh-Hans','unit': 'c'}
        req1 = requests.get(url1,params=paramsdict,timeout =5)
        m1= req1.json()#知心天气接口,有三天预报

        WeatherDailyDay = m1['results'][0]['daily'][0]['text_day']#当日白天天气
        WeatherDailyNight = m1['results'][0]['daily'][0]['text_night']#当日夜晚天气
        TemperatureDailyHigh = m1['results'][0]['daily'][0]['high']
        TemperatureDailylow = m1['results'][0]['daily'][0]['low']
        WindDirectionDaily = m1['results'][0]['daily'][0]['wind_direction']
        WindScaleDaily = m1['results'][0]['daily'][0]['wind_scale']#风级
        lasttime =m1['results'][0]['last_update']#更新时间
        weather_str =f'''{UserInput}的天气为：
          白天:{WeatherDailyDay}，夜间:{WeatherDailyNight}
          最高温度:{TemperatureDailyHigh}度,最低温度:{TemperatureDailylow}度
          风向:{WindDirectionDaily},风级:{WindScaleDaily}级'''
        #风向为{},温度为{temperature}摄氏度,更新时间为:{lasttime}
        return weather_str
        #print(weather_str)

    except KeyError:
        return "该城市目前没有被收录,请重新输入"


if __name__ == "__main__":
    UserInput = input('请输入所要查询的天气>>> ')
    SearchWeather(UserInput)
