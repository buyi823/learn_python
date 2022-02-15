#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-12-16 15:44
# 操作微信看看谁删除了我

from appium import webdriver
import time

# 使用这个打开每次都要输入密码  'noRest'是不清除session的，
# 如果第一次打开微信应该需要输入用户名和密码，得操作下
WeChat = {
    'platformName': 'Android',
    'deviceName': 'Redmi Note 8 Pro',
    'platformVersion': '11',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noRest': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', WeChat)
time.sleep(1)


# 往上的代码没有验证，上面是我自己的配置


# 获取通讯录列表
def get_address_list():
    driver.find_elements_by_id('com.tencent.mm:id/cn_')[1].click()
    # 获取昵称（备注）
    address_list = driver.find_elements_by_id('com.tencent.mm:id/dy5')
    remarks = []
    for address in address_list:
        remark = address.get_attribute("content-desc")
        # 排除自己和微信官方号
        if remark != "自己的微信名" and "微信" not in remark:
            remarks.append(remark)
    return remarks

# 判断是否被删
def is_delete(remark, count):
    if count == "1":
        time.sleep(2)
        print('点击微信搜索框')
        driver.find_element_by_id('com.tencent.mm:id/cn1').click()
    time.sleep(2)
    print('在搜索框输入搜索信息')
    driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(remark)
    time.sleep(2)
    print('点击搜索到的好友')
    driver.find_element_by_id('com.tencent.mm:id/tm').click()
    time.sleep(2)
    # 转账
    driver.find_element_by_id('com.tencent.mm:id/aks').click()
    time.sleep(2)
    driver.find_elements_by_id('com.tencent.mm:id/pa')[5].click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/cx_').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/cxi').click()
    time.sleep(5)
    # 判断是否被删
    is_exist = is_element_exist('com.tencent.mm:id/jh')
    if is_exist is True:
        return remark
    else:
        return False
    
    # 删除把自己删除的人
def del_person(nicks):
    for inx, val in enumerate(nicks):
        time.sleep(2)
        if inx == 0:
            print('在搜索框输入搜索信息')
            driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(val)
        else:
            time.sleep(2)
            print('点击微信搜索框')
            driver.find_element_by_id('com.tencent.mm:id/cn1').click()
            print('在搜索框输入搜索信息')
            time.sleep(1)
            driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(val)
        time.sleep(2)
        print('点击搜索到的人')
        driver.find_element_by_id('com.tencent.mm:id/tm').click()
        time.sleep(2)
        print('点击聊天对话框右上角...')
        driver.find_element_by_id('com.tencent.mm:id/cj').click()
        time.sleep(2)
        print('点击头像')
        driver.find_element_by_id('com.tencent.mm:id/f3y').click()
        time.sleep(2)
        print('点击联系人右上角...')
        driver.find_element_by_id('com.tencent.mm:id/cj').click()
        time.sleep(2)
        print('点击删除按钮')
        driver.find_element_by_id('com.tencent.mm:id/g6f').click()
        time.sleep(2)
        print('点击弹出框中的删除')
        driver.find_element_by_id('com.tencent.mm:id/doz').click()

