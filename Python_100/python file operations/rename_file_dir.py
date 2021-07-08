#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-08 14:17
# os.rename(src, dst)

import os
from pathlib import Path

os.rename('D:\send mail.txt', 'D:\send_mail.txt')

# 重命名文件或目录的另一种方法是使用 pathlib 模块中的 rename（）：
data_file = Path('D:\send_mail.txt')
data_file.rename('D:\send_mail1.txt')