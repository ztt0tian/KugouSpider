import re
import time
from selenium import webdriver
from pyquery import PyQuery as pq
import pymysql.cursors
import mysql
# 连接MySQL数据库
connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456789', db='j2ee_music',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# 通过cursor创建游标
cursor = connection.cursor()
browser = webdriver.Chrome()
def music_detail(url,album):
    browser.get(url)
    browser.refresh()  # 注意刷新,不然全是一样的musicURL
    time.sleep(2)
    musicname=browser.find_element_by_class_name('audioName')
    musci=browser.find_element_by_class_name('songDetail')
    audio = browser.find_element_by_class_name('music')
    image=browser.find_element_by_class_name('albumImg').find_element_by_tag_name('img')
    singer = musci.find_element_by_class_name('singerName')
    #print(type(singer.get_attribute('title')))
    if(album==0):
        return (musicname.get_attribute('title'),audio.get_attribute('src'),'null',singer.get_attribute('title').replace('、',' '),image.get_attribute('src'))
    album = browser.find_element_by_class_name('albumName').find_element_by_tag_name('a')
    return (musicname.get_attribute('title'),audio.get_attribute('src'), album.get_attribute('title'),singer.get_attribute('title').replace('、',' '),image.get_attribute('src'))
                 #歌曲名 歌曲资源url 专辑 歌手 歌曲图片url
def zhuaquTop(url):
    browser.get(url)
    page_code = browser.page_source
    patter = '''"Hash":"(\w+?)".*?"album_id":(\d+?),'''
    results = re.findall(patter, page_code, re.S)
    #print(results.__len__())
    doc = pq("http://www.kugou.com/yy/html/rank.html")
    li = doc('.pc_temp_songlist.pc_rank_songlist_short ul li a.pc_temp_songname').items()
    for url, item in zip(li, results):
        zurl = url.attr.href + "#hash=" + item[0] + "&album_id=" + item[1]
        reaurl="http://www.kugou.com/song/#hash="+ item[0]+"&album_id="+ item[1]
        print(reaurl)
        #info = music_detail(zurl, item[1])
        #mysql.insertdata(connection,cursor,info,zurl)
        info = music_detail(reaurl, item[1])
        mysql.insertdata(connection, cursor, info, reaurl)
        print(info[0] + ' ' + info[2] + ' ' + info[3]+' '+info[1]+''+info[4])
        # print(url.attr.href, url.attr('title'),item[0],item[1])
# browser.get("http://www.kugou.com/yy/html/rank.html")
# page_code=browser.page_source
#
# patter='''"Hash":"(\w+?)".*?"album_id":(\d+?),'''
# results=re.findall(patter,page_code,re.S)
# print(results.__len__())
# doc = pq("http://www.kugou.com/yy/html/rank.html")
# li = doc('.pc_temp_songlist.pc_rank_songlist_short ul li a.pc_temp_songname').items()
#
# for url,item in zip(li,results):
#     zurl=url.attr.href+"#hash="+item[0]+"&album_id="+item[1]
#     #print(zurl)
#     info=music_detail(zurl,item[1])
#     print(info[0]+' '+info[1]+' '+info[2])
#     #print(url.attr.href, url.attr('title'),item[0],item[1])