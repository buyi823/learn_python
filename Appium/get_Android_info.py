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

device = os.popen('adb shell getprop ro.product.name').read()
print(f'device: {device}')

appPackage_Activity = os.popen('adb shell dumpsys activity | findstr "mResume"').read().rstrip()
print(appPackage_Activity.lstrip()) #将字符前面空格删除掉




