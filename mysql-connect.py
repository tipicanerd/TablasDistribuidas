#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="bdd",
  password="basesDatosD-2021"
  )

mycursor = mydb.cursor()

vals = (1,'Mara')

query =  "INSERT INTO test. Employees VALUES (%s, %s)"

mycursor.execute(query, vals)

mycursor.execute("SELECT * FROM test.Employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
