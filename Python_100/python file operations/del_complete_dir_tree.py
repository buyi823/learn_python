#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-05 18:12
# Delete the complete directory tree

import shutil
import os

trash_dir = 'C:\\Users\\Blaine\\Desktop\\Test\\data'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error:{trash_dir}: {e.strerror}')

# 当调用 shutil.rmtree() 时，trash_dir 中的所有内容都将被删除。
#  在某些情况下，你可能希望以递归方式删除空文件夹。 
# 你可以使用上面讨论的方法之一结合 os.walk() 来完成此操作:

# 这个执行的时候小心
# 这将遍历目录树并尝试删除它找到的每个目录。 如果目录不为空，则引发OSError并跳过该目录
for dirpath, dirnames, files in os.walk('.', topdown=False):
    try:
        os.rmdir(dirpath)
    except OSError as ex:
        pass