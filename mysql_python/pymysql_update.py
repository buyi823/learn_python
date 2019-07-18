#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","root","123456","TESTDB")

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()