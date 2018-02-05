#!/usr/bin/env python3
# -*- coding: utf-8 -*
from selenium import  webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
#界面设置的太小，会报错 Element <input id="su" class="bg s_btn" type="submit"> could not be scrolled into view
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)
elemets = driver.find_elements_by_xpath("//*[@id='page']/a")
for element in elemets:
    print(element.text)


driver.quit()
