#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-10 10:22
# get screenRecord for KaiOS 3.2
# get adb log

import os, time

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


def getAdbLog():
    os.popen('adb root')
    print('start get adb log....')
    time.sleep(2)
    os.popen('adb logcat > d:\logs\log_{time}.txt'.format(time=time.strftime('%Y%m%d%H%M%S', time.localtime())))
    print('adb log path: d:\logs')


# KaiOS 3.2 支持adb shell gfxdebugger录屏，使用此功能录屏
def screenRecord():
    times = int(input("Please enter the time you want to record the screen(Max 300s):\n"))
    os.popen('adb shell gfxdebugger -c screenrecord -o 3gpp -t {} data/local/tmp/recordScreen.3gpp'.format(times))
   
    while times > 0:
        times -= 1
        time.sleep(1)
        print(f"Screen Record Countdown: {times}")
        
    if times == 0:
       print('time up')
   
    os.popen('adb pull /data/local/tmp/recordScreen.3gpp d:/logs')
    print('Screen Record export path d:/logs')
    # os.popen('adb shell rm /data/local/tmp/recordScreen.3gpp')

# 判断目录是否存在，不存在则新建
def ifDirExists():
    dirs = 'D:\logs'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    
    
if __name__ == '__main__':
    ifDirExists()
    print('Please find screen record and logs on d:\logs')
    if isDeviceConnect():
        screenRecord()
        getAdbLog()

