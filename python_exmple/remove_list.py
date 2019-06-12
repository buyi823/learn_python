#!usr/bin/python3
# 移除字符串中的指定位置字符

test_str = 'runoob'

# Printing original string
print("原始字符串为：", test_str)

# 移除第三个字符n
new_str = ""

for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("字符串移除后为 : " + new_str)
