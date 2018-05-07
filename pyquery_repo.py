html = """
<a>adsad</a>

<a>adsad2</a>
<h1 class="h1" name="123">dsadasda2</h1>
<div>
 <p>
 <a class="h1">套</a>
 </p>
 <p>
 <a>嵌套</a>
 <audio>dasd</audio>
 </p>
</div>
"""
da="das"

da2='dsa'
print(type(html))
print(type(da2))
from pyquery import PyQuery as pq
#doc=pq(url="https://y.qq.com/portal/player.html")
#doc=pq(filename='213.py')
doc=pq(url="http://www.kugou.com/yy/rank/home/1-6666.html?from=homepage")
li=doc('.pc_temp_songlist.pc_rank_songlist_short ul li a.pc_temp_songname')
#print(li.items())
for url in li.items():
    print(url.attr.href,url.attr('title'))
#print(li)
doc2=pq(url="http://www.kugou.com/song/#hash=EE0D951E364C4B3300DB6C727CFFF5DD&album_id=8455481")
audio=doc2('audio')
print(audio)