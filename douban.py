import requests
import re
content=requests.get('https://book.douban.com/').text
print(content)
pattern=re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-data.*?author">(.*?)*?</span>.*?year">(.*?).*?</span>.*?</li>',re.S)
print(pattern)
resul=re.findall(pattern,content)
for x in resul:
    print(x)