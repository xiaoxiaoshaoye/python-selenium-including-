#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://www.cnblogs.com/znyyy/p/7999283.html
# https://www.cnblogs.com/znyyy/p/7999283.html
#多线程实现并发
import  requests,threading,time
res_time = []#存放响应时间
global time2#全局变量
class restime_test(object):
    def __init__(self,url):
        self.url = url
    def send_req(self):
        #开始时间
        start_time = time.time()
        r = requests.get(self.url)
        # requests.adapters.DEFAULT_RETRIES = 1000
        s = requests.session()
        s.keep_alive = False#关闭多余的连接
        end_time = time.time()
        res_time.append(end_time-start_time)
        time2 = (end_time-start_time)

url='http://www.yunengzhe.com/'
print(url)
bfs=5000
test=restime_test(url)
# print(time2)

print(res_time)
t_list=[]
for i in range(bfs):
    t = threading.Thread(target=test.send_req)
    t_list.append(t)
    t.start()
    # print(t_list)
    for t in t_list:#线程依次加入1,，12,123,1234,12345
         t.join()#子线程执行完成在执行主线程
         # print(444444)
avg=sum(res_time)/len(res_time) #单位秒
print("aahahahh")
print(avg)