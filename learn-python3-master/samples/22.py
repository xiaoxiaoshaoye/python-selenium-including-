
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import android
import pprint
droid=android.Android()
pacs=droid.getRunningPackages()
pprint.pprint(pacs.result)

from splinter.browser import Browser
b = Browser(driver_name="firefox")
b.visit("http://www.12306.cn/mormhweb/")