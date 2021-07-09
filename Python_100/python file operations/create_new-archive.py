#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-09 13:31
# create new tar archive

import tarfile

file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']
with tarfile.open('packages.tar', mode='w') as tar:
    for file in file_list:
        tar.add(file)
    # 无法运行系统找不到文件，不知道该怎么回事
    # file_list这是列表，并不是实际文件，疑惑？？？？？？？

# Read the contents of the newly created archive
with tarfile.open('package.tar', mode='r') as t:
    for member in t.getmembers():
        print(member.name)