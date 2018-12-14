#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

#import sys

#print(sys.path) #打印环境变量

#print(sys.argv[2])

import os

cmd_res = os.system("ls -l") #执行命令。不保存结果
cmd_res = os.popen("ls").read()
print("-->",cmd_res)
os.mkdir("new_dir")