#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
"""
age_of_oldboy = 56

count = 0
while count <3:
    guess_age = int(input("guess age: "))

    if guess_age == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")
    count +=1
    print(count)
else:
    print("you have tried too times....fuck off")
"""

"""
for i in range(0,10):
    if i < 5:
        print("loop",i)
    else:
        print("i is ",i)
"""


for i in range(10):
    print('---------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break