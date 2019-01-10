#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def add(x,y,f):
    return f(x)+f(y)

res = add(3,-6,abs)
print(res)