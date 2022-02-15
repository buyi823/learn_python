#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-14 10:45
# 时间函数举例

if __name__ == '__main__':
    import time
    import calendar
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))
    print(calendar.month(2021, 7))
    
