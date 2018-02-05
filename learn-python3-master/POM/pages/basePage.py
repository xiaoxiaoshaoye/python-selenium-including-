#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#page基类
import  sys
from  selenium import webdriver
class Page(object):
    """
    page 是基类，所有的page都应该继承该类

    """
    def  __init__(self,driver,baseurl=u"http://www.baidu.com"):
        self.driver = driver
        self.baseurl = baseurl
        self.timeout = 30
    def find_element(self,*loc):#参数个数和类型不确定的时候使用 * 参数名 的格式
         return  self.driver.find_element(*loc)
    def input_text(self,loc,text):
         self.find_element(*loc).send_keys(text)
    def click(self,loc):
         self.find_element(*loc).click()
    def get_title(self):
        return  self.driver.title




