#!/usr/bin/env python3
import cgi
import cgitb

print("Content-type:text/html")
print()  # 空行，告诉服务器结束头部
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>hello world - 我的第一个CGI程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
print('</body>')
print('</html>')