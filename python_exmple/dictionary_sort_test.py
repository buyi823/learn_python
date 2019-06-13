#!/usr/bin/python3
#  按键(key)或值(value)对字典进行排序
def dictionary():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[7] = 18
    key_value[3] = 323

    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))
    print(sorted(key_value.items(), key=lambda kv: (kv[0], kv[1])))

def main():
    dictionary()


if __name__ == "__main__":
    main()