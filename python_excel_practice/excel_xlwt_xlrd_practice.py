#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-18 16:03
# excel practice
# Update 2021-11-22 14:00 
# 搞明白怎么操作了，循环写入那块应该可以使用其他方法实现，写了3个循环，感觉傻傻的
# 另外如何将另一个函数中输出的结果写入excel，而不是先定义列表，这个还是没想明白

import xlwt
import time


def title_style():
    # define font
    font = xlwt.Font()
    font.name = 'Calibri'
    font.bold = True
    font.colour_index = 1 # 1 white color
    font.height =  20 * 16 # 20为衡量单位，16是字号
    
    # define alignment
    alignment = xlwt.Alignment()
    # 0x01 align left   0x02 水平方向居中    0x03 align right
    alignment.horz = 0x02
    # 0x00 上端对其  0x01 垂直方向居中   0x02 底端对齐
    alignment.vert = 0x01
    
    # define borders
    borders = xlwt.Borders()
    # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
    # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
    borders.top = 1
    borders.bottom = 1
    borders.left = 1
    borders.right = 1
    # borders colour
    borders.top_colour = 8
    borders.bottom_colour = 8
    borders.left_colour = 8
    borders.right_colour = 8
    
    # define background colour
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 18
    
    # init style
    my_title_style = xlwt.XFStyle()
    my_title_style.font = font
    my_title_style.alignment = alignment
    my_title_style.borders = borders
    my_title_style.pattern = pattern
        
    return my_title_style


def content_sytle():
    font = xlwt.Font()
    font.name = 'Calibri'
    font.bold = False
    font.colour_index = 0 # 1 black color
    font.height =  20 * 12 # 20为衡量单位，16是字号
    
    # define alignment
    alignment = xlwt.Alignment()
    # 0x01 align left   0x02 水平方向居中    0x03 align right
    alignment.horz = 0x02
    # 0x00 上端对其  0x01 垂直方向居中   0x02 底端对齐
    alignment.vert = 0x01
    
    # define borders
    borders = xlwt.Borders()
    # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
    # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
    borders.top = 1
    borders.bottom = 1
    borders.left = 1
    borders.right = 1
    # borders colour
    borders.top_colour = 8
    borders.bottom_colour = 8
    borders.left_colour = 8
    borders.right_colour = 8
    
    my_content_style = xlwt.XFStyle()
    my_content_style.font = font
    my_content_style.alignment = alignment
    my_content_style.borders = borders
    
    return my_content_style  
    
if __name__ == '__main__':
    
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Blaine\'s sheet', cell_overwrite_ok=True) 
        
    title_content =  ['Number', 'Name', 'DOB', 'Team'] 
    row1 = ['1', 'Michael Jordan', '1963-2-16', 'Bulls']
    row2 = ['2', 'Kobe Bryant', '1978-8-23', 'Lakers']
    
    titleStyle = title_style()
    contentStyle = content_sytle()
    sheet.col(0).width = 15 *256 # 第一列纯数字列宽小一点
   
    # 生成标题
    for i in range(len(title_content)):
        # 设置列宽，一个中文等于两个英文等于两个字符，20为字符数，256为衡量单位
        sheet.col(i+1).width = 30 *256
        sheet.write(0, i, title_content[i], titleStyle)   
    
    # 从第二行开写入内容
    for i in range(len(row1)):
        sheet.write(1, i, row1[i], contentStyle)
        
    for i in range(len(row2)):
        sheet.write(2, i, row2[i], contentStyle)   
    
    # 如何生成个数字连续的矩形，他奶奶的想不明白
    # for i in range(9):
    #     for j in range(8):
    #         sheet.write(3+i, j, j)      
     
    book.save('BlaineExcelPractice_' + time.strftime("%Y%m%d%H%M%S") + '.xls')
        
    print('done')