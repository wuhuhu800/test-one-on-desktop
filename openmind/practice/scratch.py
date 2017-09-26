import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen
#soup = BeautifulSoup('http://www.gapp.gov.cn/news/1663/185929.shtml')

r = requests.get('http://www.gapp.gov.cn/news/1663/185929.shtml')
#html = urlopen("http://www.gapp.gov.cn/news/1663/185929")
#print(html)

#print(r.text)
html=r.content #目的就是为了将模板改为html格式
soup = BeautifulSoup(html,"html.parser")
#for string in soup.findAll('p'):
#    print(string.get_text(' ', strip=True))
with open ('content.txt','w') as fb:
    for string in soup.findAll('p'):#遍历soupfindall所有是P标签的内容
        str1 = u' '.join(string.stripped_strings)#将裂变转换为str解决报错TypeError: sequence item 1: expected str instance, Tag found
        fb.write(str1)
#    str1 = " ".join(string)
#    string = soup.stripped_strings:

#with open ('content.txt','w') as fb:
#    str1 = []
#    for string in soup.findAll('p'):
#        string = string.contents
#        str1.append(string)
#    for str2 in str1:
        #print(str2)
#        str3 = " ".join(str2)
#        fb.write(str3.text)
#        print(repr(string))
#m =soup.head
#print(m)
#table=soup.find('p')
#print(table)
#print(soup)
'''
allTdSoup = soup.findAll('p')
#print(allTdSoup)
with open ('content.txt','w') as fb:
    for chunck in allTdSoup:
        fb.write(chunck.text)
'''
#
#for eachTdSoup in allTdSoup:
#    print(eachTdSoup.string)
#print(soup.get_text().string)
