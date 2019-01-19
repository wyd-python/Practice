#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import time
#
# def deco(func):
#     start_time=time.time()
#     return func
#     stop_time=time.time()
#     print('the runing time is %s' %(stop_time-start_time))


def timer(fun):#timer(test1) func=test1
    def deco(*args,**kwargs):
        start_time = time.time()
        fun(*args,**kwargs)  # run test1
        stop_time = time.time()
        print('the runing time is %s' % (stop_time - start_time))
    return deco
@timer  #等同于test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')
@timer
def test2(name):
    time.sleep(3)
    print('test2 name is ', name)
test1()
test2("dong")