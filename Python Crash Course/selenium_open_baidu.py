#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-09 22:16:23
# Description: Selenium learn

import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOpenbaiduinput123():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
    
    def test_openbaiduinput123(self):
        self.driver.get("https://www.baidu.com/?tn=48021271_39_hao_pg")
        self.driver.set_window_size(1024, 768)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        self.driver.find_element(By.ID, "su").click()
        element = self.driver.find_element(By.LINK_TEXT, "采购")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "123(自然数之一) - 百度百科").click()
        self.vars["win2150"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2150"])
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()



