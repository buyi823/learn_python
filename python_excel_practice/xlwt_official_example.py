#usr/bin/python3
# xlwt 官方的例子
from time import *
from xlwt.Workbook import *
from xlwt.Style import *

style = XFStyle()
wb = Workbook()
ws0 = wb.add_sheet('0')
colcount = 200 + 1
rowcount = 6000 + 1
t0 = time()
print("\nstart: %s" % ctime(t0))
print("Filling...")
for col in xrange(colcount):
    print("[%d]" % col, end=' ') 
    for row in xrange(rowcount):
        ws0.write(row, col, "BIG")
t1 = time() - t0
print("\nsince starting elapsed %.2f s" % (t1))
print("Storing...")
wb.save('.//xlwt_official_exmple//big-16Mb.xls')
t2 = time() - t0
print("since starting elapsed %.2f s" % (t2))

from xlwt import *
font0 = Font()
font0.name = 'Times New Roman'
font0.struck_out = True
font0.bold = True
style0 = XFStyle()
style0.font = font0

wb = Workbook()
ws0 = wb.add_sheet('0')
ws0.write(1, 1, 'Test', style0)
for i in range(0, 0x53):
    borders = Borders()
    borders.left = i
    borders.right = i
    borders.top = i
    borders.bottom = i
    style = XFStyle()
    style.borders = borders
    ws0.write(i, 2, '', style)
    ws0.write(i, 3, hex(i), style0)
ws0.write_merge(5, 8, 6, 10, "")
wb.save('.//xlwt_official_exmple//blanks.xls')
from xlwt import *

w = Workbook()
ws = w.add_sheet('Hey, Dude')
for i in range(6, 80):
    fnt = Font()
    fnt.height = i*20
    style = XFStyle()
    style.font = fnt
    ws.write(1, i, 'Test')
    ws.col(i).width = 0x0d00 + i
w.save('.//xlwt_official_exmple//col_width.xls')
from xlwt import *
from datetime import datetime

w = Workbook()
ws = w.add_sheet('Hey, Dude')

fmts = [
    'M/D/YY',
    'D-MMM-YY',
    'D-MMM',
    'MMM-YY',
    'h:mm AM/PM',
    'h:mm:ss AM/PM',
    'h:mm',
    'h:mm:ss',
    'M/D/YY h:mm',
    'mm:ss',
    '[h]:mm:ss',
    'mm:ss.0',
]

i = 0
for fmt in fmts:
    ws.write(i, 0, fmt)
    style = XFStyle()
    style.num_format_str = fmt
    ws.write(i, 4, datetime.now(), style)
    i += 1
w.save('.//xlwt_official_exmple//dates.xls')
from xlwt import *

font0 = Font()
font0.name = 'Times New Roman'
font0.struck_out = True
font0.bold = True

style0 = XFStyle()
style0.font = font0


wb = Workbook()
ws0 = wb.add_sheet('0')

ws0.write(1, 1, 'Test', style0)

for i in range(0, 0x53):
    fnt = Font()
    fnt.name = 'Arial'
    fnt.colour_index = i
    fnt.outline = True

    borders = Borders()
    borders.left = i

    style = XFStyle()
    style.font = fnt
    style.borders = borders

    ws0.write(i, 2, 'colour', style)
    ws0.write(i, 3, hex(i), style0)


wb.save('.//xlwt_official_exmple//format.xls')
from xlwt import *

w = Workbook()
ws = w.add_sheet('F')

ws.write(0, 0, Formula("-(1+1)"))
ws.write(1, 0, Formula("-(1+1)/(-2-2)"))
ws.write(2, 0, Formula("-(134.8780789+1)"))
ws.write(3, 0, Formula("-(134.8780789e-10+1)"))
ws.write(4, 0, Formula("-1/(1+1)+9344"))

ws.write(0, 1, Formula("-(1+1)"))
ws.write(1, 1, Formula("-(1+1)/(-2-2)"))
ws.write(2, 1, Formula("-(134.8780789+1)"))
ws.write(3, 1, Formula("-(134.8780789e-10+1)"))
ws.write(4, 1, Formula("-1/(1+1)+9344"))

