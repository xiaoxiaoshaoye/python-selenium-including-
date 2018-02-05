#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  sys
from  selenium import webdriver
from selenium.webdriver.common.by import  By
from POM.pages.basePage import Page

class searchPage(Page):
        # 搜索输入框
        search_input = (By.ID,u'kw')
        # 按钮
        search_button = (By.ID,u'su')
        def __init__(self,driver,base_url=u'http://www.baidu.com'):
            Page.__init__(self,driver,base_url)
        def gotoBaiduHomePage(self):
            print("跳转到百度首页")
            self.driver.get(self.baseurl)
        def input_search_text(self,text="python"):
             print("输入关键字进行搜索")
             self.input_text(self.search_input,text)
        def click_search_text(self):
            print("开始搜索")
            self.click(self.search_button)
