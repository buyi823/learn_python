#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-14 11:09
# 时间函数2

if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
    print(end-start)
    