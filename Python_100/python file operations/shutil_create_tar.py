#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-09 13:46
# shutil 创建tar

import shutil

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('d:/Test/', 'tar', 'd:/Test/')

# 调用 .unpack_archive() 并传入存档名称和目标目录，将 backup.tar 的内容提取到 extract_dir/ 中
shutil.unpack_archive('d:/Test.tar', 'd:/logs')