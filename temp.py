# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:50:19 2020

@author: hnyangzy
"""

import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456',db='student')
cursor=db.cursor()
input_id='admin'
input_pass=0
sql="select * from admin_login_k where admin_id= '%s'" % (input_id)
cursor.execute(sql)
rescult=cursor.fetchall()
for row in rescult:
    id=row[0]
    password=row[1]
    print('%s:%s'% (id,password))
input_id='001'
input_name='simple'
input_gender='男'
input_age=14
sql="insert into student_k (id,name,gender,age) values ('%s','%s','%s','%s')" % (input_id,input_name,input_gender,input_age)
cursor.execute(sql)
db.commit()
sql="select * from student_k"
cursor.execute(sql)
rescult=cursor.fetchall()
for row in rescult:
    id=row[0]
    name=row[1]
    gerder=row[2]
    age=row[3]
    print('%s,%s,%s,%s' % (id,name,gerder,age))
