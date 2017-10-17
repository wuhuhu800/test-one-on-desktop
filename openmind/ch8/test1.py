

import requests
headers ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url1 ='http://weixin.sogou.com/weixin?type=1&query={}&ie=utf8&s_from=input&page={}&_sug_=n&_sug_type_='
url ='http://weixin.sogou.com/weixin?type=1&query=python&ie=utf8&s_from=input&page=1&_sug_=n&_sug_type_='
content = requests.get(url,headers).content
print(content)
