#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# author: wangyadong
n, a, b = 0, 0, 1
all = [a, b]
while b < 100:
    a, b = b, a + b
    if b > 100:
        break
    all.append(b)

print all
