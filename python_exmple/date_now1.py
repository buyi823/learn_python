#!/usr/bin/python3
# 将时间戳转换为指定格式日期
import datetime
now = datetime.datetime.now()
print(now)
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)