#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-29 17:11
# 获取Android信息

import os
from types import GetSetDescriptorType

# adb shell getprop

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

appPackage_Activity = os.popen('adb shell dumpsys activity | findstr "mResume"').read().rstrip()
print(appPackage_Activity.lstrip()) #将字符前面空格删除掉

# 有个想法把一个手机的基础信息导出到excel， 如何去实现？ 2011/11/2 18：26




