import requests
#示例未完成
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url = 'https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?qzonetoken=48ea57120d82974787a498d58cb48ca7d856189318d91a17d6e99bc508ecb627fc9abdeeb04877a09c89&g_tk=51782539'
cookies1 = {'qzone_check': '', '_qz_referrer': '', 'Loading': 'Yes'}
cookie = {'pgv_pvi': '2751802368',
          'RK': 'zDm+Kaj/Oi',
          'pgv_pvid': '3009801880',
          'ptcz': 'd2011dd1a89f85e0e7e1c287ec9275316a9b47a09906718c46c0c527c3f1d620',
          'pt2gguin': 'o0848316607',
          'uin': 'o0848316607',
          'skey': '@uQMWRXfTw',
          'p_uin': 'o0848316607',
          'pt4_token': '5zkleW2WDAa4dgh8msLGb*5JKfjmZkovMzq2Nsd49jU_',
          'p_skey': 'tsdM1HaQgwVpnWA9y6ARB6nbTIi-J79kPrKM9r*C9d0_',
          'Loading': 'Yes', 'qqmusic_uin': '', 'qqmusic_key': '',
          'qqmusic_fromtag': '',
          'qz_screen': '1366x768',
          'pgv_info': 'ssid:s9982883798',
          'QZ_FE_WEBP_SUPPORT': '1',
          'qzmusicplayer': 'qzone_player_848316607_1513416554819',
          'cpu_performance_v8': '3'}
data = {'syn_tweet_verson': '1', 'paramstr': '1', 'pic_template': '', 'richtype': '', 'richval': '', 'special_url': '',
        'subrichtype': '', 'who': '1', 'con': 'test', 'feedversion': '1', 'ver': '1', 'ugc_right': '1', 'to_sign': '0',
        'hostuin': '848316607', 'code_version': '1', 'format': 'fs',
        'qzreferrer': 'https%3A%2F%2Fuser.qzone.qq.com%2F848316607%2Finfocenter'}
s=requests.session()
c = requests.cookies.RequestsCookieJar()
for k,v in cookie.items():
    c.set(k,v)
s.cookies.update(c)
r = s.post(url,json=data,headers=Headers, verify=True)
print(r.text)