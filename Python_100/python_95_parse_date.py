#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-07-12 15:30
# 字符串日期转换为易读的日期格式。

from dateutil import parser
dt = parser.parse("July 12 2021 12:00AM")
print(dt)