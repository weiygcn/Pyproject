import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', }

cookie = {
    '_lxsdk_cuid': '16071e814e119-028d8dbf150e3a-b7a103e-1fa400-16071e814e2c8',
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    'webloc_geo': '31.196461%2C121.321042%2Cwgs84',
    'ci': '10',
    '__mta': '210089258.1513739523829.1513739523829.1513740714242.2',
    '_lxsdk_s': '16071e814e2-106-ff7-a9e%7C%7C4',
    'mtcdn': 'K',
    'u': '245452928',
    'n': 'HXs738289666',
    'lt': 'NfOjXH6KH5B5yyxDEMRVxa6N09UAAAAAHwUAAC0T5qRT-e2sQKvvb8GiYMixsmyPAqKb0yggZe89BrSN6_qR86YtB-8JFHz3r7O6QA',
    'lsu': '',
    'oc': '-9aKwMuLPnekgo0F3cumr9ekAtamsauxym0UJWRbejezJHd7ji5LsX7T3_aMQciwLg4uA4co6oknFIzVXS2NicCo5Q-vIEgavRnx-ww3ADS6EaTL83cWTQVNZqB_-Cx-7ToGCWtlCWYoy45ZoLbZfBG4Jv-aZDrbTjZVBg9iLx4',
    'token2': 'NfOjXH6KH5B5yyxDEMRVxa6N09UAAAAAHwUAAC0T5qRT-e2sQKvvb8GiYMixsmyPAqKb0yggZe89BrSN6_qR86YtB-8JFHz3r7O6QA',
    'uuid': '85e4e3e261d9431ea092.1513739528.2.0.1',
    'em': 'bnVsbA',
    'om': 'bnVsbA'}
userinfo_url = 'http://www.meituan.com/account/userinfo/'
session = requests.session()
c = requests.cookies.RequestsCookieJar()
for k, v in cookie.items():
    c.set(k, v)
session.cookies.update(c)
r = session.get(userinfo_url, headers=headers, verify=True)
print(r.raise_for_status())