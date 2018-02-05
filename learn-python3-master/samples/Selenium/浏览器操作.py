#!/usr/bin/env python3
# -*- coding: utf-8 -*
from selenium import webdriver
from  time import  sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.baidu.com")
sleep(3)
driver.find_element_by_xpath("//*[@id='u1']/a[2]").click()
# print(driver.title)

#执行后退操作

driver.back()
print(driver.title)
#
# sleep(3)
#
# #浏览器前进操作
driver.forward()
print(driver.title)
# sleep(3)
#刷新界面
title1 = driver.title
# print(title1)
driver.refresh()
title2 = driver.title
# print(title2)
if title1 == title2:
    print("界面刷新成功")
else:
    print("界面刷新失败")
