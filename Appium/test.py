#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-27 10:52
# Appium example

from appium import webdriver
import time

# desired capability
calculator = {
    'platformName': 'Android',
    'deviceName': 'Redmi Note 8 Pro',
    'platformVersion': '11',
    'appPackage': 'com.miui.calculator',
    'appActivity': '.cal.CalculatorActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', calculator)
time.sleep(3)

# 输出当前屏幕分辨率
print(driver.get_window_size())
# {'width':1080， 'height':2134 }  返回的是个字典

# 截图
driver.get_screenshot_as_file("d:\\logs\\appium_screenshot.png")
print("screenshot path: d:\\logs")

# 打印当前网络类型
# 0 None   1 Airplane Mode  2 Wifi only  4 Data only  6 All network on
# 直接print(driver.network.connection) 方便看网络状态可以用下面语句
if driver.network_connection == 0:
    print("Network: 0 None")
elif driver.network_connection== 1:
    print("Network: 1 Airplane Mode")
elif driver.network_connection== 2:
    print("Network: 2 Wi-Fi Only")
elif driver.network_connection== 4:
    print("Network: 4 Data Only")
else:
    print("Network: 6 All network on")


# python 3.10后支持match...case语句，与其他语言switch...case一样，上面语句可以改成这个看着清晰一点
# match driver.network_connection:
#     case 0:
#         print("Network: 0 None")
#     case 1:
#         print("Network: 1 Airplane Mode")
#     case 2:
#         print("Network: 2 Wi-Fi Only")
#     case 4:
#         print("Network: 4 Data Only")
#     case 6:
#         print("Network: 6 All network on")

def plus():
    # 使用packageName+Activity打开会先弹出对话框
    # 第二部分会弹出右上角的提示菜单，需要处理

    # click "同意"按钮
    driver.find_element_by_id("android:id/button1").click()
    # click 返回键退出当前界面
    time.sleep(1)
    driver.keyevent(4)

    # 测试5+3=8
    driver.find_element_by_id("com.miui.calculator:id/digit_5").click()
    time.sleep(1)
    driver.find_element_by_id("com.miui.calculator:id/op_add").click()
    time.sleep(1)
    driver.find_element_by_id("com.miui.calculator:id/digit_3").click()
    time.sleep(1)
    driver.find_element_by_id("com.miui.calculator:id/btn_equal_s").click()
    time.sleep(1)
    
    # swipe driver.swipe(start_x, start_y, end_x, end_y, duration=None)：
    # 参数分别是起点坐标的x,y和终点坐标的x,y，以及滑动时间，滑动事件的单位是ms
    # 滑动到第二页“换算”

    size = driver.get_window_size()
    start_x = size['width']*0.9
    start_y = size['height']*0.3
    end_x = size['width']*0.1
    end_y = size['height']*0.3
    #从右向左滑
    driver.swipe(start_x,start_y, end_x,end_y,800)
    print('swipe') 
    # By Blaine Time: 2021-11-01 23:58:49 # Description: 测试滑动没有成功
    # #从左向右滑
    # driver.swipe(end_x,end_y,start_x,start_y,200)

    # 向下滑动
    # #向上滑动：x轴不变，y从大到小
    # driver.swipe(size["width"]*0.5,size["heigth"]*0.9,size["width"]*0.5,size["heigth"]*0.1)
    # 向上滑动：x轴不变，y从小到大
    # driver.swipe(size["width"]*0.5,size["heigth"]*0.1,size["width"]*0.5,size["heigth"]*0.9)
    time.sleep(2)
    driver.quit()

plus()
