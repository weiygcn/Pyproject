# coding:utf-8
import requests

# r = requests.get('http://test.api.zsmy.cn/wx/zsmy/getToken')
# print(r.status_code)
# print('\n')
# print(r.text)
url_path = 'http://zzk.cnblogs.com/s/blogpost'
par = {'Keywords': 'yoyoketang'}
# 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive', 'Content-Type': 'text/html; charset=utf-8'}

r = requests.get(url=url_path, params=par,headers=headers)
print(r.status_code)
print(r.text)
# print('==========')
# print(r.text)
