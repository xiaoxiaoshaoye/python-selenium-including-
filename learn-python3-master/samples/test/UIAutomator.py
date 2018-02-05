#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uiautomator import device as  d  #as d 代表 定义了一个device变量
from  uiautomator import  Device
import  time
import sys
import random
import unittest
import HTMLTestRunner
import  logging
import  jsonrpc
import jsonrpcserver


#APP
class MyTest_Suit(unittest.TestCase):
        # d = Device("192.168.209.101:5555")

        d.screen.on()
        d(text="Camera").click()#打开系统邮箱，Email是桌面app的名字
        # d(classname="android.widget.TextView").click()
        # print(jsonrpcserver.Methods)
        # d(text="Email address").set_text("juan.du@yunengzhe.com")
        # d(classname="android.widget.EditText").set_text("Ynz12345")
        # d(text="Manual setup").click()

        # phone_number = random.choice(['139', '152', '185', '133']) + "".join(random.choice("0123456789") for i in range(8))
        # def setUp(self):
        #     try:
        #         d.press.home()
        #         d(text="***").click()
        #         time.sleep(2)#休眠2秒
        #         if d(text="我的").exists:
        #             d(text="我的").click()
        #             d(text="注销").click()
        #             d(text="确定").click()
        #             d(text="登录").click()
        #         if d(text="登录").exists:
        #             d(resourceId="com.isentech.attendance:id/title_back").click()
        #         else:
        #              time.sleep(2)
        #              print(u"开启app")
        #              logging.info("开启app")
        #
        #     except Exception as e:   #3.0之前的写法 except Exception, e:
        #          print(u"app开启失败")
        #
        #
        #
        # def test_register(self):#测试注册
        #      try:
        #          d(text="注册").click()
        #          d(text="请输入手机号").set_text("15210142172")#测试已经注册账号
        #          # d(text="获取验证码").click()
        #          d(text="测试注册").click()#测试注册
        #          d(text="请输入手机号").set_text(phone_number)
        #          d(text="请输入验证码").set_text("6666")
        #          d(resourceId="com.isentech.attendance:id/regis_pass").set_text("123456")
        #          d(resourceId="com.isentech.attendance:id/regis_passAgain").set_text("123456")
        #          d(text="注册").click()
        #          time.sleep(2)
        #          if  d(text="立刻去登录").exists:
        #              d(text="立即去登录").click()
        #              d(resourceId="com.isentech.attendance:id/txtLoginPassword").set_text("123456")
        #              d(text="登录").click()
        #      except Exception as  e:
        #          print(u"注册失败",e)
        #
        # def test_login(self, phone):
        #     try:
        #         d(text="登录").click()
        #         # d(resourceId="com.isentech.attendance:id/txtLoginUserName").clear_text()
        #         d(resourceId="com.isentech.attendance:id/txtLoginUserName").set_text("yw003")
        #         d(resourceId="com.isentech.attendance:id/txtLoginPassword").set_text("123456")
        #         d(text="登录").click()
        #         # d(text="请输入您的姓名").set_text("123456")
        #         # d(text="完成").click()
        #         # time.sleep(2)
        #         # if d(text="签到").exists:
        #         print(u"登录成功")
        #     except Exception as e:
        #         print(u"Error: 登录失败\n", e)
        #
        # def tearDown(self):
        #     try:
        #         d.press.home()
        #         d.press.recent()
        #         time.sleep(3)
        #         d.swipe(200, 500, 200, 0, steps=10)
        #         d.press.home()
        #         print
        #         u"关闭APP"
        #     except Exception as  e:
        #         print(u"Error: 关闭APP失败\n", e)




if __name__ == "__main__":#该模块作为程序直接被运行，如下执行代码中的变量都会被执行

    phone_number = random.choice(['139', '152', '185', '133']) + "".join(random.choice("0123456789") for i in range(8))
    test_unit = unittest.TestSuite()
    test_unit.addTest(MyTest_Suit("test_register"))
    # 定义报告输出路径
    htmlPath = "E:\\python\\result.html"
    # fp = file(htmlPath, "wb")
    fp = open(htmlPath, 'wb+')#3.0之后的写法

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="app测试",
                                           description="测试用例结果")

    runner.run(test_unit)
