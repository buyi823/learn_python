#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-27 10:52
# 

import os
import subprocess
from appium import webdriver

# print(os.popen('adb devices -l'))
# print(list(os.popen('adb devices -l').readlines()))
a = os.popen('adb devices -l').readlines()
print(a)
# os.system("adb devices -l")