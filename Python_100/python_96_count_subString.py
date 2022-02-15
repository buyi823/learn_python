#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-12 15:20
# 计算字符串中子串出现的次数。

if __name__ == '__main__':
    str1 = input("Please input a sting:\n")
    str2 = input("Please input a sub string\n")
    ncount = str1.count(str2)
    print(ncount)