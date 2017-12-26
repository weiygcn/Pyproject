#!/bin/bash/env python
import sys
import shutil
import glob

def get_dir_all(path):
    return glob.glob(path)


def get_dir_iterator(path):
    return glob.iglob(path)


def main():
    # glob_dir = get_dir_all(r'D:/Pyproject/Pyproject/test/test/*.py')
    # print(glob_dir,'\n',glob_dir.__len__())
    # for i in glob_dir:
    #     print(i)
    iglob_dir = get_dir_iterator(r'D:\迅雷下载\*.exe')
    for it in iglob_dir:
        print(it)

if __name__ == '__main__':
    main()
