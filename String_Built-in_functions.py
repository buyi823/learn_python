#!/usr/bin/python3
#Python 的字符串内建函数

#Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。
str = "this is string example from runoob....wow!!!"
print("str.capitalize(): ", str.capitalize())

#center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
str="[www.runoob.com]"
print("str.center(40, '*')", str.center(40,'*'))

#count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
str="www.runoob.com"
sub='o'
print("str.count('o'): ", str.count(sub))

sub='run'
print("str.count('run',0,10):", str.count(sub,0,10))

#decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

#endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，
#否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。
Str='Runoob example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))

#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
str = "this is\tstring example....wow!!!"
print ("原始字符串: " + str)
print ("替换 \\t 符号: " +  str.expandtabs())
print ("使用16个空格替换 \\t 符号: " +  str.expandtabs(16))


"""
find() 方法检测字符串中是否包含子字符串 str ，
如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。
如果不包含索引值，返回-1
"""
str1 = "Runoob example....wow!!!"
str2 = "exam";
 
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))

"""
index() 方法检测字符串中是否包含子字符串 str ，
如果指定 beg（开始） 和 end（结束） 范围，
则检查是否包含在指定范围内，该方法与 python find()方法一样，
只不过如果str不在 string中会报一个异常。
"""

str1 = "Runoob example....wow!!!"
str2 = "exam";

print (str1.index(str2))
print (str1.index(str2, 5))
# print (str1.index(str2, 10))

#isalnum() 方法检测字符串是否由字母和数字组成。
str = "runoob2016"  # 字符串没有空格
print (str.isalnum())
 
str = "www.runoob.com"
print (str.isalnum())

#isalpha() 方法检测字符串是否只由字母组成。
str = "runoob"
print (str.isalpha())

str = "Runoob example....wow!!!"
print (str.isalpha())

#isdigit() 方法检测字符串是否只由数字组成。
str = "123456"; 
print (str.isdigit())

str = "Runoob example....wow!!!"
print (str.isdigit())

#islower() 方法检测字符串是否由小写字母组成。
str = "RUNOOB example....wow!!!"
print (str.islower())

str = "runoob example....wow!!!"
print (str.islower())

#isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
str = "runoob2016"  
print (str.isnumeric())

str = "23443434"
print (str.isnumeric())

#isspace() 方法检测字符串是否只由空白字符组成。
str = "       " 
print (str.isspace())
 
str = "Runoob example....wow!!!"
print (str.isspace())

#istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
str = "This Is String Example...Wow!!!"
print (str.istitle())
 
str = "This is string example....wow!!!"
print (str.istitle())

#isupper() 方法检测字符串中所有的字母是否都为大写。
str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.isupper())

str = "THIS is string example....wow!!!"
print (str.isupper())

#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))

#ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
#如果指定的长度小于原字符串的长度则返回原字符串。
str = "Runoob example....wow!!!"
print (str.ljust(50, '*'))

#lstrip() 方法用于截掉字符串左边的空格或指定字符。
str = "     this is string example....wow!!!     ";
print( str.lstrip() );
str = "88888888this is string example....wow!!!8888888";
print( str.lstrip('8') );

"""
maketrans() 方法用于创建字符映射的转换表，
对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，
第二个参数也是字符串表示转换的目标。
两个字符串的长度必须相同，为一一对应的关系。
注：Python3.4 已经没有 string.maketrans() 了，
取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。
"""
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))


