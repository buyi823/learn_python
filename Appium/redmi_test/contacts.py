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
            # driver.find_element_by_xpath("//android.widget.EditText[@text='姓名']").click()
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
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', contacts)
    time.sleep(1)
    
    createContact()
    driver.close_app()