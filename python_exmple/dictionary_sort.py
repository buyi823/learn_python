#!/usr/bin/python3
#  按键(key)或值(value)对字典进行排序
def dictionary():
    #声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 

    print("按键（key）排序：")

    # sorted(key_value)返回一个迭代器
    # 字典按键排序
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")

def main():
    # 调用主函数
    dictionary()

if __name__=="__main__":
    main()