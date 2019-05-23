#!/usr/bin/python3

import os, sys
# open file
fd = os.open("D:\\buyi_github_project\\learn_python\\python_os_practices\\foo.txt", os.O_RDWR|os.O_CREAT)

# copy file 描述符
d_fd = os.dup(fd)

# 使用复制的文件描述符写入文件
os.write(d_fd, "This is test".encode())

# close file
os.closerange(fd, d_fd)

print("close all files successed")