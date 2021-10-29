#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-27 10:52
# Appium example

import os
import subprocess
from appium import webdriver
import time

calculator = {
    'platformName': 'Android',
    'deviceName': 'Redmi Note 8 Pro',
    'platformVersion': '11',
    'appPackage': 'com.miui.calculator',
    'appActivity': '.cal.CalculatorActivity'
}

driver = webdriver.Remote('http://localhost/wd/hub', calculator)
time.sleep(2)

def cal():
    driver.find_element_by_id().click()
    

cal()

