#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
"""
#names = "wuqing wangyadong taoyake"
names = ["wuqing", "wangyadong", "taoyake","meizi"]
names.append("xinxin")
#names.append("xinxin")
#names.append("xinxin")
names.insert(1,"xiaowu")
print(names)
names[1]="qingwu"
names.remove("meizi")
print(names)
names.pop(0)
print(names)
print(names.count("xinxin"))
#print(names.index("wuqing"))
#print(names[names.index("wuqing")])
#print(names[0],names[2])
#print(names[1:])
names.reverse()
print(names)
names2 = [1,2,3,4]
names.extend(names2)
del names2
print(names)
"""
"""
import copy
names = ["wuqing", "wangyadong", "taoyake",["wangjian","lvyang"],"meizi"]
name2 = copy.deepcopy(names)
print(names)
print(name2)
names[0] = "吴清"
names[3][0] = "王建"
print(names)
print(name2)
"""