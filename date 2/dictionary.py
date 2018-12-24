#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
#key-valus
info = {
    'stu1101': "TengLan lan",
    'stu1102': "LongZe luola",
    'stu1103': "XiaoZe MaLiya"
}
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

print(info.get('stu1104'))
print('stu1102' in info)