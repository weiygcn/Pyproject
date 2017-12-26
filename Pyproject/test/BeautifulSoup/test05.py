from bs4 import BeautifulSoup
import requests

url ='https://www.qiushibaike.com/'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
file = requests.get(url,headers=Headers) #,verify=True
soupObject = BeautifulSoup(file.content, 'html.parser')
c = soupObject.find_all(class_='content')
for i in c:
    duan = i.span.contents[0]
    print(duan)
    print('\n')
