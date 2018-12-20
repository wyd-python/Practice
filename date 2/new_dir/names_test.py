#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
"""
names = ["wangyadong", "wuqing", "taoyake", "meizi"]
name2 = [1,2,3,4]
print(names)
names.append("lvyang")
print(names)
names.insert(1,"wangjian")
print(names)
names.remove("wangjian")
print(names)
names.pop()
print(names)
print(names.count("wuqing"))
names.reverse()
print(names)
names.extend(name2)
print(names)
print(names.index("taoyake"))
"""

"""
import copy

a = ["wang", "li", "jun", ["tian", "xia"]]
b = copy.deepcopy(a)
print(a)
print(b)
a[3][0] = "di"
print(a)
print(b)
print(a[0:-1:2])

for i in a:
    print(i)
"""

import copy

persion=['name', ['saving', 100]]

p1=copy.copy(persion)
p2=persion[:]
p3=list(persion)

p4=persion[:]
p5=persion[:]
print(p4)
print(p5)
p4[0]='wang'
p5[0]='li'
persion[1][1]=200
print(p4)
print(p5)