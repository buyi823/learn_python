#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-08-21:16:56
# functions practice

def get_formatted_name(first_name, last_name):
    """return clean name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 让实参变成可选的

def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Return dictionary

def build_persion(first_name, last_name, age=None):
    """return a dictionary, it's include a person's information"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_persion('jimi', 'hendrix', age=27)
print(musician)

# 综合练习

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")