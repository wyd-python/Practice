#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
count = 0
while count <3:
    age_of_oldboy = 56
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