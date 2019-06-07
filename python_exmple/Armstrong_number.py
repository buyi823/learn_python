#!/usr/bin/python3
# Python 检测用户输入的数字是否为阿姆斯特朗数

num = int(input('请输入一个数字: '))

sum = 0
# 指数
n = len(str(num))

# 检测
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**n
    temp //= 10

# 输出结果
if num == sum:
    print(num, "是安姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")
