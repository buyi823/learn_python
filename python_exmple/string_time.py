#!/usr/bin/python3
# 将字符串的时间转换为时间戳

import time

a1 = "2019-5-10 23:40:00"
# 先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")  # 根据指定的格式把一个时间字符串解析为时间元组

# 转换为时间戳
# mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。
# 如果输入的值不是一个合法的时间，将触发 OverflowError 或 ValueError。
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

# 格式转换 - 转为 /
a2 = "2019/5/10 23:40:00"
#先转换为时间数组,然后转换为其他格式
# timeArray = time.strptime(a2, "%Y-%m-%d %H:%M:%S")
# time strftime()接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
# otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
# print(otherStyleTime)
# 注释掉的语句执行报错
"""
File "C:\Program Files\Python36\lib\_strptime.py", line 559, in _strptime_time
    tt = _strptime(data_string, format)[0]
  File "C:\Program Files\Python36\lib\_strptime.py", line 362, in _strptime
    (data_string, format))
ValueError: time data '2019/5/10 23:40:00' does not match format '%Y-%m-%d %H:%M:%S'
"""