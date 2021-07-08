#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-08 16:28
# 从加密的文档提取数据

import zipfile

with zipfile.ZipFile('d:/secret.zip', 'r') as pwd_zip:
    pwd_zip.extractall(path='d:/secret/', pwd=b'1234')
