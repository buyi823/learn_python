#!/usr/bin/python3

import calendar
monthRange = calendar.monthrange(2019, 7)
# 　返回两个整数组成的元组，第一个是该月的第一天是星期几，第二个是该月的天数。
# ps：此处计算星期几是按照星期一为0计算。
print(monthRange)
