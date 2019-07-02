#!/usr/bin/python3
import xlrd, xlwt
"""
Python中xlrd和xlwt模块使用方法
xlrd模块实现对excel文件内容读取，xlwt模块实现对excel文件的写入。
"""

# 打开Excel文件读取数据
data = xlrd.open_workbook('F:\\version\\test_excel.xlsx')
sheet_name = data.sheet_names() # 获取所有sheet名称
print(sheet_name)

# 根据下标获取sheet名称
sheet2_name = data.sheet_names()[1]
print(sheet2_name)

# 根据sheet索引或者名称获取sheet内容，同时获取sheet名称、行数、列数
sheet1 = data.sheet_by_index(0)
print('sheet1名称：{}\nsheet1列数：{}\nsheet1行数：{}'.format(sheet1.name, sheet1.ncols, sheet1.nrows))

sheet2 = data.sheet_by_name("test2")
print('sheet2名称：{}\nsheet2行数：{}'.format(sheet2.name, sheet2.ncols, sheet2.nrows))

# 根据sheet名称获取整行和整列的值
sheet1 = data.sheet_by_name('test1')
print(sheet1.row_values(3))
print(sheet1.col_values(3))

# 获取指定单元格的内容
print(sheet1.cell(1,0).value) # 第2 行1列内容
print(sheet1.cell_value(1,0)) # 第2 行1列内容
print(sheet1.row(1)[0].value) # 第2 行1列内容

# 获取单元格内容的数据类型
# 说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print(sheet1.cell(1,0).ctype) # 第2行1列的内容的数据类型
print(sheet1.cell(3,0).ctype)
print(sheet1.cell(1,5).ctype)
print(sheet1.cell(4,3).ctype)



 