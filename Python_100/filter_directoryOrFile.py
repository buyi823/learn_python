#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 如何使用 os.listdir() ，os.scandir() 和 pathlib.Path() 过滤打印出目录中文件或者目录的名称

import os
from pathlib import Path

print('---use listdir() and filter----')
basepath = '/home/blaine/buyi/learn_python'
for entry in os.listdir(basepath):
    # 使用os.path.isfile判断该路径是否是文件类型
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

print('---use scandir() and filter----')
basepath = '/home/blaine/buyi/learn_python'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

print('----use basepath.iterdir() and filter----')
basepath = Path('/home/blaine/buyi/learn_python')
for entry in basepath.iterdir():
    if entry.is_file():
        print(entry.name)

print('##########list directory#######')

print('--use listdir()----')
basepath = '/home/blaine/buyi/learn_python'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)
    
print('--use scandir()---')
basepath = '/home/blaine/buyi/learn_python'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)

print('---use pathlib.Path()---')
basepath = Path('/home/blaine/buyi/learn_python')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
