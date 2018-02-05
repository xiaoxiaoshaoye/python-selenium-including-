#!/usr/bin/env python3
# -*- coding: utf-8 -*
from selenium import  webdriver
import  os
import  unittest
import  time
from win32 import win32gui
import win32con

#打开上传功能页面,打开本地html文件
driver = webdriver.Firefox()
# file_path =  'file:///' + os.path.abspath('upfile.html')
# driver.get(file_path)
# print("打开本地html文件")
# #点击打开上传窗口
# driver.find_element_by_name("file").click()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.click()
time.sleep(1)
# win32gui
# dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
# ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
# ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
# Edit = win32gui.FindWindowEx(ComboBoxEx32, 1, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
# button = win32gui.FindWindowEx(ComboBoxEx32, 1, 'Button', None)  # 确定按钮Button
#
# win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:/Users/dujuan/Desktop/images/泰州用户头像.jpg')  # 往输入框输入绝对地址
# win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\test.png')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

print (upload.get_attribute('value'))
driver.quit()


#AutoIT
#调用upfile.exe上传程序
# os.system("C:\\Users\\dujuan\\Desktop\\1.exe")
print("上传成功")
# time.sleep(10)
# driver.quit()


# class testUpload(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.set_window_size(1000, 500)
#         # self.driver.get("http://test.yunengzhe.com:846/aotai/")
#         self.base_url = "http://test.yunengzhe.com:846/aotai/"
#     def testupload(self):
#         self.driver.get(self.base_url)
#         self.driver.find_element_by_id("aotai_username").send_keys("jtadmin")
#         self.driver.find_element_by_id("aotai_password").send_keys("123456")
#         # self.driver.find_element_by_id(u"loginButton").click()
#         print("开始登录")
#         self.driver.find_element_by_id("loginButton").click()
#         self.driver.find_element_by_id("remeberPass").click()
#         print("开始登录88888888")
#         time.sleep(3)
#         # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
#         #     self.driver.switch_to_window(handle)
#         #     time.sleep(5)
#         # self.driver.find_element_by_class_name(u"userName").click()
#         # time.sleep(5)
#         # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
#         #     self.driver.switch_to_window(handle)
#         #     time.sleep(5)
#         # self.driver.find_element_by_class_name(u"title").click()
#         # time.sleep(5)
#         # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
#         #     self.driver.switch_to_window(handle)
#         #     time.sleep(5)
#         # self.driver.find_element_by_id(u"uploadBtn").click()
#         # os.system(r"C:\Users\dujuan\Desktop\1.exe")
#     def tearDown(self):
#         self.driver.quit()
# if __name__ == '__main__':
#     testUpload()
#     unittest.main()