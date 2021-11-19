#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-29 17:11 
# 获取Android信息
# Update code 2021-11-04-15:49:17
# 折腾了一天都没有把导出excel的问题搞定。。。。。。 By Blaine 2021-11-17 18:46  


import os, time
from types import GetSetDescriptorType
import csv
import xlwt
import pandas as pd
from pandas import DataFrame
import numpy as np
from xlwt.Workbook import Workbook


# Check that your device is connected properly
def isDeviceConnect():
    # 将获取的设备信息保存在列表中，列表中结尾是"\n"
    devices = list(os.popen('adb devices').readlines())
    if devices[1] == '\n':
        print('Not found any device. Please check "adb devices".')
        return False
    elif len(devices) > 3: 
        print('==More than one device.==')
        return False 
    else:
        print(os.popen('adb devices').read())
        return True


# Get DUT information
# adb shell getprop
def getDeviceInfo():

    os.popen('adb root')
    deviceName = os.popen('adb shell getprop ro.product.model').read().rstrip()
    print('deviceName: ' + deviceName)

    platformVersion = os.popen('adb shell getprop ro.build.version.release').read().rstrip()
    print('platformVersion: ' + platformVersion)

    device_product = os.popen('adb shell getprop ro.product.name').read().rstrip()
    print(f'device: {device_product}')

    # 全信息显示分辨率信息
    # device_displays = os.popen('adb shell dumpsys window displays').read()
    # print(device_displays)

    device_physicalSize = os.popen('adb shell wm size').read().rstrip()
    print(device_physicalSize)

    # 查看屏幕密度
    device_density = os.popen('adb shell wm density').read().rstrip()
    print(device_density)

    device_battery = os.popen('adb shell dumpsys battery').read().rstrip()
    print(device_battery)

    appPackage_Activity = os.popen('adb shell "dumpsys activity | grep "mResume""').read().rstrip()
    print(appPackage_Activity.lstrip()) #将字符前面空格删除掉
    
    info_list = [deviceName, platformVersion, device_product, device_physicalSize, device_density,
                 device_battery, appPackage_Activity]
    
    return info_list


# use pandas
# def pandas_exportInfo():
#     # 目前可以生成标题正确的EXCEL，不知道怎么写入数据
#     title = ["Device Name", "Platform Version", "Device Product", 
#             "Device Physical Size", "Device Density", "Device Battery", "appPackage Activity"]
#     df1 = pd.DataFrame(columns=title)
#     df1.to_excel("PhoneInfo.xlsx", sheet_name='Phone Information', index=False, header=True)
    
    

# Export DUT information to Excel
# xlwt最大只支持256列
# 可以生成EXCEL，写入的循环有问题
content = ['test', 'test']
output_file = 'PhoneInfo.xls'

def create_file(output_file):
    # init style
    style_head = xlwt.XFStyle()
    # init font
    font = xlwt.Font()
    font.name = "Calibri"
    font.bold = True
    # index must digit
    font.colour_index = 1
    # init backgroud pictrue
    bg = xlwt.Pattern()
    # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    bg.pattern = xlwt.Pattern.SOLID_PATTERN
    # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 
    # 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 
    # 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
    bg.pattern_fore_colour = 4
    # set font
    style_head.font = font
    # set background
    style_head.pattern = bg
    
    # create a excel
    excel = xlwt.Workbook(encoding='utf-8')
    # add worksheet
    sheet = excel.add_sheet("The Phone Information")
    # xlwt中是行和列都是从0开始计算的
    col_1 = sheet.col(0)
    col_2 = sheet.col(1)
    col_3 = sheet.col(2)
    col_4 = sheet.col(3)
    col_5 = sheet.col(4)
    col_6 = sheet.col(5)
    col_7 = sheet.col(6)
    # 设置存储路径列宽度
    col_1.width = 256 * 25
    col_2.width = 256 * 25
    col_3.width = 256 * 25
    col_4.width = 256 * 25
    col_5.width = 256 * 25
    col_6.width = 256 * 25
    col_7.width = 256 * 25
    
    # title info
    head = ["Device Name", "Platform Version", "Device Product", 
            "Device Physical Size", "Device Density", "Device Battery", "appPackage Activity"]
        
    # create title
    for index, value in enumerate(head):
        sheet.write(0, index, value, style_head)
            
     
    # 循环写入   （这里有问题总报错 ）
    # for index, value_list in enumerate(content, 1):
    #     for i, value in enumerate(value_list):
    #         sheet.write(index, i, value)
    excel.save(output_file)



if __name__ == '__main__':
    if isDeviceConnect():
        getDeviceInfo()
        create_file(output_file)
    


