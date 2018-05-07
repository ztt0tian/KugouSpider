import pymysql.cursors
import uuid
# 连接MySQL数据库
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456789', db='j2ee_music',
#                              charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# # 通过cursor创建游标
# cursor = connection.cursor()
def insertdata(conn,cursor,data,k_url):
    singername=data[3]
    songname=data[0].replace("\xa0", " ")
    songalbum=data[2].replace("&nbsp;", " ")
    songurl=data[1]
    songpicurl=data[4]
    # 歌曲名 歌曲资源url 专辑 歌手 歌曲图片url
    if(isexit_singer(conn,cursor,singername)==None):
        singerid = str(uuid.uuid1()).replace('-', '')
        albumid = str(uuid.uuid1()).replace('-', '')
        songid = str(uuid.uuid1()).replace('-', '')
        insert_singer_sql = "INSERT  INTO `singer` (`singer_id`, `singer_name`) VALUES (%s,%s)"
        insert_album_sql = "INSERT  INTO `album` (`album_id`, `album_name`,`singer_id`) VALUES (%s,%s,%s)"
        insert_song_sql = "INSERT INTO `song` (`id`, `music_name`,`music_url`,`music_pic_url`,`album_id`,`singer_id`,`kugou_url`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_singer_sql, (singerid, singername))
        cursor.execute(insert_album_sql, (albumid, songalbum, singerid))
        cursor.execute(insert_song_sql, (songid, songname, songurl, songpicurl, albumid, singerid, k_url))
        conn.commit()
    else:
        exist_singer_id=isexit_singer(conn,cursor,singername)
        if(isexit_album(conn,cursor,exist_singer_id,songalbum)==None):
            albumid = str(uuid.uuid1()).replace('-', '')
            songid = str(uuid.uuid1()).replace('-', '')
            insert_album_sql="INSERT  INTO `album` (`album_id`, `album_name`,`singer_id`) VALUES (%s,%s,%s)"
            insert_song_sql = "INSERT INTO `song` (`id`, `music_name`,`music_url`,`music_pic_url`,`album_id`,`singer_id`,`kugou_url`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_album_sql, (albumid, songalbum, exist_singer_id))
            cursor.execute(insert_song_sql, (songid, songname, songurl, songpicurl, albumid, exist_singer_id, k_url))
        else:
            exist_album_id=isexit_album(conn,cursor,exist_singer_id,songalbum)
            if(isexit_song(conn,cursor,exist_singer_id,exist_album_id,songname)==None):
                songid = str(uuid.uuid1()).replace('-', '')
                insert_song_sql = "INSERT INTO `song` (`id`, `music_name`,`music_url`,`music_pic_url`,`album_id`,`singer_id`,`kugou_url`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(insert_song_sql,(songid, songname, songurl, songpicurl, exist_album_id, exist_singer_id, k_url))
            else:
                print("歌曲已存在")
        conn.commit()

    # insert_singer_sql="INSERT  INTO `singer` (`singer_id`, `singer_name`) VALUES (%s,%s)"
    # insert_album_sql="INSERT  INTO `album` (`album_id`, `album_name`,`singer_id`) VALUES (%s,%s,%s)"
    # insert_song_sql="INSERT INTO `song` (`id`, `music_name`,`music_url`,`music_pic_url`,`album_id`,`singer_id`,`kugou_url`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    # #sql="INSERT INTO `song` (`name`, `album`,`singer`,`url`,`pic_url`) VALUES (%s,%s,%s,%s,%s)"
    # cursor.execute(insert_singer_sql,(singerid,singername))
    # cursor.execute(insert_album_sql,(albumid,songalbum.replace("&nbsp;"," "),singerid))
    # cursor.execute(insert_song_sql,(songid,songname,songurl,songpicurl,albumid,singerid,k_url))
    # conn.commit()
# def updata(conn,cursor,data,k_url):
#     songurl = data[1]
#     id=isexit_song(conn,cursor,data)
#     if(id!=None):
#         updata_sql="UPDATE song SET song.music_url ="+repr(songurl)+"WHERE song.id="+repr(id)
#         cursor.execute(updata_sql)
#         conn.commit
#     insertdata(conn,cursor,data,k_url)


def isexit_singer(conn,curosur,singer_name):
    query_sql="SELECT * FROM singer WHERE singer.singer_name="+repr(singer_name)
    print(query_sql)
    curosur.execute(query_sql)
    conn.commit()
    result=curosur.fetchone()
    print(result)
    if (result!=None):
        return result['singer_id']
    else:
        return None
def isexit_album(conn,curosur,singer_id,album_name):
    query_sql="SELECT * FROM album WHERE album.singer_id="+repr(singer_id)+" AND album.album_name="+repr(album_name)
    print(query_sql)
    curosur.execute(query_sql)
    conn.commit()
    result = curosur.fetchone()
    print(result)
    if (result!=None):

        return result['album_id']
    else:
        return None
def isexit_song(conn,curosur,singerid,albumid,songname):
    query_sql="SELECT * FROM song WHERE song.singer_id="+repr(singerid)+"AND song.album_id="+repr(albumid)+"AND song.music_name="+repr(songname);
    print(query_sql)
    curosur.execute(query_sql)
    conn.commit()
    result = curosur.fetchone()
    print(result)
    if(result!=None):
        return result['id']
    return None