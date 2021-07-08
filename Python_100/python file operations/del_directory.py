#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-05 18:02
# Delete Directory

import os
from pathlib import Path

trash_dir = 'C:\\Users\\Blaine\\Desktop\\Test\\data'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error:{trash_dir}: {e.strerror}')

# 同样，你也可使用 pathlib 来删除目录
trash_dir = Path('C:\\Users\\Blaine\\Desktop\\Test\\data')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f'Error:{trash_dir}: {e.strerror}')