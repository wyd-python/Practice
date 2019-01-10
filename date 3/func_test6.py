#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

# def test(host,port=3306):
#     print(host,port)
#
# test(1)
#
# def test2(x,y):
#    print(x)
#    print(y)
# test2(2,3)
#
# def test3(*args):
#     print(args)
# test3(1,2,3,4,5)
#
# def test4(x,*args):
#     print(x)
#     print(args)
# test4(1,2,3,4,5,6)
#
# def test5(name,**kwargs):
#     print(name)
#     print(kawargs)
# test5('wang',age=20,sex='a')

def test(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)
    logger("jjjj")

def logger(source):
    print("from %s" %source)

test('wang',sex='a',boy='yadong',age=3)
