#！/usr/bin/python3

for letter in 'Runoob':
    if letter == 'b':
        break
    print('当前字母为：', letter)

var = 10
while var > 0:
    print('当前变量为： ', var)
    var = var - 1
    if var == 5:
        break

print('good bye!')