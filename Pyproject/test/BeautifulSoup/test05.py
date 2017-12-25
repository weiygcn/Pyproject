from bs4 import BeautifulSoup
import requests

url ='https://www.qiushibaike.com/'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
file = requests.get(url,headers=Headers) #,verify=True
soupObject = BeautifulSoup(file.content, 'html.parser')
# print(tag.attrs)
c = soupObject.find_all(class_='content')
# content=c.
print(type(c))
# for k,v in enumerate(c):
#     print('=====%s======',k,'\t值为：'+v)
#     # print(i)
#     print('\n')
# for i in tagObj:
#     print(i)
#     print('==========================')
# print('#################################')
# print(tagObj['script'])
