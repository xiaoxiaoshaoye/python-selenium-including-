#!/usr/bin/env python3
# -*- coding: utf-8 -*
from  selenium import  webdriver
from  time import sleep

"""

1.IE浏览器
# -*- coding: utf-8 -*-


from selenium import webdriver

'''
IE浏览器：
设置Desired Capabilities的acceptSslCerts选项为True

'''

capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
capabilities['acceptSslCerts'] = True
driver = webdriver.Ie(capabilities=capabilities)
driver.get('https://www.baidu.com')
2.FireFox浏览器
# -*- coding: utf-8 -*-


from selenium import webdriver

'''
FireFox浏览器：
设置FirefoxProfile()的accept_untrusted_certs的选项为True

'''

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://www.baidu.com')
3.Chrome浏览器 
# -*- coding: utf-8 -*-


from selenium import webdriver

'''
Chrome浏览器：
设置ChromeOptions()的--ignore-certificate-errors选项为True
'''

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get('https://www.baidu.com')
"""




# profile = webdriver.FirefoxProfile()
# profile.accept_untrusted_certs = True
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.maximize_window()
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.baidu.com/")
