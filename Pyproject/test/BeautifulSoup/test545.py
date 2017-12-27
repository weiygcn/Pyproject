import requests
from bs4 import BeautifulSoup


class test:
    url = 'http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    session = requests.session()
    r = session.get(url, headers=headers, verify=True)
    soupObj = BeautifulSoup(r.content, 'html.parser')
    content = soupObj.find_all(class_='catListTag')
    for i in content:
        print(i.text,end='\t\n')
        print(dir(i))


if __name__ == '__main__':
    test()
