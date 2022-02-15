#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-19 17:15
# xlwt 字体大小颜色等

import patterns as patterns
import xlwt
import time

i = 0
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('test sheet', cell_overwrite_ok=True)

while i < 64:
    font = xlwt.Font()
    font.name = 'Calibri'
    font.colour_index = i
    # 字体大小，11是字号，20为衡量单位
    font.height = 20 * 11
    font.bold = False
    font.underline = True
    
    # 设置单元格对齐方式
    alignment = xlwt.Alignment()
    # 0x01 align left   0x02 水平方向居中    0x03 align right
    alignment.horz = 0x02
    # 0x00 上端对其  0x01 垂直方向居中   0x02 底端对齐
    alignment.vert = 0x01
    # 设置自动换行
    alignment.wrap = 1
    
    # 设置边框
    borders = xlwt.Borders()
    # 不同数字代表不同边框类型
    borders.left = 1
    borders.right = 2
    borders.top = 3
    borders.bottom = 4
    borders.left_colour = i
    borders.right_colour = i
    borders.top_colour = i
    borders.bottom_colour = i
    
    # 设置列宽，一个中文字符等于两个英文字符， 11为字符数，256为衡量单位
    sheet.col(1).width = 11 * 256
    
    # 设置背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = i
    
    # init style
    style0 = xlwt.XFStyle()
    style0.font = font
    
    style1 = xlwt.XFStyle()
    style1.pattern = pattern
    
    style2 = xlwt.XFStyle()
    style2.alignment = alignment
    
    style3 = xlwt.XFStyle()
    style3.borders = borders
    
    # 设置文字模式
    font.num_format_str = '#,##0.00'
    
    sheet.write(i, 0, u'字体', style0)
    sheet.write(i, 1, u'背景', style1)
    sheet.write(i, 2, u'对齐方式', style2)
    sheet.write(i, 3, u'边框', style3)
    
    # 合并单元格，合并第2行到第4行的第4列到第5列
    sheet.write_merge(2, 4, 4, 5, u'合并',style2)
    i = i + 1
    
book.save('test_file_' + time.strftime("%Y%m%d%H%M%S")+'.xls')
    
    