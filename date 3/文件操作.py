#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def fetch():
    f = open("test.txt", 'r', encoding="utf-8")
    f_new = open("test_new.txt", 'r', encoding="utf-8")
    fetch_name = input("请输入需要查询的选项：")

    s=0
    for line in f_new:
        if fetch_name in line:
            s +=1
    if s == 0:
        print("没有你查找的选项")
    else:
        print("文件里面有你查找的选项，一个出现了%s次" % s)
def add():
    pass

def change():
    f = open("test.txt",'r',encoding="utf-8")
    f_new = open("test_new.txt",'w',encoding="utf-8")

    for line in f:
        if "万象" in line:
            # print(line)
            line = line.replace(line,"哦哦哦\n")
            # print(line)
            # print(line)
            f_new.write(line)
        else:
            f_new.write(line)
    f.close()
    f_new.close()

def delete ():
    pass

change()
fetch()