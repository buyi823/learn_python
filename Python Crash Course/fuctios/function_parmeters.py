#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-07 16:30
# 位置实参, 需要注意掉哟给顺序

def describe_pet(animal_type, pet_name='dog'):
    # 函数参数指定了默认值，调用时不赋值就使用默认值
    '''display pets information'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
describe_pet('dog', 'paopao')

# 关键字实参，需要赋值
describe_pet(animal_type='cat', pet_name='mimi')
