#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-10 11:06
# 传递列表

def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

username = ['hannah', 'ty', 'margot']
greet_user(username)
