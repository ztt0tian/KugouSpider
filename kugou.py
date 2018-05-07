
from selenium import webdriver
from pyquery import PyQuery as pq
import time

browser = webdriver.Chrome()


def zhua(play_url):
    try:
        browser.get(play_url)
        audio = browser.find_element_by_class_name('music')
        album=browser.find_element_by_class_name('albumName').find_element_by_tag_name('a')
        print(album)
        print(browser.page_source)
        time.sleep(1)
        return (audio.get_attribute('src'),album.get_attribute('title'))
    finally:
        print()


def top(home_url):
    doc = pq(home_url)
    li = doc('.pc_temp_songlist.pc_rank_songlist_short ul li a.pc_temp_songname')
    for url in li.items():
        info=zhua(url.attr.href)
        print(url.attr.href, url.attr('title') + '-----' + info[0]+'-----'+info[1])


if __name__ == '__main__':
    # index=1;
    #
    #
    # while(index<=10):
    #     url = "http://www.kugou.com/yy/rank/home/" + str(index) + "-6666.html?from=homepage"
    #     print(url)
    #     top(url)
    #     index=index+1
    url = "http://www.kugou.com/song/me6rs87.html"
    zhua(url)