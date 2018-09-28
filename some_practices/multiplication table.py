# multiplication table

# 完整表
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2d' % (i,j,i*j),end='  ')
    print('')


print('-----------------------------------------------------------------------')

# 左上三角形表
for i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%2d' % (i,j,i*j),end='  ')
    print('')

print('-----------------------------------------------------------------------')

# 右上三角形表
for i in range(1,10):
    for k in range(1,i):
        print(end='        ')
    for j in range(i,10):
        print('%d*%d=%2d' % (i,j,i*j),end='  ')
    print('')

print('-----------------------------------------------------------------------')

# 左下三角形表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d' % (i,j,i*j),end='  ')
    print('')

print('-----------------------------------------------------------------------')

# 右下三角形表
for i in range(1,10):
    for k in range(1,10-i):
        print(end='        ')
    for j in range(1,i+1):
        product = i*j
        print('%d*%d=%2d' % (i,j,i*j),end='  ')
    print(' ')