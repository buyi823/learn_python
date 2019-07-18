#!/usr/bin/python3

import pymysql

# connect database
db = pymysql.connect("localhost","root","123456","TESTDB") 

# use cursor() method
cursor = db.cursor()

# sql insert
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME,AGE,SEX,INCOME)
         VALUES('Mac','Mohan',20,'M',2000)"""

"""
# 上面SQL语句也可以写成这样
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,\
       LAST_NAME, AGE, SEX, INCOME)\
       VALUES ('%s','%s','%s','%s','%s')" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
"""
try:
    cursor.execute(sql)
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

db.close()

