#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import  requests
from  json import  dumps

url = "https://www.v2ex.com/api/nodes/show.json"
url2 = "http://www.yunengzhe.com/pvmtsys/noticeInfo/addNotice"
# header = {"token":"DA58A5485E52B2A5DA3EA90F367A1636"}
#get请求
r = requests.get(url)
#post请求
#请求头
head = {
    "token":"DA58A5485E52B2A5DA3EA90F367A1636",
    "Content-Type":"application/json"
}
data = {
    "bodyHtmlText":"我们是一个开放的光伏精准数据平台，在这里你可以找到全国范围内顶级权威的光伏资源气象源数据，在经过我们对源气象数据的处理之后，它将支持你在电站选址、发电量计算、电站投资评估等方面得到精准的结果。",
    "companyId":"1",
    "name":"公告内容1228",
    "remarks":"备注内容1228",
    "status":"1",
    "typeId":"5"
}
#dumps是将dict转化成str格式，loads是将str转化成dict格式。
r2 = requests.post(url2, data=dumps(data),headers=head)#dumps 把str将dict转化成str格式 ，不然会报400 bad request错误


print(r2)
print(r2.text)
# print(r.text,r2.text)




