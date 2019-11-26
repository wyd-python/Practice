#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import yaml
def get_section(section):
    file = open("/Users/playcrab/Desktop/sections.json", "r")
    a = yaml.load(file)
    print a[str(section)]


get_section(50016)
