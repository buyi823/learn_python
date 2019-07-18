#!/usr/bin/python3
import re

line = "Cats are smater than dogs"
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
# re.I 不区分大小写

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(): ", matchObj.group(1))
    print("matchObj.group(): ", matchObj.group(2))
    # group() 同group（0）就是匹配正则表达式整体结果
    # group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
else:
    print("No match!!")