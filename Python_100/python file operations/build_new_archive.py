#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-09 10:48
# 创建新的存档文件

import zipfile
import os

# 要创建新的ZIP存档，请以写入模式（w）打开 ZipFile 对象并添加要归档的文件：
# file_list = ['file.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
# with zipfile.ZipFile('d:/new.zip', 'w') as new_zip:
#     for name in file_list:
#         new_zip.write(name)
# 上面代码无法运行，报错



# 要将文件添加到现有的存档文件，请以追加模式打开 ZipFile 对象，然后添加文件：
with zipfile.ZipFile('d:/new.zip', 'a') as new_zip:
    new_zip.write('d:/password.txt')
    new_zip.write('d:/FTP command.txt')