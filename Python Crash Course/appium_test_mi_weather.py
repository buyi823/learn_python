# -*- coding: UTF-8 -*-
import os
import time
import unittest
# from selenium import webdriver
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['version'] = '11'
desired_caps['deviceName'] = 'Redmi_Note_8_Pro'  # 这是测试机的型号，可以查看手机的关于本机选项获得
# desired_caps['app'] = PATH('D:\\qq.apk')#被测试的App在电脑上的位置
desired_caps['appPackage'] = 'com.miui.weather2'
desired_caps['appActivity'] = 'com.miui.weather2.ActivityWeatherMain'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
print('launch appium normal')

# 直接使用package和activity会弹出用户须知
driver.find_element_by_id('android:id/button1').click()
print('click user notice successful')
time.sleep(3)
# driver.find_element_by_name('登 录').click()
driver.find_element_by_id('com.miui.weather2:id/daily_forecast_more').click()
time.sleep(5)
print('click successful: 15天天气')
time.sleep(5)

driver.find_element_by_id('com.miui.weather2:id/up').click()
print('click successful：返回上一页')

# name = driver.find_element_by_name('QQ号/手机号/邮箱')
# name.send_keys('254901517')
# psd = driver.find_element_by_id('password')
# psd.click()
# psd.send_keys("12345678")
# blogin=driver.find_element_by_id('login')
# blogin.click()

time.sleep(3)
driver.press_keycode(AndroidKey.BACK)
print('done')
