import requests
# response=requests.get("http://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(response.text)
# print(response.headers)
# data={
#     'bn':'da',
#     'pa':'dad'
# }
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
}
# response=requests.get("http://httpbin.org/",data)
# print(response.url)
# resp=requests.get("http://httpbin.org/get")
# print(resp.text)
#
# respon_pic=requests.get("https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2460833846,3970004509&fm=27&gp=0.jpg")
# print(respon_pic.text)
# print(respon_pic.content)
# with open("1.jpg","wb+") as f:
#     f.write(respon_pic.content)
#     f.close()
# respose=requests.Session()
# respose.get("http://httpbin.org/cookies/set/number/123",headers=headers)
# s=respose.get("http://httpbin.org/cookies")
# print(s.text)
#respose=requests.get("https://www.zhihu.com/explore")
# print(respose.cookies)
# for key,value in respose.cookies.items():
#     print(key+'---'+value)
response=requests.get("http://www.12306.cn/mormhweb/",timeout=11)
print(response.status_code)