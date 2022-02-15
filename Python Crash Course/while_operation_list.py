#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-06 17:02
# 创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止。
# 将每个经过验证的用户都移到已验证用户的空列表
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verified user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)