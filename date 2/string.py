#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

name = "my name is {name}, age is {age}"

print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("g"))
#print(name.expandtabs(tabsize=10))
print(name[name.find("name"):])
print(name.format(name='wangyadong',age='27'))
print(name.format_map( {'name':'wangyadong','age':27}))