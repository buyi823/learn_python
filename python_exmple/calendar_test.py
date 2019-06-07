#!/usr/bin/python3
# filename calendar

import calendar

yy = int(input("请输入年份："))
mm = int(input("请输入月份："))

print(calendar.month(yy, mm))
