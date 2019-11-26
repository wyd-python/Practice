#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

import yaml
import sys


def get_section(id, global_redis, game_redis, game_mongo, public_ip):
    file = open("/Users/playcrab/Desktop/sections.json", "r")
    section = yaml.load(file)
    b = section[str(id)].get("global_redis")
    c = section[str(id)].get("game_redis")
    d = section[str(id)].get("game_mongo").split("?", 1)[0]
    e = section[str(id)].get("public_ip")
    global_redis.strip()
    game_redis.strip()
    game_mongo.strip()
    public_ip.strip()
    if global_redis == b and game_redis == c and game_mongo == d and public_ip == e:
        print "%s: 信息正确"
    else:
        print "信息有误"



get_section(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])