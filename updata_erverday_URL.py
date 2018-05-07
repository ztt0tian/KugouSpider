from selenium import webdriver
import pymysql
import time
import pymysql.cursors

# 连接MySQL数据库
connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456789', db='j2ee_music',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# 通过cursor创建游标
cursor = connection.cursor()
browser = webdriver.Chrome()


def music_detail(url):
    browser.get(url)
    browser.refresh()  # 注意刷新,不然全是一样的musicURL
    time.sleep(2)
    music_url = browser.find_element_by_class_name('music').get_attribute('src')
    return music_url


def update_url(conn, cursor, songid, newurl):
    updata_sql = "UPDATE song SET song.music_url =" + repr(newurl) + " WHERE song.id=" + repr(songid)
    print(updata_sql)
    cursor.execute(updata_sql)
    conn.commit()


if __name__ == '__main__':
    sql_quey = "SELECT song.id,song.kugou_url FROM song"
    cursor.execute(sql_quey)
    connection.commit()
    list = cursor.fetchall()
    print(type(list))
    print(list.__len__())
    print(range(list.__len__()))
    index = 1984
    #273 618 887 1193 1290 1984
    while (index < list.__len__()):
        newurl = music_detail(list[index]['kugou_url'])
        songid = list[index]['id']
        update_url(connection, cursor, songid, newurl)
        index = index + 1
        print(index)
