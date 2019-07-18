#!/usr/bin/python3

import xlwt
from datetime import datetime, date
 
 
def set_style(name, height, bold=False, format_str='',align='center'):
    style = xlwt.XFStyle()  # 初始化样式
 
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.height = height
 
    borders = xlwt.Borders()  # 为样式创建边框
    borders.left = 2
    borders.right = 2
    borders.top = 0
    borders.bottom = 2
 
    alignment = xlwt.Alignment()  # 设置排列
    if align== 'center':
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
    else:
        alignment.horz = xlwt.Alignment.HORZ_LEFT
        alignment.vert = xlwt.Alignment.VERT_BOTTOM
 
    style.font = font
    style.borders = borders
    style.num_format_str = format_str
    style.alignment = alignment
 
    return style
 
 
wb = xlwt.Workbook()
ws = wb.add_sheet('联系人',cell_overwrite_ok=True)  # 增加sheet
rows = ['机构名称', '姓名', '部门', '电话', '入职日期', '手机', '邮箱']
col1 = ['王1', '王2', '王3']
col2 = ['666', '777','888']
col3 = ['2014-08-09','2014-08-11','2015-08-09']
# 写第一行数据
ws.write_merge(
    0,
    0,
    0,
    6,
    '联系人表',
    set_style(
        'Times New Roman',
        320,
        bold=True,
        format_str=''))  # 合并单元格
 
styleOK = xlwt.easyxf()
 
pattern = xlwt.Pattern()  # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 背景颜色
 
borders = xlwt.Borders()  # 为样式创建边框
borders.left = 2
borders.right = 2
borders.top = 6
borders.bottom = 2
 
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True
font.height = 220
 
styleOK.pattern = pattern
styleOK.borders = borders
styleOK.font = font
 
# 写第二行数据
for index, val in enumerate(rows):
    ws.col(index).width = 150 * 30 # 定义列宽
    ws.write(1, index, val, style=styleOK)
 
# 写第3行-6行第一列数据
ws.write_merge(
    2,
    2 + len(col1)-1,
    0,
    0,
    'x机构',
    set_style(
        'Times New Roman',
        320,
        bold=True,
        format_str=''))  # 合并单元格
 
# 从第3行开始写1列数据
for index, val in enumerate(col1):
    ws.col(1).width = 150 * 30 # 定义列宽
    ws.write(index+2, 1, val, style=set_style('Times New Roman',
        200,
        bold=False,
        format_str='',align=''))
 
# 从第3行开始写4列数据
for index, val in enumerate(col2):
    ws.col(3).width = 150 * 30 # 定义列宽
    ws.write(index+2, 3, val, style=set_style('Times New Roman',
        200,
        bold=False,
        format_str='',align=''))
 
 
# 从第3行开始写5列数据
for index, val in enumerate(col3):
    ws.col(4).width = 150 * 30 # 定义列宽
    ws.write(index+2, 4, val, style=set_style('Times New Roman',
        200,
        bold=False,
        format_str='',align=''))
 
ws.write(4, 2,'技术部', style=styleOK)
ws.write(4, 5,'186777233', style=styleOK)
ws.write(4, 6,'wang@166.com', style=styleOK)
wb.save('test.xls')   # 保存xls