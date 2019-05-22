#!/usr/bin/python3
# 打开一个文件

f = open("D:\\buyi_github_project\\learn_python\\python_modules\\foo1.txt","r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()