#!/usr/bin/python3
# -*- Coding: UTF-8 -*-

import os
from pathlib import Path

# 要创建单个目录，把目录路径作为参数传给 os.mkdir()
# 如果该目录已经存在，os.mkdir() 将抛出 FileExistsError 异常
# os.mkdir('D:/buyi_prac/Python_100/This_is_a_directory')

# pathlib 来创建目录
p = Path('D:/buyi_prac/Python_100/This_is_a_directory1')
# 传入 exist_ok=True 参数来忽略 FileExistsError 异常
# p.mkdir(exist_ok=True)

# 为了避免像文件存在这样的错误抛出， 当发生错误时捕获错误并让你的用户知道
try:
    p.mkdir()
except FileExistsError as e:
    print(e)
