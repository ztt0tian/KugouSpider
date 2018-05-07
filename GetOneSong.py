import re
import time
from selenium import webdriver
from pyquery import PyQuery as pq
import pymysql.cursors
import mysql
#根据播放链接添加歌曲
# 连接MySQL数据库
connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456789', db='j2ee_music',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# 通过cursor创建游标
cursor = connection.cursor()
browser = webdriver.Chrome()
def music_detail(url):
    browser.get(url)
    time.sleep(2)
    musicname=browser.find_element_by_class_name('audioName')
    musci=browser.find_element_by_class_name('songDetail')
    audio = browser.find_element_by_class_name('music')
    image=browser.find_element_by_class_name('albumImg').find_element_by_tag_name('img')
    singer = musci.find_element_by_class_name('singerName')
    album=album=browser.find_element_by_class_name('albumName').find_element_by_tag_name('a')
    #print(type(singer.get_attribute('title')))
    print(album)
    if(album==None):
        return (musicname.get_attribute('title'),audio.get_attribute('src'),'null',singer.get_attribute('title').replace('、',' '),image.get_attribute('src'))
    album = browser.find_element_by_class_name('albumName').find_element_by_tag_name('a')
    return (musicname.get_attribute('title'),audio.get_attribute('src'), album.get_attribute('title'),singer.get_attribute('title').replace('、',' '),image.get_attribute('src'))
                 #歌曲名 歌曲资源url 专辑 歌手 歌曲图片ur
if __name__ == '__main__':
    K_URL="http://www.kugou.com/song/#hash=05493A69E5783F1A459987C6AF39F37D&album_id=575254"
    mysql.insertdata(connection,cursor,music_detail(K_URL),K_URL)