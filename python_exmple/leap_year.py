#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename : leap year
# author by : Blainexu

 # Python 的 calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年
# import calendar
# print(calendar.isleap(2000))

year = int(input('input one year: '))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('{0} is leap year'.format(year))
        else:
            print('{0} is not leap year'.format(year))
    else:
        print('{0} is not leap year'.format(year))
else:
    print('{0} is not leap year'.format(year))