#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-07 10:39
# 使用用户输入来填充字典

responses = {}

# 设置一个标志，指出调查是否继续。
polling_active = True

while polling_active:
    name = input("\nwhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #  将回答存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Polling Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
