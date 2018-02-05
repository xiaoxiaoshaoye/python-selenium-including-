#!/usr/bin/env python3
# -*- coding: utf-8 -*

from  selenium import webdriver
from  time import  sleep
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.yunengzhe.com/")
driver.find_element_by_xpath("//*[@id='log']/ul/li[1]/a").click()
for handle in driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
       driver.switch_to_window(handle)
       sleep(3)

driver.find_element_by_id("username").send_keys("zhimin")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("buttonLogin").click()
