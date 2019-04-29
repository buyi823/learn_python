# -*- coding: utf-8 -*-
import os
import random
import re
from time import strftime, localtime, time
import xlrd, xlwt

#系统团队成员名单----------------------------------------
NAME_LIST=['aoshan','luyang','sunfei','gezhibo','laiaifang','hanyangang', #设置团队人员名单
           'lizhiwen','libo','liushitao','anzhanlei','wangjixiang',#分屏、分身及指纹团队人员名单
           'chenxin','wangneng','zhenxiaojuan','fengpeng','zhangjie',#动画团队人员名单
           'wangweili','xuqiheng','zhukuifeng','yedunhui','denghanmin']#控件团队人员名单


def open_excel(file= r''):
    try:
        data = xlrd.open_workbook(file)
        print 'data:',data
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='',colnameindex=1,by_index=0):
    data = open_excel(file)
    table = data.sheet_by_index(by_index)
    print data.sheet_names()
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    print nrows,ncols
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = []
             for i in range(len(colnames)):
                app.append(row[i]) 
             list.append(app)
    return list
'''
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= r'D:\workspace\GitLogFiltering\src\123.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list
'''
def log_filtering(filtering_table=[],name_list=''):
    #name_list=['moyunfei',]
    filered_list=[]
    filered_list.append(filtering_table[0])#先添加一列标题栏
    for row in filtering_table:
        for name in name_list:
            if(row[2]==name):
                filered_list.append(row)#将符合条件的log记录筛选出来
                print '***********'
                for k in  row:
                    #print k,v.strip()
                    print k
                print  '***********'
                break#跳出namelist循环
            
    for i in filered_list:
        print i
    return filered_list

def set_style(name,height,bold=False):
    style = xlwt.XFStyle()  # 初始化样式
 
    font = xlwt.Font()  # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
 
    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6
 
    style.font = font
    # style.borders = borders
 
    return style

def save_filered_list(filered_list=[],file_result='',commit_item_list=[]):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    style = xlwt.easyxf(u'align: wrap on, vert centre, horiz left;font: height 180,name 宋体;borders: top 1, bottom 1,left 1,right 1')
#     width_list=[]
    
#     first_col=sheet1.col(0)       #xlwt中是行和列都是从0开始计算的
#     first_col.width=256*20 
    
    for commit_item in commit_item_list:
        try:
            commit_item_index=filered_list[0].index(commit_item[0]);
            sheet1.col(commit_item_index).width=commit_item[1];
        except ValueError,e:#获取对应value值的id出错时，执行该操作
            print e.message
        print commit_item
    
    #sheet.write(0, 0, 'Firstname', style)
    #''
    
    #写入filered_list中的内容
    for i in range(len(filered_list)):
        if filered_list[i][0]==commit_item_list[0][0]:
            print_row=filered_list[i]
        else:
            print_row=filered_list[i]+['','','','']
        for j in range(len(print_row)):
            #sheet1.write(i,j,filered_list[i][j],set_style('Times New Roman',220,True))
            sheet1.write(i,j,print_row[j],style)
        
            
    f.save(file_result)
    
    pass

def SearchFile(FileType,SearchPath):
    print SearchPath
    for (dirpath, dirnames, filenames) in os.walk(SearchPath):
        for file in filenames:
            if re.match(FileType, file):
                TargetFile=os.path.join(dirpath,file)
                file_suffix=file.split('.')[1]
                print '------------------------'
                print 'SearchFile:',TargetFile
                print '------------------------'
                return [TargetFile,dirpath,file,file_suffix]
    
