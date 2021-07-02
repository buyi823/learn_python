#!/usr/bin/python
# -*- coding: UTF-8 -*-
# os.walk() 用于通过从上到下或从下到上遍历树来生成目录树中的文件名

import os

# os.walk() 默认是从上到下遍历目录:
for dirpath, dirname, files in os.walk('.', topdown=False):
    # 要以自下而上的方式遍历目录树，则将 topdown=False 关键字参数传递给 os.walk()
    print(f'Found directory:{dirpath}')
    for file_name in files:
        print(file_name)
