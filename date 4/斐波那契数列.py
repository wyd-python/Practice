#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def fib(max):
    n, a, b = 0, 0, 1
    all = [n, a, b]
    while b < max:
        a, b = b, a + b
        all.append(b)
        return all
f = fib(100)
print f