ws.write(0, 2, Formula("A1*B1"))
ws.write(1, 2, Formula("A2*B2"))
ws.write(2, 2, Formula("A3*B3"))
ws.write(3, 2, Formula("A4*B4*sin(pi()/4)"))
ws.write(4, 2, Formula("A5%*B5*pi()/1000"))
ws.write(5, 2, Formula("C1+C2+C3+C4+C5/(C1+C2+C3+C4/(C1+C2+C3+C4/(C1+C2+C3+C4)+C5)+C5)-20.3e-2"))
ws.write(5, 3, Formula("C1^2"))
ws.write(6, 2, Formula("SUM(C1;C2;;;;;C3;;;C4)"))
ws.write(6, 3, Formula("SUM($A$1:$C$5)"))

ws.write(7, 0, Formula('"lkjljllkllkl"'))
ws.write(7, 1, Formula('"yuyiyiyiyi"'))
ws.write(7, 2, Formula('A8 & B8 & A8'))
ws.write(8, 2, Formula('now()'))

ws.write(10, 2, Formula('TRUE'))
ws.write(11, 2, Formula('FALSE'))
ws.write(12, 3, Formula('IF(A1>A2;3;"hkjhjkhk")'))

w.save('.//xlwt_official_exmple//formulas.xls')
from xlwt import *

f = Font()
f.height = 20*72
f.name = 'Verdana'
f.bold = True
f.underline = Font.UNDERLINE_DOUBLE
f.colour_index = 4

h_style = XFStyle()
h_style.font = f

w = Workbook()
ws = w.add_sheet('F')
n = "HYPERLINK"
ws.write_merge(1, 1, 1, 10, Formula(n + '("http://www.irs.gov/pub/irs-pdf/f1000.pdf";"f1000.pdf")'), h_style)
ws.write_merge(2, 2, 2, 25, Formula(n + '("mailto:roman.kiseliov@gmail.com?subject=pyExcelerator-feedback&Body=Hello,%20Roman!";"pyExcelerator-feedback")'), h_style)
w.save(".//xlwt_official_exmple//hyperlinks.xls")
from xlwt import *

fnt = Font()
fnt.name = 'Arial'
fnt.colour_index = 4
fnt.bold = True

borders = Borders()
borders.left = 6
borders.right = 6
borders.top = 6
borders.bottom = 6
al = Alignment()
al.horz = Alignment.HORZ_CENTER
al.vert = Alignment.VERT_CENTER
style = XFStyle()
style.font = fnt
style.borders = borders
style.alignment = al
wb = Workbook()
ws0 = wb.add_sheet('sheet0')
ws1 = wb.add_sheet('sheet1')
ws2 = wb.add_sheet('sheet2')
for i in range(0, 0x200, 2):
    ws0.write_merge(i, i+1, 1, 5, 'test %d' % i, style)
    ws1.write_merge(i, i, 1, 7, 'test %d' % i, style)
    ws2.write_merge(i, i+1, 1, 7 + (i%10), 'test %d' % i, style)
wb.save('.//xlwt_official_exmple//merged.xls')
import xlwt
book = xlwt.Workbook()
for magn in (0, 60, 100, 75, 150):
    for preview in (False, True):
        sheet = book.add_sheet('magn%d%s' % (magn, "np"[preview]))
        if preview:
            sheet.preview_magn = magn
        else:
            sheet.normal_magn = magn
        sheet.page_preview = preview
        for rowx in range(100):
            sheet.write(rowx, 0, "Some text")
book.save(".//xlwt_official_exmple//zoom_magnification.xls")
import xlwt
import datetime
ezxf = xlwt.easyxf
def write_xls(file_name, sheet_name, headings, data, heading_xf, data_xfs):
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheet_name)
    rowx = 0
    for colx, value in enumerate(headings):
        sheet.write(rowx, colx, value, heading_xf)
    sheet.set_panes_frozen(True) # frozen headings instead of split panes
    sheet.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
    sheet.set_remove_splits(True) # if user does unfreeze, don't leave a split there
    for row in data:
        rowx += 1
        for colx, value in enumerate(row):
            sheet.write(rowx, colx, value, data_xfs[colx])
    book.save(file_name)

