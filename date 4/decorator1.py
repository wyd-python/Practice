#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

# def foo():
#     print('in the foo')
#     bar()
# foo()
#
# def bar():
#     print('in the bar')
# def foo():
#     print('in the foo')
#     bar()
# foo()

def foo():
    print('in the foo')
    bar()
def bar():
    print('in the bar')
foo()

cacl = lambda x:x*3
print(cacl(3))