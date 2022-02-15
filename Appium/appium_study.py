#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-11-29 13:33
# Appium test 各种手势操作


from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

settings = {
    'platformName': 'Android',
    'deviceName': 'Redmi Note 8 Pro',
    'platformVersion': '11',
    'appPackage': 'com.android.settings',
    'appActivity': '.MainSettings',
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', settings)

time.sleep(3)

# location查看元素的坐标， size可以查看元素高度和宽度
titles = driver.find_element_by_id('android:id/title')
print(titles.location)
print(titles.size)

# swipe 
# 滑动 从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动。 持续3s
# 距离相同时，持续时间越长，惯性越小。
# 持续时间相同时，手指滑动的距离越大，实际滑动的距离也就越大
driver.swipe(211, 2012, 211, 1250, 3000)
time.sleep(2)

# scroll 
# 从一个元素滑动到另一个元素，直到页面自动停止
# driver.scroll(origin_el, destination_el)
# 不能设置持续时间，惯性很大。不能设置持续时间，惯性很大。
scroll_destination_ele = driver.find_element_by_xpath("//*[@text='显示']")
scroll_origin_ele= driver.find_element_by_xpath("//*[@text='安全']")
driver.scroll(scroll_origin_ele, scroll_destination_ele)
# 从“安全”滑动到“显示”
time.sleep(1)

# drag_and_drop 
# 从一个元素滑动到另一个元素，第二个元素代替第一个元素原本屏幕上的位置。
# driver.drag_and_drop(origin_el, destination_el)：参数分别是滑动开始的元素和滑动结束的元素。
# 不能设置持续时间，没有惯性
drag_and_drop_origin = driver.find_element_by_xpath("//*[@text='应用设置']")
drag_and_drop_destination = driver.find_element_by_xpath("//*[@text='特色功能']")
driver.drag_and_drop(drag_and_drop_origin, drag_and_drop_destination)
time.sleep(1)

# 高级手势
# 轻敲操作  模拟手指对某个元素或坐标按下并快速抬起。比如，固定点击（100, 100）的位置。
# TouchAction(driver).tap(element=None, x=None, y=None).perform()：参数可以是元素，也可以是x,y坐标。
# ele = driver.find_element_by_xpath("//*[@text='安全']")  这样也行，定位元素方法不同
ele = driver.find_element_by_xpath("//*[contains(@text,'安全')]")
TouchAction(driver).tap(ele).perform()
time.sleep(1)

# press back
driver.press_keycode(4)
# driver.keyevent(4)
time.sleep(1)


scroll_destination_ele1 = driver.find_element_by_xpath("//*[@text='小爱同学']")
scroll_origin_ele1= driver.find_element_by_xpath("//*[@text='桌面']")
driver.scroll(scroll_origin_ele1, scroll_destination_ele1)
time.sleep(1)

# 按下和抬起操作
# 模拟手指一直按下，模拟手指抬起。可以用来组合成轻敲或长按操作。
# TouchAction(driver).press(el=None, x=None, y=None).perform()：模拟手指按下，参数和轻敲操作一样。
# TouchAction(driver).release().perform()：模拟手指对元素或坐标的抬起操作。
TouchAction(driver).press(x=211, y=1250).perform() # 只是按下去
time.sleep(2)
TouchAction(driver).press(x=211, y=1250).release().perform() # 按下去后抬起

driver.press_keycode(3) # 按home
time.sleep(1)

# 坐标点是设置的起始位置，但是按了之后没按住设置，等于是桌面的空白地方长按了
# TouchAction(driver).long_press(x=642, y=1510).perform() # long press
# settings_button = driver.find_element_by_xpath("//*[@text='设置']")# 这一句同上不知道为啥还是按倒空白地方了
settings_button = driver.find_element_by_accessibility_id("设置") # content-desc的值 这种定位方式长按设置成功了
TouchAction(driver).long_press(settings_button).perform()
time.sleep(1)

# driver.find_element_by_xpath("//*[@text='应用信息']").click() # 这句没有报错但是没有点击成功
# 下面两句还是没有点到应用信息
# app_info = driver.find_element_by_xpath("//*[@text='应用信息']") 
# TouchAction(driver).press(app_info).perform()
# 这句没有报错但是没有点击成功
# driver.find_element_by_android_uiautomator('new UiSelector().text("应用信息")').click() 
# driver.find_elements_by_id('com.miui.home:id/item_title')[0].click()# 不报错还是没有点中
# driver.find_elements_by_class_name('android.widget.TextView')[0].click() # 不报错还是没有点中
# 坐标点是716 772  再试试
TouchAction(driver).press(x=716, y=772).perform()  #  不报错还是没有点中,我绝望了
# 上面要点击长按设置后的“应用信息”,还没有完成 2021/12/1 17：46

# 以上代码可以运行，下面的没有运行，只是例子

# 等待操作
# TouchAction(driver).wait(ms=0).perform():参数是暂停的毫秒数
# 使用坐标的形式点击 WLAN（650, 650），2 秒后，按下（650, 650）的位置，暂停2秒，并抬起。
TouchAction(driver).press(x=650, y=650).wait(2000).release().perform()

# 模拟手指移动操作，比如，手势解锁需要先按下，再移动
# TouchAction(driver).move_to(el=None, x=None, y=None).perform()
# 图案解锁，只是例子没有验证
TouchAction(driver).press(x=150, y=525).move_to(x=450, y=525).move_to(x=750, y=525).move_to(
    x=750, y=825).move_to(x=450, y=825).move_to(x=150, y=825).move_to(x=450, y=1125).release().perform()