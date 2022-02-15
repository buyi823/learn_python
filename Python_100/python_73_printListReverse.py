#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-14 17:17
# 反向输出一个链表

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('Please input a number:\n'))
        ptr.append(num)
    print(f"Positive list:\n{ptr}" )
    ptr.reverse()
    print(f"Reverse list:\n{ptr}")