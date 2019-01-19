#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
import time
user,passwd = 'wangqing','123456'

def auth(auth_type): #func=index
    print("auth is ",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("Username: ").strip()
                password = input("Password: ").strip()

                if user == username and passwd == password:
                   print("\033[32;1mUser has passed authentication\033[0m")
                   res = func(*args, **kwargs)
                   print("----hi---")
                   return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                print("ldap还没接通，以后再用")
        return wrapper
    return outer_wrapper



@auth(auth_type="local")
def index():
    print("welcome to index page")
@auth(auth_type="ldap") #
def home():
    print("welcome to home page")
    return "from home"
# @auth
# def bbs():
#     print("welcome to bbs page")

index()
home()
#bbs()