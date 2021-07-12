#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-12 14:44
# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

if __name__ == '__main__':
    from sys import stdout
    filename = input("Please input file name:\n")
    fp = open(filename, 'w')
    ch = input("Please input strings:\n")
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()