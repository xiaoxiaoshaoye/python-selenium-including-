#!/usr/bin/env python3
# -*- coding: utf-8 -*
#https://www.jianshu.com/p/c6e82df841f9
from  selenium import  webdriver
import  time
import  os
#访问百度
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.maximize_window()#窗口最大化
time.sleep(3)
#获取百度首页句柄

current_windows = driver.current_window_handle

#打开第一条对应链接
driver.find_element_by_xpath('//*[@id="u1"]/a[1]').click()

time.sleep(3)
#获取所有句柄
all_handles = driver.window_handles
for handle in  all_handles:
    if handle != current_windows:
        driver.switch_to_window(handle)
print(u"切换句柄成功")
time.sleep(3)
driver.quit()

