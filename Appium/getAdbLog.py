#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-04 17:05
# 循环抓adb log

import os, time

# 判断手机是否连接
def isDeviceConnect():
    # 将获取的设备信息保存在列表中，列表中结尾是"\n"
    # 以结尾的回车来判断
    devices = list(os.popen('adb devices').readlines())
    if devices[1] == '\n':
        print('Not found any device. Please check "adb devices".')
        return False
    elif len(devices) > 3: 
        print('More than one device.')
        return False 
    else:
        print(os.popen('adb devices').read())
        return True


# 获取LOG
def getAdbLog():
    os.popen('adb root')
    # interval: 抓log间隔时间,用户输入次数,单位秒
    # times：循环抓LOG次数，用户输入次数
    for i in range(times):
        # 放在当前目录了, 以抓log时间命名
        os.popen('adb logcat > log_{time}.txt'.format(time=time.strftime('%Y%m%d%H%M%S', time.localtime())))
        print(f'第{i+1}次获取抓取成功......{time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())}')
        i += 1
        # 抓取LOG的间隔时间可以设置
        print(f'waiting {interval}s.....')
        time.sleep(interval)


if __name__ == '__main__':
    
    if isDeviceConnect():
        # abs() 绝对值 
        interval = abs(int(input('请输入抓log间隔时间(单位秒),请输入正整数后回车： ')))
        times = abs(int(input('请输入您想抓取log的次数，请输入正整数后回车： ')))
        getAdbLog()

# 生成以当前时间命名的文件
# uuid_str = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
# tmp_file_name = '%s.txt' % uuid_str
# with open(tmp_file_name, 'a') as f:
#     f.write("{}\n\n".format(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))))