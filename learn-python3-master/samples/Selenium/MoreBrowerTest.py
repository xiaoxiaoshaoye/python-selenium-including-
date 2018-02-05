#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# #为了能在同一台机器上不同浏览器上同时执行测试用例，我们需要多线程技术

#方法一暂时出现问题
# from selenium import webdriver
# import  sys
# from  time import sleep
# from  threading import Thread
# import  _thread
# import  threading
# import  pytest
# import  unittest
# # class  testBaidu_search(unittest.TestCase):
#
# def testbaidu_search(cache,capfd):
#       driver = None
#       if cache =="ie":
#           driver = webdriver.Ie()
#       elif cache == "firefox":
#           driver = webdriver.Firefox()
#       elif cache == "chrome":
#            driver == webdriver.Chrome()
#       print("hahhahahhahh")
#       if cache == None:
#          exit()
#          print("开始搜索")
#          driver.get(capfd)
#          print(u"开始输入查询条件")
#          driver.find_element_by_id("kw").clear()
#          driver.find_element_by_id("kw").send_keys("hahhah")
#          print(u"开始搜索")
#          driver.find_element_by_id("su").click()
#          driver.quit()
#
#
#
# if __name__ == "__main__":
#     # pytest.main("MoreBrower.py")
#     data={
#          "ie":"http://www.baidu.com",
#          "firefox":"http://www.baidu.com",
#          "chrome":"http://www.baidu.com"
#
#     }
#     # t = threading.Thread(target=testbaidu_search, args=("firefox","http://www.baidu.com"))
#     # t.run()
#     # # 构建线程
#     threads = []
#     for b, url in data.items():
#         # t = Thread(target=testBaidu_search, args=(b, url))
#         t= threading.Thread(target=testbaidu_search,args=(b,url))
#         threads.append(t)
#         # 启动所有线程
#     for thr in threads:
#         thr.start()

#方法二亲测可行
#import os
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# test case
def testbrowser(driver):
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").click()
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys("vx")
    driver.find_element_by_id("su").click()
    driver.implicitly_wait(30)
    time.sleep(3)
    driver.close()
    driver.quit()
    return None

driverfirefox = webdriver.Firefox()
testbrowser(driverfirefox)

driverie = webdriver.Ie()
testbrowser(driverie)

driverchrome = webdriver.Chrome()
testbrowser(driverchrome)