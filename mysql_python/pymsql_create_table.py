#!/usr/bin/python3

import pymysql

# open mysql connect
db = pymysql.connect("localhost", "root", "123456", "TESTDB")

# cursor() 
cursor = db.cursor()

# 使用execute（）方法执行SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# create table
sql = """CREATE TABLE EMPLOYEE(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)"""

cursor.execute(sql)

# close db
db.close()