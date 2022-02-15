#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-19 11:38
# xlwt xlrd practice

import xlwt
from xlwt.Workbook import Workbook
import xlrd

data = [
    ('有', '人', '云', '淡', '风', '轻'),
    ('有', '人', '负', '重', '前', '行'),
    ('p', 'y', 't', 'h', 'o', 'n')
]

output_file = 'blaineTest.xls'

def save_excel(target_list, output_file):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('test sheet')
    title_data = ('a', 'b', 'c', 'd', 'e', 'f')
    # 刚开始有点疑惑，Excel的标题也是数据的一部分
    # 这里其实是调用这个函数，会将data的传给target_list了；
    # 然后将标题title_data插入到target_list前面insert(index, obj)
    # 打印出来如下：
    # [('a', 'b', 'c', 'd', 'e', 'f'), ('有', '人', '云', '淡', '风', '轻'), ('有', '人', '负', '重', '前', '行'), ('p', 'y', 't', 'h', 'o', 'n')]
    target_list.insert(0, title_data)
    rows = len(target_list)
    lines = len(target_list[0])
    for i in range(rows):
        for j in range(lines):
            sheet.write(i, j, target_list[i][j])
    workbook.save(output_file)

save_excel(data, output_file)


intput_file = 'blaineTest.xls'

def read_excel(input_file):
    workbook = xlrd.open_workbook(input_file)
    print(workbook)
    # 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
    print(workbook.sheet_names())
    # 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('test sheet')
    print(table)
    rows = table.nrows
    cols = table.ncols
    # 可以通过row.values()按行获取数据，返回一个列表，也可以按列
    for row in range(rows):
        row_data = table.row_values(row)
        print(''.join(row_data))
    # 也可以根据单元格获取每一个单元格的数据
    for row in range(rows):
        for col in range(cols):
            data = table.cell(row, col).value
            print(data, end=' ')

read_excel(intput_file)
        
    
    
    