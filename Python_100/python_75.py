#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-14 16:51
# 

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print(64 + i)
         