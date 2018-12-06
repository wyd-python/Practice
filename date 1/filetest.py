#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import sys,os
import getpass

count = 0

while count < 3:
    name = input("请输入用户名： ")
    lock_file = open('kes.txt','r+')
    lock_list = lock_file.readlines()

    for lock_line in lock_list:
        lock_online = lock_line.strip('\n')
        print(lock_online)
        if name == lock_online:
            sys.exit('用户 %s 已经被锁定，退出' % (name))

    user_file = open('user_p.txt','r')
    user_list = user_file.readlines()

    for lock_user in user_list:
        (user,password) = lock_user.strip('\n').split( )

        if name == user:
            j = 0
            while j < 3:
                passwd = input('请输入密码： ')
                if passwd == password:
                    print("欢迎登录!",name)
                    sys.exit()
                else:
                    if j != 2:
                        print("用户或密码错误，密码错误，请重新输入密码，还有%d次机会" % (2-j))
                j += 1
            else:
                lock_file.write(name + '\n')
                sys.exit('用户登录次数已打最大登录次数，将被系统锁定，请联系管理员！')
        else:
            pass
    else:
        if count != 2:
            print('用户名%s不存在，请从新输入！' % name)
        count += 1
else:
    sys.exit("用户%s不存在，退出" % name)

lock_file.close()
user_file.close()
