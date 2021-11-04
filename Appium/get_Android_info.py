#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-29 17:11 
# 获取Android信息
# Update code 2021-11-04-15:49:17

import os, time
from types import GetSetDescriptorType
import csv

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


# adb shell getprop
def getDeviceInfo():

    os.popen('adb root')
    deviceName = os.popen('adb shell getprop ro.product.model').read()
    print('deviceName: ' + deviceName)

    platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
    print('platformVersion: ' + platformVersion)

    device_product = os.popen('adb shell getprop ro.product.name').read()
    print(f'device: {device_product}')

    # 全信息显示分辨率信息
    # device_displays = os.popen('adb shell dumpsys window displays').read()
    # print(device_displays)

    device_physicalSize = os.popen('adb shell wm size').read()
    print(device_physicalSize)

    # 查看屏幕密度
    device_density = os.popen('adb shell wm density').read()
    print(device_density)

    device_battery = os.popen('adb shell dumpsys battery').read()
    print(device_battery)

    appPackage_Activity = os.popen('adb shell "dumpsys activity | grep "mResume""').read().rstrip()
    print(appPackage_Activity.lstrip()) #将字符前面空格删除掉

# 将信息导出到csv   还不知道怎么实现
# def deviceInfo_csv():
#     # start_time = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime())
#     # csv_data = [start_time]
#     path = "deviceInfo.csv"
#     with open(path, 'wb') as f:
#         csv_write = csv.writer(f)
#         csv_head = ["deviceName", "platformVersion", "platformVersion", 
#         "device_product", "device_physicalSize", 'device_density', 'device_battery']
#         csv_write.writerows(csv_head)



if __name__ == '__main__':
    if isDeviceConnect():
        getDeviceInfo()


