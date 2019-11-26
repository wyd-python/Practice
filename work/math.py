#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong

def go_db(self):
    dbs = PrettyTable(["索引", "主机", "端口", "类型", "角色"])
    dbs.align = "l"

    app_list = c.app_list.split("#")
    app_list.remove("")
    db_list = []
    index = -1
    for i in app_list:
        if i.split("|")[4] in ["mongo", "redis", "mysql", "rabbmiq"]:
            if i.split("|")[5] == "master":
                index += 1
                db_list.append(i.split("|"))
                dbs.add_row([index, i.split("|")[3], i.split("|")[7], i.split("|")[4], i.split("|")[5]])
    print dbs
    in_db = raw_input("请输入db索引(不支持以外的):")
    host = db_list[int(in_db)][3]
    port = db_list[int(in_db)][7]
    type = db_list[int(in_db)][4]
    user_passwd = self.get_user_passwd(c.platform.split("#")[0])
    self.connect_db(host, port, type, user_passwd)