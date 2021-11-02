#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-02 17:13
# 抓adb log

import os, time

print('请确保连接好手机。')

deviceInfo = os.popen('adb wait-for-device').read()
# if deviceInfo in
print(deviceInfo)