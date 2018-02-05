#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder
import  sys
import  time
#连接设备
#第一个参数为等待连接设备时间
#第二个参数为具体连接的设备
device=mr.waitForConnection(2,'192.168.209.101:5555')
# recorder.start(device)
if not device:
    print(sys.stderr,"fail")
    sys.exit(2)#退出
device.installPackage('D:\\android-release.apk')#测试apk路径
# device.installPackage("D:\\apk\\app-universal-debug.apk")
# device.removePackage("testtecentpush.dujuan.testtecentdemo")
#启动APP
device.wake()
device.startActivity(component="com.yunengzhe.yunweiapp/.MainActivity")#教训，如下是错误的写法
#device.startActivity("component=com.yunengzhe.yunweiapp/.MainActivity")
# device.startActivity(component="testtecentpush.dujuan.testtecentdemo/.MainActivity")

device.touch(200,200,"DOWN_AND_UP")
# #点击回车键
device.press('KEYCODE_ENTER','DOWN_AND_UP')
#
#
# #截图
result=device.takeSnapshot()
# #保存到文件
result.writeToFile('D:/test.png','png')
#
# device.press('KEYCODE_DEL','DOWN_AND_UP')
# mr.sleep(2)