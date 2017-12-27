import requests
from bs4 import BeautifulSoup
import re


def test():
    url = 'http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    session = requests.session()
    r = session.get(url, headers=headers, verify=False)
    soupObj = BeautifulSoup(r.content, 'html.parser')
    c = soupObj.find_all(class_='catListTitle')
    print(c)
    patten = re.compile('<li><a href="(.*?)">(.*?)</a></li>', re.S)
    tags = re.findall(patten, str(c))
    print(tags)
    for a in tags:
        print(a)
        print(a[1])


if __name__ == '__main__':
    test()
