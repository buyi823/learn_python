#!/usr/bin/python3
#随机函数

import random
print(random.choice(range(10)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# 从 1-100 中选取一个奇数
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
 
# 从 0-99 选取一个随机数
print ("randrange(100) : ", random.randrange(100))

print('random():', random.random())


#改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed
random.seed()
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())

#shuffle() 方法将序列的所有元素随机排序。

list=[20,16,10,5]
random.shuffle(list)
print("随机排序列表：", list)

random.shuffle(list)
print ("随机排序列表 : ",  list)

#uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。

print ("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))
print ("uniform(7, 14) 的随机浮点数 : ",  random.uniform(7, 14))
