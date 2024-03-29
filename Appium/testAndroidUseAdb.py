#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-02 16:54
# 用python + adb 命令执行测试

import os
import time
from appium import webdriver


print('Start test....')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)

# https://blog.csdn.net/duoluo9/article/details/79791988   adb 命令大全

# 使用keyevetn 打开calculator
# os.popen('adb shell input keyevent 210')

# =========== adb shell am start==================
# 使用另一个命令打开 adb shell am start
os.popen('adb shell am start com.miui.calculator')

# adb shell am start其他用法
# -W参数  输出内容如下：
# os.popen('adb shell am start -W com.miui.calculator')
# Starting: Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] pkg=com.miui.calculator }
# Status: ok
# LaunchState: WARM
# Activity: com.miui.calculator/.cal.CalculatorActivity
# TotalTime: 121   应用自身启动耗时=ThisTime+应用application等资源启动时间
# WaitTime: 123  系统启动应用耗时=TotalTime+系统资源启动时间
# Complete

# adb shell am start [options] <INTENT>
# os.popen('adb shell am start -n com.android.settings/.Settings')

# adb shell am broadcast [options]<INTENT>  下面例子我没有测试成功，不知道为啥
# 举例：adb shell am broadcast -a "action_finish" （发送一个广播去关闭一个activity）
# 举例：adb shell am broadcast -a android.intent.action.MASTER_CLEAR（恢复出厂设置的方法，会清除内存所有内容）
# 举例：adb shell am broadcast -n com.lt.test/.MyBroadcast

# adb shell am start -n 包名+类名（-n 类名,-a action,-d date,-m MIME-TYPE,-c category,-e 扩展数据,等
# 添加网络DialogActivity
# os.popen('adb shell am start -n com.android.settings/com.android.settings.wifi.WifiDialogActivity')

# 强制关闭应用
# os.open('adb shell am force-stop com.miui.calculator')
# =================================================



app = 'calculator'
time.sleep(2)
appPackage_Activity = os.popen('adb shell dumpsys activity | findstr "mResume"').read()

# -*- coding: UTF-8 -*-
# By Blaine 2021-11-04 17:05
# 循环抓adb log

if app in appPackage_Activity:
    print('Open calculator successfully.')
else:
    print('Failed to open calculator.')
    
    
# os.popen('adb logcat > d:\\logs\\calculator.txt')
# 试了一下可以抓到log,有个想法，运行测试开始就开始抓log并保存，每隔一段时间就抓log
# 抓的log以当前时间命名，能否把每次抓log的时间和名称保存下来导出Excel,这个做练习用 blaine 2021-11-2 17:23

# 在焦点处于某文本框时，可以通过 input 命令来输入文本。命令：
# adb shell input text hello    
# 只能输入英文



"""
3	HOME 键
4	返回键
5	打开拨号应用
6	挂断电话
24	增加音量
25	降低音量
26	电源键
27	拍照（需要在相机应用里）
64	打开浏览器
82	菜单键
85	播放/暂停
86	停止播放
87	播放下一首
88	播放上一首
122	移动光标到行首或列表顶部
123	移动光标到行末或列表底部
126	恢复播放
127	暂停播放
164	静音
176	打开系统设置
187	切换应用
207	打开联系人
208	打开日历
209	打开音乐
210	打开计算器
220	降低屏幕亮度
221	提高屏幕亮度
223	系统休眠
224	点亮屏幕
231	打开语音助手
276	如果没有 wakelock 则让系统休眠
"""

