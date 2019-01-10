#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def calc(n):
    print(n)
    if int(n/2) >0:
        return  calc(int(n/2))
calc(100)