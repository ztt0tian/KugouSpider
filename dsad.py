
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.kugou.com/song/#hash=63AE4A906E79C302C1E7DC05BEDD0B1C&album_id=8455348")
#a=browser.find_element_by_class_name('pc_temp_songname')
#a.click()

print(browser.page_source)
album=browser.find_element_by_class_name('albumName').find_element_by_tag_name('a')
print(album.get_attribute('title'))
