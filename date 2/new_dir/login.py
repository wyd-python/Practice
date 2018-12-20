#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

msg = "吾爱吾妻"

print(msg)

print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))