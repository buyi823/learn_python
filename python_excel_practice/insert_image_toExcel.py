#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-22 17:23
# insert image 

import xlsxwriter, time

xlsx_book = xlsxwriter.Workbook('insertImageToExcel_' + time.strftime("%Y%m%d%H%M%S") + '.xlsx')
xlsx_sheet = xlsx_book.add_worksheet('test insert image')
xlsx_sheet.insert_image('A1', 'xlwt_colour__number_code.png')
xlsx_book.close() 
print('done')