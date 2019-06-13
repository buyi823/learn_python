#!/usr/bin/python3
# 计算几天前并转换为指定格式。

import time
import datetime

timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAge = dateArray = datetime.timedelta(days = 3)
print(threeDayAge)