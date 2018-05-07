from bs4 import BeautifulSoup
html="""
<a>adsad</a>
 
<a>adsad2</a>
<h1 class="h1" name="123">dsadasda2</h1>
<div>
 <p>
 <a class="h1">套</a>
 </p>
 <p>
 <a>嵌套</a>
 </p>
</div>
"""
sop=BeautifulSoup(html,"lxml")
# print(sop.find_all('p'))
# print(type(sop.find_all('p')[0]))
# print(sop.prettify())
# print(type(sop.h1))
# print(sop.a.string)
# print(sop.h1.attrs['name'])
# print(sop.div.a.string)
# print(sop.p.parent)
# for i,child in enumerate(sop.div.children):
#     print(i,child)
print(sop.find_all(attrs={"class":"h1"}))
print(sop.find_all(class_="h1"))
print(sop.select('.h1'))
print(sop.select('h1'))
for h1 in sop.select('h1'):
    print(h1['class'])
    print(h1.attrs['class'])
    print(h1.attrs['name'])
    print(h1['name'])
    print(h1.get_text())
