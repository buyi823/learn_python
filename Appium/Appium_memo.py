#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-12-01 16:30
# Appium 总结 
# memorandum

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.support.wait import WebDriverWait

# 这个不运行，只是个例子

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

# 获取元素的方法
driver.find_element_by_id()   # 对应 resource-id
driver.find_element_by_class_name()  # 对应 class name 
# 名字不唯一，可以使用下标定位 如:
driver.find_elements_by_class_name('android.widget.TextView')[1].click()
driver.find_element_by_accessibility_id() # 对应 content-desc
# xpath定位可以分为两种，绝对定位和相对定位
# 绝对定位的路径非常的长，后期代码也比较麻烦，开发中几乎不可能使用

# 1. 如果当前class内存在唯一text可以定位元素，直接用当前class+text，例如：
element = driver.find_element_by_xpath('//android.widget.TextView[@text="排行"]')
TouchAction(driver).tap(element).perform()
# 2. 如果当前class内，resource-id、text两者能唯一定位元素，直接用当前class+两者并列，例如
element1 = driver.find_element_by_xpath('//android.widget.TextView[@text="我的游戏"]')
TouchAction(driver).tap(element1).perform()
time.sleep(2)
element2 = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.taptap:id/app_title" and @text="第五人格T"]')
TouchAction(driver).tap(element2).perform()
time.sleep(5)
# 3. 如果当前class内，text中的文本内容不是完全符合，但能匹配部分内容，可用当前class+模糊定位contains，例如：
element = driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"我的")]')
TouchAction(driver).tap(element).perform()
time.sleep(2)
# refer to 六张表 搞定 Xpath 语法 https://blog.csdn.net/Dome_/article/details/80638245

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

# 等待操作
# TouchAction(driver).wait(ms=0).perform():参数是暂停的毫秒数
# 使用坐标的形式点击 WLAN（650, 650），2 秒后，按下（650, 650）的位置，暂停2秒，并抬起。
TouchAction(driver).press(x=650, y=650).wait(2000).release().perform()

# 模拟手指移动操作，比如，手势解锁需要先按下，再移动
# TouchAction(driver).move_to(el=None, x=None, y=None).perform()
# 图案解锁，只是例子没有验证
TouchAction(driver).press(x=150, y=525).move_to(x=450, y=525).move_to(x=750, y=525).move_to(
    x=750, y=825).move_to(x=450, y=825).move_to(x=150, y=825).move_to(x=450, y=1125).release().perform()


# Refer to https://blog.csdn.net/feizhixuan46789/article/details/16801429
# Press HOME = adb shell input keyevent 3
driver.press_keycode(3)
driver.press_keycode(5) # dial button

# 当前网络类型
driver.network_connection
# 设置网络类型
driver.set_network_connection(1) # 设置飞行模式

# 截图
driver.get_screenshot_as_file("screen.png")

# 获取手机分辨率
driver.get_window_size()

# 操作手机通知栏
driver.open_notifications()

# 当前package和activity
driver.current_package
driver.current_activity

# 安装应用
# driver.install_app("path")
# 卸载应用
# driver.remove_app(app_id)
# 检查应用是否安装
# driver.is_app_installed(app_id)
    
# E.G. 
if driver.is_app_installed("com.tencent.android.qqdownloader"):
    driver.remove_app("com.tencent.android.qqdownloader")
else:
    driver.install_app("d:\yingyongbao.apk")
    
    
# 在脚本内启动其他应用
driver.start_activity('appPackage', 'appActivity')

# 关闭应用 
# 这种关闭呢，是关闭驱动对象，同时关闭所有关联的应用，关闭后我们是无法使用脚本操作应用的。
driver.quit()

# 我们只想关闭当前操作的应用，不关闭驱动对象，我们就可以使用driver.close_app()方法。
driver.close_app()

# 重置应用  相当于“恢复出厂默认值”的效果
driver.reset()

# 将应用置于后台
driver.background_app(seconds)

# 我们在使用脚本的时候，可能会由于网络、服务器处理、电脑等原因，我们想要找的元素没有加载出来，这个时候如果直接定位就可能会报错。
# 这个时候我们就可以设置元素等待了。
# 什么叫元素等待呢？
# 就是WebDriver定位页面元素时如果没有找到，就会在指定时间内一直等待的过程。
# 元素等待一共分为两种类型：显示等待和隐式等待。
driver.implicitly_wait(5)

# 显示等待就是为需要等待的元素分别设置不同的值。
# 等待元素加载指定的时长，超出时长抛出TimeoutException异常。
# WebDriverWait(driver, timeout, poll_frequency=0.5)：
# 参数分别是驱动对象、超时时长、检测间隔时间，检测间隔时间默认是0.5秒。
# wait.until(method)：参数为lambda查找元素表达式。
# 需要导入 from selenium.webdriver.support.wait import WebDriverWait

# 在5秒钟内，每1秒在《设置》中的“返回”按钮，如果找到则点击，如果找不到则观察对应错误信息。
# 第一种
driver.find_element_by_id('com.android.settings:id/search').click()
wait = WebDriverWait(driver, 25, 5)
# 第二种
back_button = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath("//*[@content-desc='收起']"))
back_button.click()
# 第三种
WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath("//*[@content-desc='收起']")).click()