#!/usr/bin/python3

tel = {'jack': 4098, 'sape': 4139}
print('dic: ', tel)
tel['guido'] = 4127
print('new dic: ', tel)

del tel['sape']
print('del tel: ',tel)

print(list(tel.keys()))
print(sorted(tel.keys()))

print('guido' in tel)
print('jack' not in tel)

# 字典推导可以用来创建任意键和值的表达式词典
print({x: x**2 for x in (2, 4, 6)})

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
print(dict(sape=4139, guido=4127, jack=4098))

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0} ? It is {1}.'.format(q,a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] 
for f in sorted(set(basket)):
    print(f)
 