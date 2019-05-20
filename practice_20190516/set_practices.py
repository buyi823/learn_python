#!/usr/bin/python3

basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

i = 'orange' in basket
print(i)

a = set('abracadabra')
b = set('alacazam')
print(a)

print(a-b) # 在 a 中的字母，但不在 b 中
print(a | b)  # 在 a 或 b 中的字母
print(a & b)  # 在 a 和 b 中都有的字母
print(a ^ b) # 在 a 或 b 中的字母，但不同时在 a 和 b 中

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)