#!/usr/bin/python3
from datetime import datetime,date
import xlrd

data = xlrd.open_workbook('F:\\version\\test_excel.xlsx')

sheet1 = data.sheet_by_index(0)
if sheet1.cell(1,5).ctype == 3:
    print(sheet1.cell(1,5).value)
    date_value = xlrd.xldate_as_tuple(sheet1.cell(1,5).value, datemode=0)
    #d是从excel中读取出来的浮点数
    # xldate_as_tuple(d,0)
    # xldate_as_tuple第二个参数有两种取值，0或者1，0是以1900-01-01为基准的日期，而1是1904-01-01为基准的日期。
    # 该函数返回的是一个元组，他的值类似：(year, month, day, hour, minute, nearest_second)
    print(date_value)
    print(date(*date_value[:3]))
    print(date(*date_value[:3]).strftime('%y%m%d'))

if sheet1.cell(1,9).ctype == 2:
    print(sheet1.cell(1,9).value)
    num_value = int(sheet1.cell(1,9).value)
    print(num_value)

