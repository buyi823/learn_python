#!/usr/bin/python3
import re

# re.sub(pattern, repl, string, count=0, flags=0)
"""
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。
"""

phone = "2004-959-559 # this is a phone number"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码：", num)

# 移除非数字内容
num = re.sub(r'\D', "", phone)
print("电话号码：", num)


