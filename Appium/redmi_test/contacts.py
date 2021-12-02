#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-12-02 10:10
# Contacts Testing
 
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import os
import traceback

# contacts = {
#     'platformName': 'Android',
#     'deviceName': 'Redmi Note 8 Pro',
#     'platformVersion': '11',
#     'appPackage': 'com.android.contacts',
#     'appActivity': '.activities.TwelveKeyDialer',
#     'unicodeKeyboard': True,
#     'resetKeyboard': True
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', contacts)
# time.sleep(1)


# 想法：1. 一个文件测试一个手机模块，然后所有都执行；
# 2. 如果报错输出错误信息，报错时抓手机log，并保存错误信息
# 3. 测试完成生成个测试报告，记录测试时常，每个模块测试结果，如果报错打印出哪里报错，并记录抓的是哪个log
# 待实现
# By Blaine 2021-12-02 18:23


'''
测试自己手机
createContact()
新建手机存储空间的联系人，没有执行完成的话报错，抓LOG，LOG以当前时间命名
报错不一定是手机问题，也可能是没有找到相关的元素导致失败。

'''

def createContact():
    try:
        
        for i in range(1, 3):
            # 打开联系人界面在dialer界面，点击联系人,下面两种方式都可以点击成功
            # driver.find_element_by_xpath("//*[@text='联系人']").click()
            driver.find_element_by_xpath("//android.widget.TextView[@text='联系人']").click()
            time.sleep(1)
            # 点击新建联系人按钮两种方式都可以定位到元素
            driver.find_element_by_id('android:id/icon').click()
            # driver.find_element_by_accessibility_id('新建联系人').click()
            time.sleep(1)
            # 点击仅保存在设备中  第一次会弹出保存路径，不退出联系人使用脚本，不会再次弹出了
            # 做个判断进第一次需要点击保存手机中按钮
            if i == 1:
                driver.find_element_by_id('android:id/button3').click()    
            time.sleep(1)
            # 点击姓名文本框应该弹出输入法，appium执行后无法弹出输入法，不过下面的语句使用send_keys()方法，其实也没有使用输入法
            # 这句语句不执行，直接定位元素输入字符也是可以成功的，如果模拟用户输入的话，一般是点击输入框后弹出输入法然后输入才对
            driver.find_element_by_xpath("//android.widget.EditText[@text='姓名']").click()
            time.sleep(1)
            # 输入联系人名称
            driver.find_element_by_xpath("//android.widget.EditText[@text='姓名']").send_keys(f"Blaine Xu-{i}")
            time.sleep(1)
            # driver.find_element_by_xpath("//android.widget.EditText[@text='电话']").click()
            time.sleep(1)
            # 输入电话号码
            driver.find_element_by_xpath("//android.widget.EditText[@text='电话']").send_keys(f"13488359081-{i}")
            time.sleep(1)
            driver.find_element_by_id("android:id/button2").click() #点击确定对号
            print(f"新建第{i}个联系人完成!")
            time.sleep(1)
            driver.press_keycode(4)
            time.sleep(1)
            
    except Exception as e:
        print(e)
        traceback.print_exc() # 会打印详细Traceback信息
        os.popen('adb logcat > log_{time}.txt'.format(time=time.strftime('%Y%m%d%H%M%S', time.localtime())))
        logname = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
        print(f"Log抓取成功{logname}")
           

if __name__ == '__main__':
    # 初始化Appium配置信息
    contacts = {
    'platformName': 'Android',
    'deviceName': 'Redmi Note 8 Pro',
    'platformVersion': '11',
    'appPackage': 'com.android.contacts',
    'appActivity': '.activities.TwelveKeyDialer',
    'unicodeKeyboard': True,
    'resetKeyboard': True
}
    # 与Appium建立连接
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', contacts)
    time.sleep(1)
    
    createContact()
    driver.close_app()