#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import time

def consumer(name):
    print("%s,准备吃包子啦" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被【%s]吃掉啦！" % (baozi,name))

# c = consumer("wuqing")
# c.__next__()
# b1="韭菜馅"
# c.send(b1)
# #c.__next__()
def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print("老子开始准备做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c1.send(i)
        c2.send(i)

producer("taoyake")

