#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

name = "my name is wangyadong, age is 27"
name2 = "my name is {name}, age is {age}"

print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("g"))
#print(name.expandtabs(tabsize=10))
print(name[name.find("name"):])
print(name2.format(name='wangyadong',age='27'))
print(name2.format_map( {'name':'wangyadong','age':27}))
print('23'.isdigit())
print('wangud ksk\n'.strip())
print('-----')