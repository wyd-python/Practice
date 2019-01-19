#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import time

def kehu(name):
    print("%s,准备吃包子啦" % name)
    while True:
        baozi = yield
        print("包子[%s]被【%s]吃掉啦！" %s (baozi,name))

def dianjia(name):
