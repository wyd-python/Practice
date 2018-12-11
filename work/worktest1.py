#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import sys

count = 0
while count < 3:
    user = input("请输入用户名： ")
    lock_file = open('kes.txt','r+')
    lock_list = lock_file.readlines()
    for lock_line in lock_list:
        lock_online = lock_line.strip('\n')
        if user == lock_online:
            sys.exit("用户已被锁定，请联系管理员！")

    user_file = open('user_p.txt','r+')
    user_list = user_file.readlines()

    for user_line in user_list:
        (username,password) = user_line.strip('\n').split( )
        if user == username:
            count_p = 0
            while count_p < 3:
                passwd = input("请输入密码： ")
                if passwd == password:
                    print("欢迎再次登录！")
                    sys.exit()
                else:
                    if count_p != 2:
                        print("账号或密码错误，你还有%d次机会" % (2-count_p))
                count_p +=1
            else:
                lock_file.write(user + '\n')
                sys.exit("用户或密码已输入最大次数，账号已被锁定，请联系管理员")
        else:
            pass
    else:
        if count != 2:
            print("用户名或密码错误，请重新输入")
        count +=1
else:
    sys.exit("用户名不存在")

lock_file.close()
user_file.close()






