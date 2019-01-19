#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#
# foo()
#
# def test1():
#     foo()
#
# test1()

x=0
def grandpa():
    x=1
    print('grandpa is %s' % x)
    def bad():
        x=2
        print('bad is %s' % x)
        def son():
            x=3
            print('son is %s' % x)
        son()
    bad()
grandpa()