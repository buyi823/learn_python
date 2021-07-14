#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-14 11:16
# time function 3

if __name__ == '__main__':
    import time
    start = time.perf_counter()
    for i in range(100):
        print(i)
    end = time.perf_counter()
    print('different is %6.3f' % (end-start))