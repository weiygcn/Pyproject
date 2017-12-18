import requests

url = 'http://test.api.zsmy.cn/user/distributor/mySubordinateList'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate',
#     'Connection': 'keep-alive', 'Content-Type': 'text/html; charset=utf-8', 'content-type': 'application/json',
#     'x-cert-token': 'iloveyudi', 'x-cert-uid': '482'}

headers = {
    'x-cert-token': 'iloveyudi', 'x-cert-uid': '482'}
payload = {'page': '1', 'size': '20', 'role': '2'}
r = requests.post(url, json=payload, headers=headers)
print(r.json())
