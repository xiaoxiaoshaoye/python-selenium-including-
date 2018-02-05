#!/usr/bin/env python3
# -*- coding: utf-8 -*
from  selenium import webdriver
from  selenium.webdriver.common.keys import  Keys
import time
#访问百度
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#搜素
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
#将页面滚动条拖到底部
time.sleep(3)
#通过按向下键将页面滚动条拖到底部
#将滚动条移动到页面的底部
js="var q=document.documentElement.scrollTop=10000000"
#将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)

#如下方法web程序内置浏览器的滚动条使用
#https://www.jianshu.com/p/73a3e5a978c1
#http://blog.csdn.net/u013372487/article/details/46503169
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)
# time.sleep(3)
# driver.quit()