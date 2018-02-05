#!/usr/bin/python3
#coding:utf-8
#以163邮箱为例
from  selenium import webdriver
from  time import sleep

"""
iframe是HTML语言中的一个内嵌标签其用法与frame大同小异，
但是作用局不一样，当我们遇到iframe标签中的元素如果不做切换
，就会经常遇到元素找不到这样的错误；
selenium.common.exceptions.NoSuchElementException: 
Message: Unable to locate element: [name="email"]


加上
.switch_to.frame-进入iframe标签
3.switch_to.default_content()-退出iframe标签
这两句话就可以解决

"""


'''
如果iframe标签没有任何属性，例如：id、name则：
iframe=find_element_by_xpath("")
driver.switch_to.frame(iframe)
'''
driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
driver.set_window_size(1000,500)
sleep(2)
#进入iframe

# driver.switch_to_frame("x-URS-iframe") #x-URS-iframe iframe的ID值 ，登录界面的iframe
sleep(2)
driver.find_element_by_name("email").send_keys(u"djjsjxx159@163.com")
driver.find_element_by_name("password").send_keys(u"djjsjxx1599")
driver.find_element_by_id("dologin").click()
# driver.switch_to_default_content()