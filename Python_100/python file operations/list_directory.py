#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# operation directory
# 遗留版本的Python获取目录列表

import os
entries = os.listdir('/home/blaine/buyi/learn_python')

for entry in entries:
    print(entry)