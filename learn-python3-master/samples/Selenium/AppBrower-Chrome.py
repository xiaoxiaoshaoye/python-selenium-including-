#!/usr/bin/env python3
# -*- coding: utf-8 -*
#https://www.jianshu.com/p/f2147add5094
from selenium import webdriver
from  time import  sleep

#chrome
mobileEmulator = {"deviceName":"Apple iPhone 6 Plus"}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulator',mobileEmulator)


#启动driver
driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
# driver = webdriver.Chrome(executable_path="geckodriver.exe",firefox_options=options)



#FireFox

#IE



#访问网页
driver.get("http://www.baidu.com")
sleep(3)
driver.quit()