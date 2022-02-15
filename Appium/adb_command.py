#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-25 10:51
# adb command
# refer to https://blog.csdn.net/duoluo9/article/details/79791988

import os

a = os.popen('adb devices').read().rstrip()
print(a)
b = os.popen('adb shell wm size').read()
print(b)

# 指定 adb server 的网络端口
# adb -P <port> start-server

# 查看应用列表
# adb shell pm list packages [-f] [-d] [-e] [-s] [-3] [i] [u] [--user USER_ID] [FILTER]
# 清除应用数据及缓存
# adb shell pm clear <package name>

# install
# adb install 实际是分三步完成：
# push apk 文件到 /data/local/tmp。
# 调用 pm install 安装。
# 删除 /data/local/tmp 下的对应 apk 文件。
# 所以，必要的时候也可以根据这个步骤，手动分步执行安装过程。

# adb uninstall [-k] <packagename>

# 查看前台 Activity
# adb shell dumpsys activity activities | grep MfocusedActivity
# adb shell dumpsys activity | grep mResume

# 查看正在运行的 Services
# adb shell dumpsys activity service [<packagename>]]

# 查看应用详细信息
# adb shell dumpsys package <packagename>

# 调起 Activity
# adb shell am start [options] <INTENT>
# e.g.    adb shell am start -n com.tencetn.mm/.ui.LauncherUI
# 表示调起 org.mazhuang.boottimemeasure/.MainActivity 并传给它 string 数据键值对 toast - hello, world
# adb shell am start -n org.mazhuang.boottimemeasure/.MainActivity --es "toast" "hello, world"

# 调起 Service
# adb shell am startservice [options] <INTENT>
# adb shell am startservice -n com.tencent.mm/.plugin.accountsync.model.AccountAuthenticatorService
# 表示调起微信的某 Service

# 发送广播
# adb shell am broadcast [options] <INTENT>
# 可以向所有组件广播，也可以只向指定组件广播。 例如，向所有组件广播 BOOT_COMPLETED：
# adb shell am broadcast -a android.intent.action.BOOT_COMPLETED
# 只向 org.mazhuang.boottimemeasure/.BootCompletedReceiver 广播 BOOT_COMPLETED：
# adb shell am broadcast -a android.intent.action.BOOT_COMPLETED -n org.mazhuang.boottimemeasure/.BootCompletedReceiver

# 强制停止应用
# adb shell am force-stop <packagename>

# 在 adb shell 里有个很实用的命令叫 input，通过它可以做一些有趣的事情
# adb shell input keyevent <keycode>
# The sources are:
#       dpad
#       keyboard
#       mouse
#       touchpad
#       gamepad
#       touchnavigation
#       joystick
#       touchscreen
#       stylus
#       trackball
# The commands and default sources are:
#       text <string> (Default: touchscreen)
#       keyevent [--longpress] <key code number or name> ... (Default: keyboard)
#       tap <x> <y> (Default: touchscreen)
#       swipe <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
#       draganddrop <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
#       press (Default: trackball)
#       roll <dx> <dy> (Default: trackball)
#       motionevent <DOWN|UP|MOVE> <x> <y> (Default: touchscreen)
#       tmode <tmode>
# press menu: adb shell input keyevent 82
# press Home: adb shell input keyevent 3
# press back: adb shell input keyevent 4
# adjust volume: (up) adb shell input keyevent 24; (down) adb shell input keyevent 25 slient: adb shell input keyevent 164
# 点亮/熄灭屏幕
# adb shell input keyevent 224  点亮
# adb shell input keyevent 223  熄灭
# 如果锁屏没有密码，是通过滑动手势解锁，那么可以通过 input swipe 来解锁
# 参数 300 1000 300 500 分别表示起始点x坐标 起始点y坐标 结束点x坐标 结束点y坐标。
# adb shell input swipe 300 1000 300 500
# 输入文本 在焦点处于某文本框时，可以通过 input 命令来输入文本。
# adb shell input text hello

# adb shell getprop ro.product.model
# adb shell dumpsys battery
# adb shell wm size
# adb shell wm density
# adb shell dumpsys window displays
# adb shell settings get secure android_id
# adb shell dumpsys iphonesubinfo   在 Android 4.4 及以下版本可通过如下命令获取 IMEI
# adb shell getprop ro.build.version.release
# adb shell ifconfig | grep Mask
# adb shell ifconfig wlan0
# adb shell cat /sys/class/net/wlan0/address
# adb shell cat /system/build.prop
# adb exec-out screencap -p > sc.png   这个命令之前没有用过
# adb shell screenrecord /sdcard/filename.mp4  默认录制180s adb shell screenrecord --help
# wifi password      need root
# adb shell   cat /data/misc/wifi/*.conf
# open & close wifi
# adb shell svc wifi enable/disable
# 重启到 Recovery 模式
# adb reboot recovery
# 重启到 Fastboot 模式
# adb reboot bootloader

# 启用、禁用 SElinux
# adb shell setenforce 1
# adb shell setenforce 0  禁用

# adb shell ps
# adb shell top

