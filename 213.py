
import re
import requests
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
}
patter="http://fs.w.kugou.com/201804111505/9aae3a7410899852b2979880e07a6039/G130/M0B/1F/0D/IocBAFqw6zSAAaVLADSo_S-IxQw181.mp3"
response=requests.get("http://www.kugou.com/song/mctly98.html#hash=80D7B5EBE2BC88F1E170917368A11140&album_id=0")
print(response.text)
string=str(response.text)
print(string)
resuilt=re.findall(patter,string)
print(resuilt.__len__())
for url in resuilt:
    print(url)