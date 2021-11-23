#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-29 17:11 
# 获取Android信息
# Update code 2021-11-04-15:49:17
# 折腾了一天都没有把导出excel的问题搞定。。。。。。 By Blaine 2021-11-17 18:46  
# update again 2021-11-23 终于可以导出到EXCEL了
# 2021-11-23 16:55 Done


import os, time
import xlwt

'''
isDeviceConnect() 判断是否连接设备
getDeviceInfo() 通过adb命令获取设备各种信息
title_style() 将设备信息导出Excel的标题风格定义
content_style()设备具体内容的风格定义

'''

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


# Get DUT information: adb shell getprop
def getDeviceInfo():

    os.popen('adb root')
    deviceName = os.popen('adb shell getprop ro.product.model').read().rstrip()
    print('deviceName: ' + deviceName)

    platformVersion = os.popen('adb shell getprop ro.build.version.release').read().rstrip()
    print('platformVersion: ' + platformVersion)

    device_product = os.popen('adb shell getprop ro.product.name').read().rstrip()
    print(f'device: {device_product}')
    
    device_sdk_version = os.popen('adb shell getprop ro.build.version.sdk').read().rstrip()
    print(f'device sdk version: {device_sdk_version}')
    
    # grep windows无法使用要加引号  adb shell "cat /proc/cpuinfo | grep "Hardware""
    # device_cpu = os.popen('adb shell "cat //proc//cpuinfo"').read().rstrip()
    # adb shell getprop ro.hardware：查看机器板子代号 这个也可以显示CPU型号
    device_cpu = os.popen('adb shell "cat //proc//cpuinfo | grep "Hardware""').read().rstrip()
    print(f'device_cpu Hardware: {device_cpu}')
    
    # device_memory = os.popen('adb shell "cat //proc//meminfo"').read().rstrip() # 打印的东西太多了筛选下
    device_memory = os.popen('adb shell "cat //proc//meminfo | grep "MemTotal""').read().rstrip()
    print(f'device memroy: {device_memory}')
    
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
    
    # 每个应用程序的内存上限
    # dalvik_vm_heapsize = os.popen('adb shell getprop dalvik.vm.heapsize')
    
    info_list = [deviceName, platformVersion, device_product, device_sdk_version ,device_cpu, device_memory, device_physicalSize, device_density,
                 device_battery, appPackage_Activity]
    
    return info_list


def title_style():
    # define font
    font = xlwt.Font()
    font.name = 'Calibri'
    font.bold = True
    font.colour_index = 1 # 1 white color
    font.height =  25 * 10 # 20为衡量单位，16是字号
    
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
    pattern.pattern_fore_colour = 4
    
    # init style
    my_title_style = xlwt.XFStyle()
    my_title_style.font = font
    my_title_style.alignment = alignment
    my_title_style.borders = borders
    my_title_style.pattern = pattern
        
    return my_title_style


def content_style():
    # define font
    font = xlwt.Font()
    font.name = 'Calibri'
    font.bold = False
    font.colour_index = 0 # 1 white color
    font.height =  25 * 10 # 20为衡量单位，16是字号
    
    # define alignment
    alignment = xlwt.Alignment()
    # 0x01 align left   0x02 水平方向居中    0x03 align right
    alignment.horz = 0x01
    # 0x00 上端对其  0x01 垂直方向居中   0x02 底端对齐
    alignment.vert = 0x01
    alignment.wrap = 1 # 自动换行
    
    
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
        
    # init style
    my_content_style = xlwt.XFStyle()
    my_content_style.font = font
    my_content_style.alignment = alignment
    my_content_style.borders = borders
        
    return my_content_style

if __name__ == '__main__':
    if isDeviceConnect():
        getDeviceInfo()
    book = xlwt.Workbook(encoding='UTF-8')
    sheet = book.add_sheet('Phone Information')
    
    # 标题格式
    titleStyle = title_style()
    # 内容格式
    contentStyle = content_style()
    
    # xlwt中是行和列都是从0开始计算的
    col_1 = sheet.col(0)
    col_2 = sheet.col(1)
    col_3 = sheet.col(2)
    col_4 = sheet.col(3)
    col_5 = sheet.col(4)
    col_6 = sheet.col(5)
    col_7 = sheet.col(6)
    col_8 = sheet.col(7)
    col_9 = sheet.col(8)
    col_10 = sheet.col(9)
    # 设置存储路径列宽度
    col_1.width = 256 * 25
    col_2.width = 256 * 20
    col_3.width = 256 * 25
    col_4.width = 256 * 25
    col_5.width = 256 * 35
    col_6.width = 256 * 35
    col_7.width = 256 * 50
    col_8.width = 256 * 75
    col_9.width = 256 * 75
    col_10.width = 256 * 75
    
    
    # title info
    head = ["Device Name", "Platform Version", "Device Product", "Device SDK Version", "Device Hardware", "Device Memory",
            "Device Physical Size", "Device Density", "Device Battery", "appPackage Activity"]
    
    # 获取getDeviceInfo()中打印的数据
    deviceInfo = getDeviceInfo()

    # create title
    for index, value in enumerate(head):
        sheet.write(0, index, value, titleStyle)    
     
    # 循环写入获取的数据 
    for index, value in enumerate(deviceInfo):
        sheet.write(1, index, value, contentStyle)
    
    book.save(deviceInfo[0]+ '_PhoneInfo_' + time.strftime("%Y%m%d%H%M%S") + '.xls')


