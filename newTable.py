#!/usr/bin/python3

import getpass
import mysql.connector

"""
#Datos de conexion.
sucursal = input("Sucursal: ").lower()
usr = input("Usuario: ")
pwd = getpass.getpass("Contraseña: ")


#Conexión
mydb = mysql.connector.connect(
  host="localhost",
  user=usr,
  password=pwd
  )"""

def createTables(mydb):
    #mydb: mysql.connector.connect, 

    mycursor = mydb.cursor()

    nueva_sucursal = input("¿Cuál es la nueva sucursal? ")

    suc = nueva_sucursal.upper()[:3]
    mycursor.execute("INSERT INTO adminSucursales.idConstructor VALUES(1,%s)",(suc,))

    mycursor.execute("CREATE DATABASE %s",(nueva_sucursal,))
    mycursor.execute("USE %s",(nueva_sucursal,))

    query2 = """CREATE TABLE clientes(
      id CHAR(9) PRIMARY KEY,
      nombre VARCHAR(250) NOT NULL,
      apellidoPaterno VARCHAR(250),
      apellidoMaterno VARCHAR(250),
      RFC CHAR(13) UNIQUE
      )
      """
    query3 = """CREATE TABLE direcciones(
      id_cliente CHAR(9),
      id INT(6) ZEROFILL NOT NULL AUTO_INCREMENT  PRIMARY KEY,
      calle VARCHAR(250),
      numero INT,
      Colonia VARCHAR(250),
      Estado VARCHAR(250),
      CP CHAR(5),
      FOREIGN KEY (id_cliente) REFERENCES clientes(id)
      )"""

    mycursor.execute(query2)
    mycursor.execute(query3)
    mydb.commit()