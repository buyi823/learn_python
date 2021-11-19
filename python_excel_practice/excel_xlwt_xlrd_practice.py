#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-18 16:03
# excel practice

import xlwt
import os

from xlwt.Workbook import Workbook
from xlwt.Worksheet import Worksheet


def set_style(fontName, fontHeight, fontBold):
    # Init style
    style = xlwt.XFStyle()
    # Create font for style
    font = xlwt.Font()
    font.name = fontName
    font.height = fontHeight
    font.bold = fontBold
    font.colour_index = 1
    
    bg = xlwt.Pattern()
    bg.pattern = xlwt.Pattern.SOLID_PATTERN
    bg.pattern_fore_colour = 9
    
    # 不知道怎么弄
    # style0 = xlwt.XFStyle()
    # style0.font = font

    
    return style

def write_excel():
    workbook = xlwt.Workbook(encoding='utf-8')
    work_sheet = workbook.add_sheet('Blaine worksheet')
    row0 = ['Number', 'Name', 'DOB', 'Team'] 
    row1 = ['1', 'Michael Jordan', '1963-2-16', 'Bulls']
    row2 = ['2', 'Kobe Bryant', '1978-8-23', 'Lakers']
    
    for i in range(len(row0)):
        # 不带set_style可以成功写入，带上不行，卧槽
        work_sheet.write(0, i, row0[i], set_style('Calibri', 220, True))
        work_sheet.write(1, i, row1[i], set_style('Calibri', 220, True))
        work_sheet.write(2, i, row2[i], set_style('Calibri', 220, True))
        # work_sheet.write(0, i, row0[i])
        # work_sheet.write(1, i, row1[i])
        # work_sheet.write(2, i, row2[i])
        
    workbook.save('BlaineTest.xls')
    
if __name__ == '__main__':
        
    write_excel()
    print('done')