#!/usr/bin/python3
import xlwt
from datetime import datetime,date

def set_style(name, height, bold=False, format_str=''):
    style = xlwt.XFStyle() #初始化样式

    font = xlwt.Font() #为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.height = height

    borders = xlwt.Borders() # 为样式创建边框
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders
    style.num_format_str = format_str

    return style

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet') # add a sheet
ws.col(0).width = 200*30 #设置第一列列宽

ws.write(0, 0, 1234.56, set_style('Times New Roman', 220, bold=True, format_str='#,##0.00'))
ws.write(1,0, datetime.now(),set_style('Times New Roman', 220, bold=False, format_str='DD-MM-YYYY'))

styleOK = xlwt.easyxf('pattern: fore_colour light_blue;'
                          'font: colour green, bold True;')

pattern = xlwt.Pattern() # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['red'] # 背景颜色

styleOK.pattern = pattern
ws.write(2,0,1,style=styleOK)
ws.write(2,1,1)
ws.write(2,2,xlwt.Formula("A3+B3"))

wb.save('example.xls')