#!/usr/bin/python3
# -*- Coding: UTF-8 -*-
# By Blaine 2021-07-05 17:38
# Python 删除文件

import os

# data_file = 'C:\\Users\\Blaine\\Desktop\\Test\\data.txt'
# os.remove(data_file)
# 使用 os.unlink() 删除文件与使用 os.remove() 的方式类似
# os.unlink(data_file)

"""
在文件上调用 .unlink() 或 .remove() 会从文件系统中删除该文件。 
如果传递给它们的路径指向目录而不是文件，这两个函数将抛出 OSError 。 
为避免这种情况，
可以检查你要删除的内容是否是文件，并在确认是文件时执行删除操作，或者可以使用异常处理来处理 OSError 
"""

data_file = 'C:\\Users\\Blaine\\Desktop\\Test\\data.txt'
# 如果类型是文件则进行删除
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')

# 以下示例说明如何在删除文件时使用异常处理来处理错误
data_file = 'C:\\Users\\Blaine\\Desktop\\Test\\data.txt'

try:
    os.remove(data_file)
except OSError as e:
    print(f'Error:{data_file}:{e.strerror}')