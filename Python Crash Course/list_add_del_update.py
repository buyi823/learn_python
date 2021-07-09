#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2021-07-08 22:54:53
# Description: modify add delete List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'初始列表：{motorcycles}')
motorcycles[0] = 'ducati'  # 将列表第一个元素替换
print(f'替换第一个元素后：{motorcycles}')

motorcycles.append('ducati')  # 在列表末尾添加
print(f'在列表末尾添加元素后：{motorcycles}')

# 可以新建一个空列表然后使用append()添加
motorbike = []
motorbike.append('honda')
motorbike.append('yamaha')
motorbike.append('suzuki')
print(f'使用append()方法新建的列表：{motorbike}')
# 在列表中添加元素
motorbike.insert(1, 'ducati')
print(f'使用insert()方法在列表中添加元素：{motorbike}')
# 删除列表中的元素 del list[index]
del motorbike[1]
print(f'使用del语句删除元素：{motorbike}')
# pop()删除列表末尾的元素，并能让你接着使用它
# list就像一个栈，删除列列表末尾的元素相当于弹出栈顶元素
popped_motorbike = motorbike.pop()
print(f'使用pop()方法删除末尾元素后：{motorbike}')
print(popped_motorbike)
# pop()可以删除列表中任意位置的元素
first_owned = motorbike.pop(1)
print(f'The first motorcycle I owned was a {first_owned.title()}')
# 如果你要从列表中删除一个元素，且不再以任何方式使用它，那么就使用del语句；
# 如果你要在删除元素后还能继续使用它，就使用方法pop()

# 根据列表中的值删除元素
list_bike = ['giant', 'cannondale', 'merida', 'feige']
print(list_bike)
list_bike.remove('feige')
print(list_bike)
