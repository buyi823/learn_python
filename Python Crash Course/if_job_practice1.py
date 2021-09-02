#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-08-30 15:24
# if job practice

users = ['admin', 'john', 'michael', 'phoebe', 'monica', 'karl']
if users:  # 判断列表是否为空
    print("we need to find some users")
for i in range(len(users)):
    if users:
        users.pop()
    print(users)

users = ['admin', 'john', 'michael', 'phoebe', 'monica', 'karl']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f"Hello {user}, thank you for logging in again.")
