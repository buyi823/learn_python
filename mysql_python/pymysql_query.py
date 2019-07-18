#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","root","123456","TESTDB")

cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
    cursor.execute(sql)
    # 获取所有记录
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
               (fname,lname,age,sex,income))
except:
    print("Error: unable to fech data")

db.close()