#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  sys
import  unittest
from  selenium import webdriver
from  POM.pages.searchPage import  searchPage
import  HTMLTestRunner
# import  file


class TestSearchPage(unittest.TestCase):
       def setUp(self):
            self.driver = webdriver.Firefox()
       def testSearch(self):
           driver =  self.driver
           url = u'http://www.baidu.com'
           text = u'python'
           assert_title = u"百度一下，你就知道"
           print("hahhah"+assert_title)
           search_page = searchPage(driver,url)
           search_page.gotoBaiduHomePage()
           search_page.input_search_text(text)
           search_page.click_search_text()
           # 验证标题是否正确
           print(search_page.get_title())
           self.assertEqual(search_page.get_title(),assert_title)

       def tearDown(self):
            self.driver.quit()
if __name__ == "main":
    testunit = unittest.TestSuite()
    testunit.addTest(TestSearchPage('testSearch'))
    # htmlPath = u'pom.html'
    htmlPath = "E:\\python\\pomresult.html"
    # fp = file(htmlPath, "wb")
    fp = open(htmlPath,'wb+')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="百度搜索测试",
                                           description="测试用例结果")

    runner.run(testunit)

    fp.close()