if __name__ == '__main__':
    import sys
    mkd = datetime.date
    hdngs = ['Date', 'Stock Code', 'Quantity', 'Unit Price', 'Value', 'Message']
    kinds =  'date    text          int         price         money    text'.split()
    data = [
        [mkd(2007, 7, 1), 'ABC', 1000, 1.234567, 1234.57, ''],
        [mkd(2007, 12, 31), 'XYZ', -100, 4.654321, -465.43, 'Goods returned'],
        ] + [
            [mkd(2008, 6, 30), 'PQRCD', 100, 2.345678, 234.57, ''],
        ] * 100

    heading_xf = ezxf('font: bold on; align: wrap on, vert centre, horiz center')
    kind_to_xf_map = {
        'date': ezxf(num_format_str='yyyy-mm-dd'),
        'int': ezxf(num_format_str='#,##0'),
        'money': ezxf('font: italic on; pattern: pattern solid, fore-colour grey25',
            num_format_str='$#,##0.00'),
        'price': ezxf(num_format_str='#0.000000'),
        'text': ezxf(),
        }
    data_xfs = [kind_to_xf_map[k] for k in kinds]
    write_xls('.//xlwt_official_exmple//xlwt_easyxf_simple_demo.xls', 'Demo', hdngs, data, heading_xf, data_xfs)
    from xlwt import *
w = Workbook()
ws = w.add_sheet('Hey, Dude')
for i in range(6, 80):
    fnt = Font()
    fnt.height = i*20
    style = XFStyle()
    style.font = fnt
    ws.write(i, 1, 'Test')
    ws.row(i).set_style(style)
w.save('.//xlwt_official_exmple//row_styles.xls')
from xlwt import *

fnt = Font()
fnt.name = 'Arial'
fnt.colour_index = 4
fnt.bold = True

borders = Borders()
borders.left = 6
borders.right = 6
borders.top = 6
borders.bottom = 6

style = XFStyle()
style.font = fnt
style.borders = borders

wb = Workbook()

ws0 = wb.add_sheet('Rows Outline')

ws0.write_merge(1, 1, 1, 5, 'test 1', style)
ws0.write_merge(2, 2, 1, 4, 'test 1', style)
ws0.write_merge(3, 3, 1, 3, 'test 2', style)
ws0.write_merge(4, 4, 1, 4, 'test 1', style)
ws0.write_merge(5, 5, 1, 4, 'test 3', style)
ws0.write_merge(6, 6, 1, 5, 'test 1', style)
ws0.write_merge(7, 7, 1, 5, 'test 4', style)
ws0.write_merge(8, 8, 1, 4, 'test 1', style)
ws0.write_merge(9, 9, 1, 3, 'test 5', style)

ws0.row(1).level = 1
ws0.row(2).level = 1
ws0.row(3).level = 2
ws0.row(4).level = 2
ws0.row(5).level = 2
ws0.row(6).level = 2
ws0.row(7).level = 2
ws0.row(8).level = 1
ws0.row(9).level = 1


ws1 = wb.add_sheet('Columns Outline')

ws1.write_merge(1, 1, 1, 5, 'test 1', style)
ws1.write_merge(2, 2, 1, 4, 'test 1', style)
ws1.write_merge(3, 3, 1, 3, 'test 2', style)
ws1.write_merge(4, 4, 1, 4, 'test 1', style)
ws1.write_merge(5, 5, 1, 4, 'test 3', style)
ws1.write_merge(6, 6, 1, 5, 'test 1', style)
ws1.write_merge(7, 7, 1, 5, 'test 4', style)
ws1.write_merge(8, 8, 1, 4, 'test 1', style)
ws1.write_merge(9, 9, 1, 3, 'test 5', style)

ws1.col(1).level = 1
ws1.col(2).level = 1
ws1.col(3).level = 2
ws1.col(4).level = 2
ws1.col(5).level = 2
ws1.col(6).level = 2
ws1.col(7).level = 2
ws1.col(8).level = 1
ws1.col(9).level = 1


ws2 = wb.add_sheet('Rows and Columns Outline')

ws2.write_merge(1, 1, 1, 5, 'test 1', style)
ws2.write_merge(2, 2, 1, 4, 'test 1', style)
ws2.write_merge(3, 3, 1, 3, 'test 2', style)
ws2.write_merge(4, 4, 1, 4, 'test 1', style)
ws2.write_merge(5, 5, 1, 4, 'test 3', style)
ws2.write_merge(6, 6, 1, 5, 'test 1', style)
ws2.write_merge(7, 7, 1, 5, 'test 4', style)
ws2.write_merge(8, 8, 1, 4, 'test 1', style)
ws2.write_merge(9, 9, 1, 3, 'test 5', style)

