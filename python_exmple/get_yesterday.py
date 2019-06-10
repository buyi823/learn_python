#!/usr/bin/python3
# filename yesterday

import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)  #timedelta代表两个datetime之间的时间差
    yesterday = today - oneday
    return yesterday


#输出
print(getYesterday())
