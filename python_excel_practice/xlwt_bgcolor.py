#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-22 16:04
# 生成不同的背景色

import xlwt, time

# 不知道怎么能换行生成个矩形

# 这个函数是为了测试不同的背景颜色
def backgound_color():
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('backgroundColor', cell_overwrite_ok=True)
    i = 0
    while i < 73:
        font = xlwt.Font()
        font.name = 'Calibri'
        font.bold = True
        font.colour_index = 1 # 1 white color
        font.height =  20 * 12
        
        alignment = xlwt.Alignment()
        # 0x01 align left   0x02 水平方向居中    0x03 align right
        alignment.horz = 0x02
        # 0x00 上端对其  0x01 垂直方向居中   0x02 底端对齐
        alignment.vert = 0x01
        
        borders = xlwt.Borders()
        # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
        # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
        borders.top = 2
        borders.bottom = 2
        borders.left = 2
        borders.right = 2
        borders.top_colour = 8
        borders.bottom_colour = 8
        borders.left_colour = 8
        borders.right_colour = 8
        
        # define background colour
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = i
        
        # init style
        my_background_color = xlwt.XFStyle()
        my_background_color.font = font
        my_background_color.alignment = alignment
        my_background_color.borders = borders
        my_background_color.pattern = pattern 
        
        # 背景颜色
        sheet.write(i, 0, i, my_background_color)
               
        i += 1
        
    book.save('backgroundColor_' + time.strftime("%Y%m%d%H%M%S") + '.xls')
        

backgound_color()
print('done')