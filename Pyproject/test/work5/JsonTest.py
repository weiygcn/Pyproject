import json
import requests

'''
d1 = {"a": None, "b": False, "c": True, "d": "BAB2", "e": ["1", 12], "f": (
    "1n", 90), "g": {"h": 1, "i": "11", "j": True}}
print(type(d1))
js = json.dumps(d1)
print(js)
'''

url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
session = requests.session()
r = session.get(url, headers=Headers, verify=False)
result=r.json()
print('快递公司名称=',result['company'],end="\n")
data=result['data']
get_result = data[0]['context']
if u'已签收' in get_result:
    print("已签收")
else:
    print("未签收")