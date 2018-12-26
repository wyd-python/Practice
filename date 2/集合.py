#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

list_1 = [1,3,2,4,23,2,34]
list_1 = set(list_1)
list_2 = set([2,6,3,2,7,5])

print(list_1,list_2)

#交集
list_1.intersection(list_2)
print(list_1.intersection(list_2))

#并集
print(list_1.union(list_2))

#差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))

#子集
list_3 = set([2,3])
print(list_1.issuperset(list_3))

list_1.add(999)
print(list_1)

if 99 in list_1:
    print("yes")
else:
    print("no")