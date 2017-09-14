'''
import sys
import requests

url = "https://api.seniverse.com/v3/weather/now.json"

paramsdict ={'key': 'lom0ftfaihx65jh0','location':'北京' ,'language': 'zh-Hans','unit': 'c'}
req = requests.get(url,params=paramsdict,timeout =1)

print(req)
'''
import requests
API = "https://api.seniverse.com/v3/weather/daily.json"


def fetchWeather(location):
    result = requests.get(API, params={
        'key': 'lom0ftfaihx65jh0',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=10)
    return result.text


if __name__ == '__main__':

    result = fetchWeather('北京')
    print(result)
