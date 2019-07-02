# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
import random
import re
from time import strftime, localtime, time
import xlrd, xlwt

# 系统团队成员名单----------------------------------------

NAME_LIST=['liuxiangtao','mazhansheng','lanxiangyu','fumiaomiao','fanxudong','xueguolei','wangyajie',
'suhanghang','wangsheng','sunyang']

def open_excel(file = r''):
    try:
        data = xlrd.open_workbook(file)
        print('data:',data)
        return data
    except Exception as e:
        print(str(e))

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='', colnameindex=1, by_index=0):
    data = open_excel(file)
    table = data.sheet_by_index(by_index) 
    print(data.sheet_names())
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    print(nrows,ncols)
    colnames = table.row_values(colnameindex) # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = []
            for i in range(len(colnames)):
                app.append(row[i])
            list.append(app)
    return list

def log_filtering(filtering_table=[], name_list=''):
    filered_list=[]
    filered_list.append(filtering_table[0]) # 添加一列标题栏
    for row in filtering_table:
        for name in name_list:
            if(row[2]==name):
                filered_list.append(now) # 将符合条件的Log记录筛选出来
                print('**********')
                for k in row:
                    print(k)
                print('**********')
                break  # 跳出namelist循环

for i in filered_list:
    print(i)
return filered_list

def set_style(name, height, bold=False):
    style = xlwt.Font() # 初始化样式
    font = xlwt.Font() # 为样式创建字体
    font.name = name  # Times New Roman
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style

def save_filered_list(filered_list=[], file_result='', commit_item_list=[]):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True) # 创建sheet
    style = xlwt.easyxf(u'align:wrap on, centre, horiz left;font: height 180, name 宋体; borders: top 1, bottom 1, left 1, right 1')

    for commit_item in commit_item_list:
        try:
            commit_item_index = filered_list[0].index(commit_item[0])
            sheet1.col(commit_item_index).width = commit_item[1]
        except ValueError as e: #获取对应value值的ID出错是，执行该操作
            print(e.message)
        print(commit_item)
    
    # 写入filered_list中的内容
    for i in range(len(filered_list)):
        if filered_list[i][0]==commit_item_list[0][0]:
            print_row = filered_list[i]
        else:
            print_row = filered_list[i]+['','','','']
        for j in range(len(print_row)):
            sheet1.write(i,j,print_row[j], style)
    
    f.save(file_result)
    pass

def SearchFile(FileType, SearchPath):
    print(SearchPath)
    for(dirpath, dirnames, filenames) in os.walk(SearchPath):
        for file in filenames:
            if re.math(FileType, file):
                TargetFile = os.path.join(dirpath, file)
                file_suffix = file.split('.')[1]
                print('------------------------')
                print('SearchFile', TargetFile)
                print('------------------------')
                return [TargetFile, dirpath, file, file_suffix]

def get_teamer_name(file_workspace):
    name_list=[]
    team_name_address = SearchFile('.*ame.*\.txt', file_workspace)[0]
    f = open(team_name_address, 'r+')
    for line in f.readlines():
        name_list.append(line.strip())
    f.close()
    print(name_list)
    return name_list

    #暂未使用的方法
    #将其中可用的commit-item项全部拿出来
def get_commit_item(commit_item_list=[]):
    commit_item_result=[]
    for item in commit_item_list:
        commit_item_result.append(item[0])
    return commit_item_result

#按commit_item_list中的commit-item项过滤其中的每一项
def filter_commit_content(filered_list=[],commit_item_list=[]):
    #获取commit_item_list中指定commit描述项的对应列数
    commit_item_filter_result=[]
    for commit_item in commit_item_list:
        try:
            commit_item_index = filered_list[0].index(commit_item[0])
            commit_item_filter_result.append(commit_item_index)
        except ValueError as e: # 获取对应value值的id出错时，执行该操作
        print(commit_item)
    
    print(commit_item_list)
    print(commit_item_filter_result)

    #依据获取到的列数结果，过滤结果
    filered_list_commit_filter= []
    for row_list in filered_list:
        new_row=[]
        for item_index in commit_item_filter_result:
            new_row.append(row_list[item_index])
        if new_row[0]==commit_item_list[0][0]:
            new_row.append(u'问题具体原因及修改内容')
            new_row.append(u'新知识点')
            new_row.append(u'测试建议')
            new_row.append(u'测试结果')
        filered_list_commit_filter.append(new_row)
        print(new_row)

    return filered_list_commit_filter:
    pass

def main():
    #工作文件夹地址
    file_resource=r'F:\msmSDM845_NX616J_rom81_user_sign_app_20181217210658.xls'
    if re.match('\".*\"', file_resource):
        file_resource = file_resource.split('\"')[1]
    file_resource_name = file_resource.split("\\")[-1]
    print('file_resource:')
    print(file_resource)
    #过滤的commit-item显示项
    commit_item_list=[['author',256*7],[u'Date',256*10],
                      [u'问题来源及描述',256*15],[u'问题原因',256*20],[u'解决方法',256*20],
                      [u'PR号',256*8],[u'关联测试场景路径',256*10],
                      [u'操作类型',256*7],[u'被Revert的commit',256*7],
                      [u'问题具体原因及修改内容',256*10],[u'新知识点',256*10],[u'测试建议',256*10],[u'测试结果',256*10]]
    
    file_resource_path,file_resource_name=os.path.split(file_resource)
    file_workspace=file_resource_path
    print(file_resource_path)
    print(file_resource_name)
    #确定输出文件地址及文件名
    TodayTime=strftime('%H%M%S',localtime(time()))
    file_result_name='TeamGitlog_'+TodayTime+'_'+file_resource_name
    file_result=os.path.join(file_workspace,file_result_name)
    
    print(u'输出结果文件地址：'.encode('gbk'),file_result)
    
    #获取团队成员名，通过字符串
    name_list=NAME_LIST
    #通过读取团队成员名
    #name_list=get_teamer_name(file_workspace)
    
    #获取源文件
    tables = excel_table_byindex(file_resource)
    #过滤文件中的log
    filered_list=[]
    filered_list=log_filtering(tables,name_list)#依据人名过滤gitlog，返回过滤后的log-list
    
    filered_list=filter_commit_content(filered_list,commit_item_list)
    
    #保存log
    save_filered_list(filered_list,file_result,commit_item_list)

if __name__=="__main__":
    main()