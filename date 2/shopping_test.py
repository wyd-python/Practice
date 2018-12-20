#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
product_list = [
    ("xiaomi",4000),
    ("Iphone",8000),
    ("Mac pro",10000),
    ("video",300),
    ("people",3000)
]
shopping_list = []
salary = input("请输入你的薪水：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("请输入你要买商品的编号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            print(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -=p_item[1]
                    print("你购买了%s,剩余的钱还有%s" %(p_item,salary))
                else:
                    print("购买的物品价钱是%s,你剩余的钱是%s" %(p_item[1],salary))
            else:
                print("请输入正确的编号")
        elif user_choice == "q":
            print("-------- shopping_list --------")
            for shop in shopping_list:
                print(shop)
                print("你还剩余%s块钱" %(salary))
            print("欢迎下次再来")
            exit()
else:
    print("请输入数字：")