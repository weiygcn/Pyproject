# coding:utf-8
import requests
url='https://www.baidu.com/'
r=requests.get(url,verify=True)
print(r.url)
print('\n=======encoding=========',r.encoding)
print('\n=======content=========',r.content)
print('\n=======headers=========',r.headers)
print('\n=======cookies=========',r.cookies)
print('\n=======raw=========',r.raw)
print('\n=======raise=========',r.raise_for_status())