from selenium import webdriver
import time
from pyquery import PyQuery as pq
from lxml import etree
browser=webdriver.Chrome()
try:
    browser.get('http://www.kugou.com/song/gngg426.html')
    html=browser.page_source
    input=browser.find_element_by_tag_name('audio')
    audio=browser.find_element_by_class_name('music')
    print(audio.get_attribute('src'))
    print(input)
finally:
    browser.close()
# browser.get('http://www.taobao.com')
# input=browser.find_element_by_id('q')
# input.send_keys('电脑')
# time.sleep(1)
# btn=browser.find_element_by_class_name('btn-search')
# btn.click()
# browser.execute_script('alert("hello")')