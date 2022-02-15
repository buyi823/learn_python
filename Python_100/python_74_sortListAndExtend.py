#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-14 16:58
# 列表排序和连接

if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    a.sort()
    print(a)

    # 连接a与b
    print(a + b)

    # 连接列表a与b
    a.extend(b)
    print(a)

