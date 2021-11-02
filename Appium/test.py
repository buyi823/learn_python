#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-10-27 10:52
# Appium example

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

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
# 截图
driver.get_screenshot_as_file("d:\\logs\\appium_screenshot.png")
print("screenshot path: d:\\logs")


# appium 教程参考 https://www.cnblogs.com/liuhui0308/p/12033199.html


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
    
# python 3.10后支持match...case语句，与其他与他switch...case一样，上面语句可以改成这个看着清晰一点
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




# 从一个元素滑动到另一个元素，直到页面自动停止。
# driver.scroll(origin_el, destination_el)：参数分别是滑动开始的元素和滑动结束的元素。 

# 从一个元素滑动到另一个元素，第二个元素代替第一个元素原本屏幕上的位置。drag_and_drop拖拽事件
# 方法：driver.drag_and_drop(origin_el, destination_el)：参数分别是滑动开始的元素和滑动结束的元素。
# save_button = driver.find_element_by_xpath("//*[@text='存储']")
# more_button = driver.find_element_by_xpath("//*[@text='更多']")
# driver.drag_and_drop(save_button, more_button)

# 模拟手指对某个元素或坐标按下并快速抬起。比如，固定点击（100, 100）的位置。
# methord: TouchAction(driver).tap(element=None, x=None, y=None).perform()：参数可以是元素，也可以是x,y坐标。
# el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).tap(el).perform()

# 手势解锁需要先按下，再移动
# TouchAction(driver).move_to(el=None, x=None, y=None).perform()
# TouchAction(driver).press(x=150, y=525).move_to(x=450, y=525).move_to(x=750,
# y=525).move_to(x=750, y=825).move_to(x=450, y=825).move_to(x=150,
# y=825).move_to(x=450, y=1125).release().perform()


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
    driver.swipe()
    # driver.swipe(start_x, start_y, end_x, end_y, duration=None)：参数分别是起点坐标的x,y和终点坐标的x,y，以及滑动时间，滑动事件的单位是ms。
    driver.quit()

# plus()
