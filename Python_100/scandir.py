#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 在现代Python版本中，可以使用 os.scandir() 和 pathlib.Path 来替代 os.listdir()

import os
# os.scandir() 调用时返回一个迭代器而不是一个列表
entries = os.scandir('/home/blaine/buyi/learn_python')
print(entries)

# ScandirIterator 指向了当前目录中的所有条目。你可以遍历迭代器的内容，并打印文件名
with os.scandir('/home/blaine/buyi/learn_python') as entries:
    for entry in entries:
        print(entry.name)