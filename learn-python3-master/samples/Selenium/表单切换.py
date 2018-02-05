#!/usr/bin/env python3
# -*- coding: utf-8 -*

from  selenium import  webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.126.com")
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()
"""
#先通过xpth定位到iframe
xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')

#再将定位对象传给switch_to.frame()方法
driver.switch_to.frame(xf)
……
driver.switch_to.parent_frame()
"""