#!/usr/bin/env python3
# -*- coding: utf-8 -*
from  selenium import  webdriver

class screen(object):
    #捕捉图片的装饰器
    # driver = webdriver.Firefox()

    def __init__(self,driver):
        self.driver = driver


    def __call__(self,f):#类可以作为实例被调用
        def innner(*args):
            try:
                return  f(*args)
            except:
                import  time
                nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("%s.jpg"%nowtime)
                raise
                # 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。
                # 一旦执行了raise语句，raise后面的语句将不能执行
        return  innner
import  unittest
class Test(unittest.TestCase):
    driver = webdriver.Firefox()
    def setUp(self):
        self.driver.get("http://www.baidu.com")
    @screen(driver)
    def test01(self):
        print("这是一个失败的案例")
        self.driver.find_element_by_id("11kw").send_keys("python")
        self.driver.find_element_by_id("su").click()
    @screen(driver)
    def test02(self):
        print("这是一个成功的案例")
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()