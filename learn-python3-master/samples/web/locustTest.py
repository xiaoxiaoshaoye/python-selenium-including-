#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from locust import  TaskSet,HttpLocust,task,web,events
class UserBehaviorTest(TaskSet):
    @task(1)
    def baidu(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):#WebsiteUser()类用于设置性能测试
    task_set = UserBehaviorTest #获取用户行为 指向一个定义了的用户行为类。
    min_wait = 3000 #最小等待时间  毫秒
    max_wait = 6000 #最大等待时间  毫秒
    host = "http://221.11.8.54:8180/longieb/index/6.do?powerStationId=6"


#--no-web是用来选择无浏览器模式，-c后面接的是模拟用户数，-r后面接的每秒模拟用户并发数，-n后面接的是模拟请求数。
