#!/usr/bin/env python3
# -*- coding: utf-8 -*
#https://pypi.python.org/pypi/PyUserInput

from  pymouse import PyMouse,PyMouseEvent
from  pykeyboard import  PyKeyboard,PyKeyboardEvent
from selenium import webdriver
#创建鼠标和键盘对象
#打开百度
# driver = webdriver.Firefox()
# driver.get("Http://www.baidu.com")
# driver.maximize_window()
m = PyMouse()
k = PyKeyboard()
#实例，点击屏幕中央并输入HelloWorld
x_dim,y_dim = m.screen_size()
print(x_dim,y_dim)
# m.position()
# m.click(x_dim//2,y_dim//2,1)#鼠标点击
7# k.press_key('H')#键盘输入
# k.release_key('H')#释放键盘
# k.tap_77key('e',777n=H1,interval=5)#n表示输入的个数，interval表示每次输入的间隔
#特殊按键输入
# k.press_key(k.alt_key)
# k.tap_key(k.tab_key)
# k.tap_key(k.numpad_keys['Home'])#点击Home键
# k.tap_key(k.function_keys[12],n=3)#Tap F12
# k.press_keys([k.windows_l_key,'d'])#组合键发送 command +d 回到桌面

#PyMouseEvent,PyKeyboardEvent用于监听，不做任何操作
def fibo():
     a = 0
     yield  a
     b = 1
     yield  b
     while True:
          a,b = b,a+b
          yield  b

class Clickonacci(PyMouseEvent):
        def __init__(self):
            PyMouseEvent.__init__(self)
            self.fibo = fibo()

        def click(self, x, y, button, press):
            '''Print Fibonacci numbers when the left click is pressed.'''
            if button == 1:
                if press:
                    print(self.fibo)
            else:  # Exit if any other mouse button used
                self.stop()

c = Clickonacci()
c.run()