ws2.row(1).level = 1
ws2.row(2).level = 1
ws2.row(3).level = 2
ws2.row(4).level = 2
ws2.row(5).level = 2
ws2.row(6).level = 2
ws2.row(7).level = 2
ws2.row(8).level = 1
ws2.row(9).level = 1

ws2.col(1).level = 1
ws2.col(2).level = 1
ws2.col(3).level = 2
ws2.col(4).level = 2
ws2.col(5).level = 2
ws2.col(6).level = 2
ws2.col(7).level = 2
ws2.col(8).level = 1
ws2.col(9).level = 1


ws0.protect = True
ws0.wnd_protect = True
ws0.obj_protect = True
ws0.scen_protect = True
ws0.password = "123456"

ws1.protect = True
ws1.wnd_protect = True
ws1.obj_protect = True
ws1.scen_protect = True
ws1.password = "abcdefghij"

ws2.protect = True
ws2.wnd_protect = True
ws2.obj_protect = True
ws2.scen_protect = True
ws2.password = "ok"

wb.protect = True
wb.wnd_protect = True
wb.obj_protect = True
wb.save('.//xlwt_official_exmple//protection.xls')
from xlwt import Workbook
from xlwt.BIFFRecords import PanesRecord
w = Workbook()

# do each of the 4 scenarios with each of the 4 possible
# active pane settings

for px,py in (
    (0,0),   # no split
    (0,10),  # horizontal split
    (10,0),  # vertical split
    (10,10), # both split
    ):
    
    for active in range(4):

        # 0 - logical bottom-right pane
        # 1 - logical top-right pane
        # 2 - logical bottom-left pane
        # 3 - logical top-left pane

        # only set valid values:
        if active not in PanesRecord.valid_active_pane.get(
            (int(px > 0),int(py > 0))
            ):
            continue

        sheet = w.add_sheet('px-%i py-%i active-%i' %(
                px,py,active
                ))

        for rx in range(20):
            for cx in range(20):
                sheet.write(rx,cx,'R%iC%i'%(rx,cx))

        sheet.panes_frozen = False
        sheet.vert_split_pos = px * 8.43
        sheet.horz_split_pos = py * 12.75
        sheet.active_pane = active

w.save('.//xlwt_official_exmple//panes3.xls')
import xlwt

