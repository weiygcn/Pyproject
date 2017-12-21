import requests

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

data = {'logonId': '18170358569',
        'passwordSecurityId': 'web|authcenter_querypwd_login|634d38ca-5dad-4be9-bb1b-aa8ffdb46bf8RZ13',
        'password': 'WEL/Fbfs6GxkCpuRnL0jZpmJZC4/t7fzEwIOjpbfR7EOzkouEI7o3V69icA/HGQKc9q+Mt5DttyC7Rc9oYkBTFVtYcUOqjNif5ErakVQE9Sj565uIlrO7ToVgdFK5+yxJLsadfBUIJRwt6pQ4eNIVjdDJ9mYaNcfIXeloY7MRxd9cMG+kwF/qupe4FFyGKkA5yZng425b3agiDj5T4YKGNNkSJYx64MlqauYpvgWj9aLlUQzp+QcC9Gc7ZABEvuJSzGtw+koHdShjUtqaNI0mKjoIcRChS6y4Slbb4plEGSYdypKV/rMmxYSYpE5+5w22/gCiEYwT1O8rTBS3AAfiQ=='}
# 参数关联，拼接在url请求上的参数
QueryString_uuid = '85e4e3e261d9431ea092.1513740728.1.0.0'
QueryString_service = 'www'
QueryString_continue = 'http://www.meituan.com/account/settoken?continue=http%3A%2F%2Fwww.meituan.com%2F'

Login_url = 'https://passport.meituan.com/account/unitivemobilelogin'
Login_url2 = 'https://passport.meituan.com/account/unitivemobilelogin?uuid=' + QueryString_uuid + '&service=' + QueryString_service + '&continue=' + QueryString_continue

print(Login_url,end='\n======================\n')
session=requests.session()
r = session.post(Login_url, data=data, headers=Headers, verify=True, allow_redirects=True)
print(r.url,end='\n++++++++++++++++++++++++\n')
# print(r.raise_for_status())
print(r.history,'\n')
print(r.text)
