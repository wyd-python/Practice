#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import getpass

_username = 'wangyadong'
_passwd = '123456'
username = input("username: ")
passwd = getpass.getpass("passwd: ")

print (username,passwd)

if _username == username and _passwd == passwd:
    print("Welcome use {name} login...".format(name=username))
else:
    print("Invalid username or passwd!")