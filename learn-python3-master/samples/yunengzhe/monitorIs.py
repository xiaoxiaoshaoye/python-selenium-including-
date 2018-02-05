#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from  time import sleep
import  os
import  datetime

class service_test(object):
        def init__test(self):
           driver = webdriver.Firefox()
           driver.maximize_window()
           driver.get("http://www.yunengzhe.com/")
        def timerFun(self, sched_Timer):
            flag = 0
            while True:
                now = datetime.datetime.now()
                if now == sched_Timer:
                    self.init__test()
                    flag = 1
                else:
                   if flag == 1:
                      # self.init__test()
                      sched_Timer = sched_Timer + datetime.timedelta(minutes=1)
                      flag = 0
        def re_exe(cmd, inc=60):
            while True:
                os.system(cmd);
                sleep(inc)
if __name__ == "__main__":
    print("运行")
    cs = service_test()
    sched_Timer = datetime.datetime(2018,1,24,15,0) ## 用指定日期时间创建datetime
    cs.timerFun(sched_Timer)
    cs.re_exe("此昂啊",1)




