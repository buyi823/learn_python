#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-04 19:04
# mutliple table

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
    