#!/usr/bin/python3
# 打开一个文件
f = open("D:\\buyi_github_project\\learn_python\\python_modules\\foo1.txt", "r")

# str = f.read()
# print(str)

# str1 = f.readline()
# print(str1)

str2 = f.readlines()
print(str2)

f.close()
