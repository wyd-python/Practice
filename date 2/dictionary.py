#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
#key-valus
#info = {
#    'stu1101': "TengLan lan",
#    'stu1102': "LongZe luola",
#    'stu1103': "XiaoZe MaLiya"
#}
"""
print(info)
#print(info["stu1103"])

info["stu1101"] = "bdyjy"
info["stu1104"] = "cangjk"
print(info)

#del
#del  info["stu1101"]
#info.pop("stu1102")
info.popitem()#随便删
print(info)
"""

#print(info.get('stu1104'))
#print('stu1102' in info)
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

"""print(A0)

A1 = range(10)

print(A1)
A2 = [i for i in A1 if i in A0]
print(A2)
"""
A=8
B=9
if 'a' in A0:
    print(A)
else:
    print(B)