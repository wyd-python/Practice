#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
# import time
# def bar():
#     time.sleep(3)
#     print('in the bar')
#
# def test1(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print("the func run time is %s" %(stop_time-start_time))
#
# test1(bar)

import time
def bar():
    time.sleep(3)
    print('in the bar')
def test2(func):
    print(func)
    return func

t=test2(bar)
t()