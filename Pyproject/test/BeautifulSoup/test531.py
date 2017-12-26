import requests
from bs4 import BeautifulSoup
import os
import re


class test():
    url = 'http://699pic.com/sousuo-218808-13-1-0-0-0.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    session = requests.session()
    r = session.get(url, headers=headers, verify=False)
    soupObj = BeautifulSoup(r.content, 'html.parser')
    file = soupObj.find_all(class_='lazy')
    creatPath = 'D:\\Pyproject\Pyproject\\test\\BeautifulSoup\\JPG\\'
    if os.path.exists(creatPath) == True:
        print('目录已存在，不执行创建')
    else:
        os.system('mkdir ' + creatPath)
    print(file)
    print('\n' + '======================================')

    # 过滤文件名非法字符
    def validateTitle(title):
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        new_title = re.sub(rstr, "_", title)  # 替换为下划线
        return new_title

    for f in file:
        countNum = file.__len__() + 1
        currentNum = file.index(f) + 1
        print('总共%s张图,当前操作第%s张图' % (countNum, currentNum))
        # new_file_name 为做字符串阶段处理，因为有的图片素材的备注中存在逗号，等等符号，会导致命名文件失败
        file_name = f['alt']
        file_name = validateTitle(file_name)
        print(file_name)
        get_url = f['data-original']
        with open(creatPath + file_name + '.jpg', 'wb') as newFile:
            newFile.write(requests.get(get_url).content)


if __name__ == '__main__':
    test()
