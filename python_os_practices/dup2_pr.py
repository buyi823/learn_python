#!/usr/bin/python3

# 这个运行部通过
import os

# open file
f=open('txt','a')

# 将这个文件描述符代表的文件，传递给 1 描述符指向的文件（也就是 stdout）
os.dup2(f.fileno(),1)

# 关闭文件
f.close()

# print 输出到标准输出流，就是文件描述符1
print('runoob')
print('google')