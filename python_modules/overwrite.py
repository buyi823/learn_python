#!/usr/bin/python3

# 打开一个文件
f = open("D:\\buyi_github_project\\learn_python\\python_modules\\foo1.txt", "w")

num = f.write( "Python是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()