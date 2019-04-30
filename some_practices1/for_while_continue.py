#!/usr/bin/python

for letter in 'Runoob':
    if letter == 'o':
        continue
    print('当前字母: ', letter)

var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('当前变量值： ', var)
print('good bye')