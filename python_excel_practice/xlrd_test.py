#!/usr/bin/python3
import xlrd
# from openpyxl import load_workbook
data = xlrd.open_workbook("F:\\version\\test_excel.xlsx")
# 这里，需要在读取文件的时候添加个参数，将formatting_info参数设置为True，默认是False，否
# 则可能调用merged_cells属性获取到的是空值。

#workbook = load_workbook("F:\\version\\test_excel.xlsx")
#sheet1 = workbook['test1']
sheet1 = data.sheet_by_name('test1')
print(sheet1)

#获取整行和整列的值（返回数组）
print(sheet1.row_values(0))
print(sheet1.col_values(1))

# 获取行数和列数
print(sheet1.nrows)
print(sheet1.ncols)

# 获取单元格
print(sheet1.cell(1,1).value)
print(sheet1.cell(3,4).value)
