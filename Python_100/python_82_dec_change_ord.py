#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-28 18:07
# 八进制转换为十进制

if __name__ == '__main__':
    n = 0
    p = input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)