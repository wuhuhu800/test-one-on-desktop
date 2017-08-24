import requests
r = requests.get('https://api.github.com/events',stream = True)
with open ('test.txt','wb') as fb:
    for chunck in r.iter_content(1):
        fb.write(chunck)