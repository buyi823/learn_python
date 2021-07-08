#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-08 14:49
# Archive  Compress

import zipfile
import os

# .namelist() 返回存档文件中文件和目录的名称列表
with zipfile.ZipFile('d:/zip.zip', 'r') as zipobj:
    print(zipobj.namelist())

# 要检索有关存档文件中文件的信息，使用 .getinfo()
with zipfile.ZipFile('d:/zip.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('zip/sub_dir/hello.py')
    print(f'file size: {bar_info.file_size}')
    print(f'data time: {bar_info.date_time}')
    print(f'compress size: {bar_info.compress_size}')
    print(f'filename: {bar_info.filename}')  # 显示文件路径


data_zip = zipfile.ZipFile('d:/zip.zip', 'r')
# 提取单个文件到当前目录
data_zip.extract('zip/sub_dir/hello.py')
data_zip.extractall(path='d:/Test/')
data_zip.close()
