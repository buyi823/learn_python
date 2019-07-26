#!/usr/bin/python3

import time

# 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
print("time.altzone %d" % time.altzone)

# time.asctime([tupletime])
# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
t = time.localtime()
print("time.asctime(t): %s" % time.asctime(t))

print(time.perf_counter()) # 返回系统运行时间
# 返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。
print(time.process_time()) # 返回进程运行时间
# 返回当前进程执行 CPU 的时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。

print("time.ctime(): %s" % time.ctime())

print("Start: %s" % time.ctime())
time.sleep(5)
print("End: %s" % time.ctime())

struct_time = time.strptime("30 Nov 00", "%d %b %y")

print("返回元组：", struct_time)