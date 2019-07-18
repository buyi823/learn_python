#!/usr/bin/python3
import re

# re.search 扫描整个字符串并返回第一个成功的匹配
# re.search(pattern, string, flags=0)
# 匹配成功re.search方法返回一个匹配的对象，否则返回None。
# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。 匹配对象方法	描述 group(num=0)
# 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

print(re.search('www', 'www.runoob.com').span())
print(re.search('com','www.runboo.com').span())

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print("SearchObj.group(): ", searchObj.group())
    print("SearchObj.group(): ", searchObj.group(1))
    print("SearchObj.group(): ", searchObj.group(2))
else:
    print("Nothing found!")