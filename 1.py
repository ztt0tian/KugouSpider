# from urllib.parse import urlencode
# params={
#     'name':'dsad',
#     'age':'22'
# }
# base_url="http://www.baidu.com?"
# url=base_url+urlencode(params)
# print(url)
import uuid
print(str(uuid.uuid1()).replace('-',''))