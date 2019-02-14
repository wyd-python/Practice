#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
a = ( i*2 for i in range(1000) )

b = a.__next__()
print(b)
b = a.__next__()
print(b)