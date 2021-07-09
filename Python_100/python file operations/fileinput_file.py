#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-09 13:51
# 使用fileinput循环遍历多个文件

import fileinput
import sys

files = fileinput.input()
for line in files:
    if fileinput.isfirstlin():
        print(f'\n--- Reading {fileinput.filename()}---')
    print(' ->' + line, end='')
print()