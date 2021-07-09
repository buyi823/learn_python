#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-09 11:22
# 打开tar存档文件

import tarfile
import os

with tarfile.open('d:/example.tar', 'r') as tar_file:
    print(tar_file.getnames())
