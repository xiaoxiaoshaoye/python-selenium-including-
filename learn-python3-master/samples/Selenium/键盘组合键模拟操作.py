#!/usr/bin/env python3
# -*- coding: utf-8 -*
from  selenium import  webdriver
from  selenium.webdriver.common.keys import  Keys#组合键
from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.action_chains import  ActionBuilder
from  time import  sleep

driver = webdriver.Firefox()
# driver.set_window_size(800,500)
driver.maximize_window()
driver.get("http://www.baidu.com")
sleep(3)
# driver.find_element_by_id('kw').send_keys(u'白醋')
#ctrl+A 全选
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL+'A')
#backspace-删除操作 两种写法都是正确的。一次只能删除一个字符
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
#鼠标操作
"""
click(on_element=None) ——单击鼠标左键

click_and_hold(on_element=None) ——点击鼠标左键，不松开

context_click(on_element=None) ——点击鼠标右键

double_click(on_element=None) ——双击鼠标左键

drag_and_drop(source, target) ——拖拽到某个元素然后松开

drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

key_down(value, element=None) ——按下某个键盘上的键

key_up(value, element=None) ——松开某个键

move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

move_to_element(to_element) ——鼠标移动到某个元素

move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

perform() ——执行链中的所有动作

release(on_element=None) ——在某个元素位置松开鼠标左键

send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素 
"""
element = driver.find_element_by_id('kw')
element2 = driver.find_element_by_id('su')
# ActionChains(driver).click(element2).perform()#单击
# ActionChains(driver).double_click(element2).perform()#双击
# ActionChains(driver).context_click(element).perform()#鼠标右击
# targetEelement=driver.find_element_by_class_name("mnav")
# targetEelement=driver.find_element_by_name("tj_trhao123")
# ActionChains(driver).move_to_element(targetEelement).perform()
sleep(3)
# ActionChains(driver).move_by_offset(200,100).perform()
#拖拽
action = ActionChains(driver)
action.drag_and_drop(element,element2).perform()#目标移动到目标2
#与上边语句作用一致
# action.click_and_hold(element).release(element2).perform()
#将目标1拖拽到指定坐标下
# action.click_and_hold(element).move_by_offset(100, 88).release().perform()
sleep(2)
# action.drag_and_drop_by_offset(element2,500,500)