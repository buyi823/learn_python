#!/usr/bin/python3
# 指定时间戳
import time
timeStamp = 1557502800

timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)