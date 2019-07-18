#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","root","123456","TESTDB")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()