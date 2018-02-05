#!/usr/bin/python3
from  selenium import  webdriver
import  sys
import  time
import  datetime#获取当前日期
import  unittest

from  selenium.common.exceptions import NoSuchElementException

class testDayExport(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.base_url = "http://221.11.8.54:8180/longieb/"
        # self.base_url = "http://test.yunengzhe.com:846/aotai/"
    def login(self,username,password):#测试登录
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("pvmts_username").send_keys(username)
        driver.find_element_by_id("pvmts_password").send_keys(password)
        driver.find_element_by_id(u"loginSys").click()
        # self.driver.switch_to_window(self.driver.window_handles[0])
        print("开始登录")

    def testdayExport(self):
        # self.login("gnrx","123456")
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("pvmts_username").send_keys("gnrx")
        driver.find_element_by_id("pvmts_password").send_keys("123456")
        driver.find_element_by_id(u"loginSys").click()
        driver.find_element_by_id("remberPass").click()
        # driver.find_element_by_id(u"aotai_username").send_keys("jtadmin")
        # driver.find_element_by_id(u"aotai_password").send_keys("123456")
        # # self.driver.find_element_by_id(u"loginButton").click()
        # driver.find_element_by_xpath("//*[@id='loginButton']").click()
        # driver.find_element_by_id("remeberPass").click()
        time.sleep(10)
        print("登录成功")
        time.sleep(3)
        # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
        #     self.driver.switch_to_window(handle)
        #
        # # current_windows = self.driver.current_window_handle
        # # # 获取所有句柄
        # # all_handles = self.driver.window_handles
        # # for handle in all_handles:
        # #     if handle != current_windows:
        # #         self.driver.switch_to_window(handle)
        # # print(u"切换句柄成功")
        # # self.driver.switch_to_window(self.driver.window_handles[0])
        # # self.driver.find_element_by_css_selector("//*[@id='reportDailyTable']/thead/tr/th[2]")
        # # self.driver.find_element_by_xpath("//*[@id='tuModule']").click()
        # self.driver.find_element_by_id("listModule").click()
        # time.sleep(5)
        # # self.driver.find_element_by_css_selector("#powerStationIcon > div:nth-child(1) > div > div > div > a > img").click()
        # # self.driver.find_element_by_class_name("bgMapBtn").click()
        # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
        #     self.driver.switch_to_window(handle)
        #     time.sleep(5)
        #
        # self.driver.find_element_by_xpath("//*[@id='powerStationList']/a[2]/li/span[1]").click()
        # time.sleep(3)
        # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
        #     self.driver.switch_to_window(handle)
        #     time.sleep(5)
        #
        # try:
        #   self.driver.find_element_by_xpath("//*[@id='report_everyday']/a/span").click()
        # except Exception as e:
        #    print(e)
        #
        #
        # time.sleep(5)
        # for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
        #     self.driver.switch_to_window(handle)
        #     time.sleep(5)
        #
        # str = self.driver.find_element_by_xpath("//*[@id='reportDailyTable']/tbody/tr[1]/td[2]").text
        # print(str)
        # print("检查每日报表是否是最新的")
        # today = datetime.date.today()
        # yestoday = today + datetime.timedelta(days=-1)
        # print(today, yestoday)
        # self.assertEqual(str,yestoday,"每日报表生成成功")

        #文件上传

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
