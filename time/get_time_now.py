#!/usr/bin/python3
import time

ticks = time.time()
print("当前时间戳为：", ticks)
# 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。
# 太遥远的日期也不行，UNIX和Windows只支持到2038年。

localtime = time.localtime(time.time())
print("本地时间：", localtime)

localtime1 = time.asctime(time.localtime(time.time()))
print("格式化后的本地时间：", localtime1)