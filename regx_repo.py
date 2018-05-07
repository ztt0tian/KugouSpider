import re
import requests
def spider(url):
    patt="http://fs.w.kugou.com/.+.mp3"
    response=requests.get(url)
    musicstr=str(response.text)
    f=open("page/")
    url_res=re.findall(patt,musicstr)
    print(url_res.__len__())
    for music in url_res:
        print(music)

headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
}
patter="http://www.kugou.com/song/\w+.html"
response=requests.get("http://www.kugou.com/yy/rank/home/1-6666.html?from=homepage",headers=headers)
print(response.text)
string=str(response.text)
print(string)
resuilt=re.findall(patter,string)
print(resuilt.__len__())
for url in resuilt:
    print(url)
