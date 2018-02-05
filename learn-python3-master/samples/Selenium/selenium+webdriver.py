#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest
import  HTMLTestRunner
from cgitb import text
from time import sleep
import  time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains#模拟鼠标操作库文件
import  sys
import  importlib
importlib.reload(sys)

"""

登录测试，分下面几种情况：
 3 (1)用户名、密码正确
 4 (2)用户名正确、密码不正确
 5 (3)用户名正确、密码为空
 6 (4)用户名错误、密码正确
 7 (5)用户名为空、密码正确
"""


# class BaiduTest(unittest.TestCase):
#     """百度首页搜索测试用例"""
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://www.baidu.com/"
#
#     def test_baidu_search(self):
#         driver = self.driver
#         print("开始[case_0001]百度搜索")
#
#         driver.get(self.base_url)
#         # driver.Navigate().GoToURL("http://www.baidu.com/")
#         # 验证标题
#         self.assertEqual(driver.title, "百度一下，你就知道")
#
# #浏览器最大化，前进后退等
#         # driver.maximize_window()#最大化
#         # driver.refresh()#刷新
#         # driver.back()#后退
#         # driver.forward()#前进
#         # driver.quit()#退出
#         # driver.find_element_by_id("kw").clear()
#
#         driver.find_element_by_id("kw").send_keys("开源优测")
#
#         driver.find_element_by_id("su").click()
#         driver.get_screenshot_as_file('C:/Users/dujuan/Desktop')
#
# #模拟鼠标操作
#         ActionChains(driver).click()
#
#         # sleep(3)
#         # 验证搜索结果标题
#         self.assertEqual(driver.title, "开源优测_百度搜索")
#
#     def tearDown(self):
#         self.driver.quit()

class yunweiTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(480,960)
        self.driver.implicitly_wait(30)
        self.base_url = "http://221.11.8.54:8180/longieb/user/logout"
    def login(self,username,password):#测试登录
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("pvmts_username").send_keys(username)
        driver.find_element_by_id("pvmts_password").send_keys(password)
        driver.find_element_by_id(u"loginSys").click()
        print("开始测试登录")
    def test_login_success(self):
        self.login("gnrx","123456")
        sleep(5)
        while 1:
             # start = time.clock()
             try:
                username=self.driver.find_element_by_id("username")
                print("已经捕捉到元素")
             except:
                 print("没有捕捉到元素")
        # self.assertTrue('gnrx' in username.text)#用assertTrue(x)方法来断言.登录成功，个人中心显示用户名
        # self.driver.get_screenshot_as_file("C:\\Users\\dujuan\\Desktop\\1.png")#测试结果截图
    def test_login_pwderror(self):
        self.login("gnrx","12455")
        sleep(5)
        # while 1:
        #     try:
        error_message = self.driver.find_element_by_id("tip").text   #//*[@id="tip"]/dl/dd
               # error_message = self.driver.find_element_by_xpath("*[@id='tip']/dl/dd").text
               # print(error_message)
            # except:
            #     print("没有捕捉到元素")
        # print(error_message)
        # self.assertIn("用户名密码错误！",error_message)##用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        # self.assertEqual("用户名密码错误！",error_message)

    def tearDown(self):
        self.driver.quit()
        # self.driver.back()
if __name__ == '__main__':
    unittest.main()
    # testunit = unittest.TestSuite()
    # testunit.addTest(BaiduTest('test_Login'))
    # testYunwei = yunweiTest()
    # testunit.addTest(yunweiTest("test_login_success"))
    # testunit.addTest(yunweiTest("test_login_pwderror"))
    # 定义报告输出路径
    # htmlPath = "E:\\python\\result.html"
    # fp = file(htmlPath, "wb")
    # fp = open(htmlPath,'wb+')
    #
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        title="百度搜索测试",
    #                                        description="测试用例结果")
    #
    # runner.run(testunit)
    #
    # fp.close()