#!/usr/bin/python3
import xlwt

def setup(self):
        if self.report.ftype == REPORT.XLS:
            font_h = xlwt.Font()
            font_h.bold = True
            style_h = xlwt.XFStyle()
            style_h.font = font_h

            self.xls_styles = {
                'datetime': xlwt.easyxf(num_format_str='D/M/YY h:mm'),
                'date': xlwt.easyxf(num_format_str='D/M/YY'),
                'time': xlwt.easyxf(num_format_str='h:mm'),
                'default': xlwt.Style.default_style,
                'bold': style_h
            }

            self.wb = xlwt.Workbook()
            self.ws = self.wb.add_sheet('Data')
            if self.make_sub_reports:
                self.section_ws = self.wb.add_sheet('Section') 