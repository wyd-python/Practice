#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n +=1
    return 'down'
f = fib(10)

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print("----------")

# for i in f:
#     print(i)

while True:
    try:
        x = next(f)
        print('g:',x)
    except StopIteration as e:
        print('General return valus:', e.value)
        break