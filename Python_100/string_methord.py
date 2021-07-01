#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 字符串方法

import os
import fnmatch

for f_name in os.listdir('D:/buyi_prac/Python_100'):
    if f_name.endswith('.txt'):
        print(f_name)
# 上述代码找到 目标路径中的所有文件，遍历并使用 .endswith() 来打印所有扩展名为 .txt 的文件名
print('------I\'m just the delimiter------')

# 字符串方法匹配的能力是有限的。fnmatch 有对于模式匹配有更先进的函数和方法。
# 我们将考虑使用 fnmatch.fnmatch() ，这是一个支持使用 * 和 ? 等通配符的函数。
# 例如，使用 fnmatch 查找目录中所有 .txt 文件，你可以这样做:
for f_name in os.listdir('D:/buyi_prac/Python_100'):
    if fnmatch.fnmatch(f_name, '*.txt'):
        print(f_name)
print('------I\'m just the delimiter------')

# 假设你想要查找符合特定掉件的 .txt 文件。
# 例如，你可能指向找到包含单次 data 的 .txt文件，一组下划线之间的数字，以及文件名中包含单词 backup 。
# 就类似于 data_01_backup, data_02_backup, 或 data_03_backup 。

for f_name in os.listdir('D:/buyi_prac/Python_100'):
    if fnmatch.fnmatch(f_name, 'data_*_backup.txt'):
        print(f_name)