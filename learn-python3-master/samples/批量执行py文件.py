
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import  os
def exepy():
    allList = os.listdir(os.getcwd())
    for lists in allList:
        if os.path.isfile(lists) and lists.endswith('.py') and lists.find('__init__') == -1:
            cmd = 'python'+lists
            try:
                os.popen(cmd)
                print("执行%s文件成功"%lists)
            except:
                print("执行%s文件失败"%lists)

