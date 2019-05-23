#!/usr/bin/python3

import os, sys
# open file
fd = os.open("D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt", os.O_RDWR|os.O_CREAT)

# 写入字符串
os.write(fd, b'this is a test')
#关闭文件
os.close(fd)

print('关闭文件成功')