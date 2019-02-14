#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import json

def sayhi(name):
    print("hello,",name)

info = {
    'name':'wang',
    'age':'18',
}
f = open("text.text","w")
f.write( json.dumps(info))

f.close()