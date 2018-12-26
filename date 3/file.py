#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
f = open("test.txt",'r',encoding="utf-8")
print(f.tell())
print(f.read(5))
print(f.tell())

#f.write("\nsiw skadis s a isa 。。。。，\n")
#f.write("我爱你家")
"""
print(f.readline())
print(f.readline())
for i in range(5):
    print(f.readline())

for index,line in enumerate(f.readlines()):
    if index == 4:
        print('------我是分割线------')
        continue
    print(line.strip())
"""
count = 0
for line in f:
    if count == 4:
        print("-----我是分割符----")
        count +=1
    print(line.strip())
    count +=1