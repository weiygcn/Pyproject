import requests
from bs4 import BeautifulSoup


class test:
    url = 'https://www.cnblogs.com/zfquan/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    session = requests.session()
    r = session.get(url, headers=headers, verify=True)
    soupObj = BeautifulSoup(r.content, 'html.parser')
    content = soupObj.find_all(class_='c_b_p_desc')
    for i in content:
        print('##########', '\n', i.__len__())
        print('子孙节点的个数：', len(list(i.descendants)))
        # print(i.contents)
        # for ii in i:
        #     print(ii)
        #     print('-----------')
        print('子节点的个数：', len(list(i.children)))
        # for ii in i.children:
        #     print(ii)
        #     print('~~~~~~~~~~')
        for ii in i.descendants:
            print(ii)
            print('++++++++++++')


if __name__ == '__main__':
    test()
