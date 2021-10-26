#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-10-26 22:14:57
# Description: adb命令查看手机上的APP包名和启动activity

import re
import os

appName = 'weather'

read_DeviceId = list(os.popen('adb devices').readlines())

device_Id = read_DeviceId[1].split('\t')[0]

print("deviceID: " + device_Id)

# 系统版本号
device_Android_Version = list(os.popen('adb shell getprop ro.build.version.release').readlines())
device_Android_VersionSdk = list(os.popen('adb shell getprop ro.build.version.sdk').readlines())
device_Version = device_Android_Version[0].split('\n')[0]
device_VersionSdk = device_Android_VersionSdk[0].split('\n')[0]
print("Version: " + device_Version)
print("platformVersion: " + device_VersionSdk)

packageName = list(os.popen('adb shell pm list package -e \"' + appName+'\"').readlines())
print(packageName)
packageName=packageName[0].strip().split(':')[1]
print("package: " + packageName)

# 读取APK的package信息
appPackageAdb = list(os.popen('adb shell pm dumpsys package'+packageName).readlines())
length = len(appPackageAdb)
for index in range(length):
    if appPackageAdb[index].find("Non-Data") != -1:
        packageInfo = appPackageAdb[index + 2].strip()
        matchObj = re.match(r'.* (.*)/(.*?) .*', packageInfo, re.M | re.I)
        if matchObj:
            print("appActivity:", matchObj.group(2))
        break;

