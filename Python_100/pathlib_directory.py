#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 另一个获取目录列表的方法是使用 pathlib 模块

from pathlib import Path

entries = Path('/home/blaine/buyi/learn_python')
for entry in entries.iterdir():
    print(entry.name)

# 使用 pathlib.Path() 或 os.scandir() 来替代 os.listdir() 是获取目录列表的首选方法，
# 尤其是当你需要获取文件类型和文件属性信息的时候。
# pathlib.Path() 提供了在 os 和 shutil 中大部分处理文件和路径的功能，并且它的方法比这些模块更加有效  