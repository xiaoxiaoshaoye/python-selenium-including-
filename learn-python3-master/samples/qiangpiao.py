
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  splinter.browser import Browser
from  time import sleep


# 设定用户名，密码
username =u"abcdujuan"
password = u"dj19930201"

startCity = "%u5317%u4EAC%2CBJP"
endCity = "%u4E0A%u6D77%2CSHH"

time = "2017-12-26"
order = 1#预订第一个车次,如果为0则预订离现在时间最近有票的车次  

#设定网址
tikcet_url = "http://www.12306.cn/mormhweb/"
login_url = "https://kyfw.12306.cn/otn/leftTicket/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

def qiangpiao():
    # global  b
    b = Browser(driver_name="firefox")
    b.visit(tikcet_url)
    while b.is_text_present(u"登录"):
        sleep(1)
        b.find_by_text(u"登录").click()
        sleep(3)

        #用于自动登录，username是12306账号名，passwd是12306密码
        b.fill("loginUserDTO.username",abcdujuan)
        sleep(1)
        b.fill("userDTO.password",dj19930201)
        sleep(1)
        print(u"等待验证码，请输入、、、")
        sleep(10)
        if b.url == initmy_url:
            break
            try:
                b.visit(tikcet_url)
                b.cookies.add({"_jc_save_fromDate": time})
                b.cookies.add({"_jc_save_fromStation":startCity})
                b.cookies.add({"_jc_save_toStation":endCity})
                b.reload()
                b.find_by_text(u"查询").click()
                if order != 0:
                    while b.url == tikcet_url:
                        b.find_by_text(u"预定")[order -1].click()
                        b.find_by_text("").click()
                    else:
                        while b.url == tikcet_url:
                            for i in  b.find_by_text(u"预定"):
                                i.click()
                                b.find_by_text("").click()
                                print(u"等待验证码输入")
            except Exception as  e:
                print (str(e))

if __name__ == "__main__":
      qiangpiao()
