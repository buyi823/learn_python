#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root","123456","TESTDB")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("Database version: %s" % data)

# 关闭数据库连接
db.close()