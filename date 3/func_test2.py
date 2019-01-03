#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
import time
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    print(time_format)
    print(time_current)
    with open('a.txt','a+') as f:
        f.write('%s end action\n' %time_current)
def test1():
    print("test1 staring action")
    logger()
def test2():
    print('test2 staring action')
    logger()
def test3():
    print('test3 staring action')
    logger()
def test4():
    print("你好")
    logger()
test1()
test2()
test3()
test4()