w = xlwt.Workbook()
sheets = [w.add_sheet('sheet ' + str(sheetx+1)) for sheetx in range(7)]
ws1, ws2, ws3, ws4, ws5, ws6, ws7 = sheets
for sheet in sheets:
    for i in range(0x100):
        sheet.write(i // 0x10, i % 0x10, i)

H = 1
V = 2
HF = H + 2
VF = V + 2

ws1.panes_frozen = True
ws1.horz_split_pos = H
ws1.horz_split_first_visible = HF

ws2.panes_frozen = True
ws2.vert_split_pos = V
ws2.vert_split_first_visible = VF

ws3.panes_frozen = True
ws3.horz_split_pos = H
ws3.vert_split_pos = V
ws3.horz_split_first_visible = HF
ws3.vert_split_first_visible = VF

H = 10
V = 12
HF = H + 2
VF = V + 2

ws4.panes_frozen = False
ws4.horz_split_pos = H * 12.75 # rows
ws4.horz_split_first_visible = HF

ws5.panes_frozen = False
ws5.vert_split_pos = V * 8.43 # rows
ws5.vert_split_first_visible = VF

ws6.panes_frozen = False
ws6.horz_split_pos = H * 12.75 # rows
ws6.horz_split_first_visible = HF
ws6.vert_split_pos = V * 8.43 # cols
ws6.vert_split_first_visible = VF

ws7.split_position_units_are_twips = True
ws7.panes_frozen = False
ws7.horz_split_pos = H * 250 + 240 # twips
ws7.horz_split_first_visible = HF
ws7.vert_split_pos = V * 955 + 410 # twips
ws7.vert_split_first_visible = VF

w.save('.//xlwt_official_exmple//panes2.xls')
from xlwt import *

wb = Workbook()
ws0 = wb.add_sheet('sheet0')

fnt1 = Font()
fnt1.name = 'Verdana'
fnt1.bold = True
fnt1.height = 18*0x14

pat1 = Pattern()
pat1.pattern = Pattern.SOLID_PATTERN
pat1.pattern_fore_colour = 0x16

brd1 = Borders()
brd1.left = 0x06
brd1.right = 0x06
brd1.top = 0x06
brd1.bottom = 0x06

fnt2 = Font()
fnt2.name = 'Verdana'
fnt2.bold = True
fnt2.height = 14*0x14

brd2 = Borders()
brd2.left = 0x01
brd2.right = 0x01
brd2.top = 0x01
brd2.bottom = 0x01

pat2 = Pattern()
pat2.pattern = Pattern.SOLID_PATTERN
pat2.pattern_fore_colour = 0x01F

fnt3 = Font()
fnt3.name = 'Verdana'
fnt3.bold = True
fnt3.italic = True
fnt3.height = 12*0x14

brd3 = Borders()
brd3.left = 0x07
brd3.right = 0x07
brd3.top = 0x07
brd3.bottom = 0x07

fnt4 = Font()

al1 = Alignment()
al1.horz = Alignment.HORZ_CENTER
al1.vert = Alignment.VERT_CENTER

al2 = Alignment()
al2.horz = Alignment.HORZ_RIGHT
al2.vert = Alignment.VERT_CENTER

al3 = Alignment()
al3.horz = Alignment.HORZ_LEFT
al3.vert = Alignment.VERT_CENTER

style1 = XFStyle()
style1.font = fnt1
style1.alignment = al1
style1.pattern = pat1
style1.borders = brd1

style2 = XFStyle()
style2.font = fnt2
style2.alignment = al1
style2.pattern = pat2
style2.borders = brd2

style3 = XFStyle()
style3.font = fnt3
style3.alignment = al1
style3.pattern = pat2
style3.borders = brd3

price_style = XFStyle()
price_style.font = fnt4
price_style.alignment = al2
price_style.borders = brd3
price_style.num_format_str = '_(#,##0.00_) "money"'

ware_style = XFStyle()
ware_style.font = fnt4
ware_style.alignment = al3
ware_style.borders = brd3


ws0.merge(3, 3, 1, 5, style1)
ws0.merge(4, 10, 1, 6, style2)
ws0.merge(14, 16, 1, 7, style3)
ws0.col(1).width = 0x0d00


wb.save('.//xlwt_official_exmple//merged1.xls')

from xlwt import *

w = Workbook()
ws = w.add_sheet('Hey, Dude')

fmts = [
    'general',
    '0',
    '0.00',
    '#,##0',
    '#,##0.00',
    '"$"#,##0_);("$"#,##',
    '"$"#,##0_);[Red]("$"#,##',
    '"$"#,##0.00_);("$"#,##',
    '"$"#,##0.00_);[Red]("$"#,##',
    '0%',
    '0.00%',
    '0.00E+00',
    '# ?/?',
    '# ??/??',
    'M/D/YY',
    'D-MMM-YY',
    'D-MMM',
    'MMM-YY',
    'h:mm AM/PM',
    'h:mm:ss AM/PM',
    'h:mm',
    'h:mm:ss',
    'M/D/YY h:mm',
    '_(#,##0_);(#,##0)',
    '_(#,##0_);[Red](#,##0)',
    '_(#,##0.00_);(#,##0.00)',
    '_(#,##0.00_);[Red](#,##0.00)',
    '_("$"* #,##0_);_("$"* (#,##0);_("$"* "-"_);_(@_)',
    '_(* #,##0_);_(* (#,##0);_(* "-"_);_(@_)',
    '_("$"* #,##0.00_);_("$"* (#,##0.00);_("$"* "-"??_);_(@_)',
    '_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)',
    'mm:ss',
    '[h]:mm:ss',
    'mm:ss.0',
    '##0.0E+0',
    '@'   
]

i = 0
for fmt in fmts:
    ws.write(i, 0, fmt)

    style = XFStyle()
    style.num_format_str = fmt

    ws.write(i, 4, -1278.9078, style)

    i += 1

w.save('.//xlwt_official_exmple//num_formats.xls')