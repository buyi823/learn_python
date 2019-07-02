#!/usr/bin/python3
# 定义一个变量rows并赋值想要打印正方形的边长
rows = 5
# 外层for循环控制打印的行数
for x in range(rows):
    # 通过if语句判断行数，筛选出第一行和最后一行
    if x == 0 or x == rows - 1:
        # 内层for循环打印正方形上下两边
        for y in range(rows):
            print(' *', end='')
# else获取剩余行数
    else:
        # for循环打印
        for y in range(rows):
            # if语句判断列，筛选出第一列和最后一列打印 *
            if y == 0 or y == rows - 1:
                print(' *', end='')
# else获取剩余列，打印空格
            else:
                print('  ', end='')
# 换行
    print('')