def get_teamer_name(file_workspace):
    name_list=[]
    team_name_address=SearchFile('.*ame.*\.txt',file_workspace)[0]
    f = open(team_name_address,'r+')
    for line in f.readlines():
        name_list.append(line.strip())
    f.close()
    print name_list
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
            commit_item_index=filered_list[0].index(commit_item[0])
            commit_item_filter_result.append(commit_item_index)
        except ValueError,e:#获取对应value值的id出错时，执行该操作
            print e.message
        print commit_item
        
    print commit_item_list;
    print commit_item_filter_result
    
    #依据获取到的列数结果，过滤结果
    filered_list_commit_filter=[]
    for row_list in filered_list:
        new_row=[];
        for item_index in commit_item_filter_result:
            new_row.append(row_list[item_index])
        if new_row[0]==commit_item_list[0][0]:
            new_row.append(u'问题具体原因及修改内容');
            new_row.append(u'新知识点');
            new_row.append(u'测试建议');
            new_row.append(u'测试结果');
        filered_list_commit_filter.append(new_row);
        print new_row
    
    
    
    return filered_list_commit_filter;
    pass
    
def main():
    '''
    #工作文件夹地址
    #file_resource=r'D:\workspace\GitLogFiltering\src\123.xls'
    file_workspace=os.getcwd()
    file_resource_detail=SearchFile('msm8996_NX531J_AndroidN_dev_user_sign_app_\d{14}.*\.xls',file_workspace)
    file_resource=file_resource_detail[0]
    
    #获取存放目标文件的地址
    #file_result=r'D:\workspace\GitLogFiltering\src\SystemTeamGitLog.xls'
    file_result_name='TeamGitlog_'+file_resource_detail[2]
    file_result=os.path.join(file_workspace,file_result_name)
    
    '''
    #工作文件夹地址
    #file_workspace=r'd:\\'
    #获取需被分离文件地址
    #file_resource=raw_input(u'请将需筛选xls文件托人该界面并回车确认！'.encode('gbk'))
    #xp系统版地址
    #file_resource=r'"D:\workspace\GitLogFiltering\src\msm8996_NX531J_AndroidN_rom_user_sign_app_20171010011249.xls"'
    #win7系统版地址
    file_resource=r'F:\version\msmSDM845_NX619J_rom90_user_sign_app_20181203234110.xls'
    
    if re.match('\".*\"', file_resource):#代表其输入地址为“。。。”的显示格式，而不是直接是地址。。。，应该是xp系统
        file_resource=file_resource.split('\"')[1]
    file_resource_name=file_resource.split("\\")[-1]
    print 'file_resource:'
    print file_resource

    #过滤的commit-item显示项
    #commit_item_list=[['commit',256*20],['author',256*20],[u'提交人',256*20],[u'问题来源及描述',256*20]]
    commit_item_list=[['author',256*7],[u'Date',256*10],
                      [u'问题来源及描述',256*15],[u'问题原因',256*20],[u'解决方法',256*20],
                      [u'PR号',256*8],[u'关联测试场景路径',256*10],
                      [u'操作类型',256*7],[u'被Revert的commit',256*7],
                      [u'问题具体原因及修改内容',256*10],[u'新知识点',256*10],[u'测试建议',256*10],[u'测试结果',256*10]]
    #去掉文件名称识别
#     if not re.match(r'msm8996_NX531J_AndroidN_dev_user_sign_app_\d{14}.*\.xls', file_resource_name):
#         print u'输入处理文件格式不符!'
#         return None
    file_resource_path,file_resource_name=os.path.split(file_resource)
    file_workspace=file_resource_path
    print file_resource_path
    print file_resource_name
    #确定输出文件地址及文件名
    TodayTime=strftime('%H%M%S',localtime(time()))
    file_result_name='TeamGitlog_'+TodayTime+'_'+file_resource_name
    file_result=os.path.join(file_workspace,file_result_name)
    
    print u'输出结果文件地址：'.encode('gbk'),file_result
    
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
    '''
    for row in tables:
        for name in name_list:
            if(row['author']==name):
                print '***********'
                for (k,v) in  row.items():
                    print k,v.strip()
                print '***********'
'''
'''
   tables = excel_table_byname()
   for row in tables:
       print row
'''
       
if __name__=="__main__":
    main()

    

'''
Created on 2017-2-23

@author: carrybur
'''