#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def test01():
    pass
def test02():
    return 0
def test03():
    return 0,10,'hello',['wang','10'],{'wanghs': '11'}

t1=test01()
t2=test02()
t3=test03()

print("from test01 return is [%s]: " %type(t1),t1)
print("from test02 return is [%s]: " %type(t2),t2)
print("from test03 return is [%s]: " %type(t3),t3)