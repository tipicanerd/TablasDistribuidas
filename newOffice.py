#!/usr/bin/python3

import getpass
import mysql.connector
from sucursalesGen import *
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
    sucursales = getSucursales(mydb)
    sucursales = [s.lower() for s in sucursales]
    mycursor = mydb.cursor()
    while(True):
      nueva_sucursal = input("¿Cuál es la nueva sucursal? ")
      if(nueva_sucursal):
        if(nueva_sucursal.lower() not in sucursales):
          print(f"Se creó la sucursal {nueva_sucursal}")
          break
        else:
          print(f"La sucursal ya se encuentra en el sistema, use otro nombre")

    suc = nueva_sucursal.upper()[:3]
    mycursor.execute("INSERT INTO adminSucursales.idConstructor VALUES(1,%s)",(suc,))

    mycursor.execute(f"CREATE DATABASE {nueva_sucursal}")#,(nueva_sucursal,))

    mycursor.execute(f"INSERT INTO adminSucursales.sucursales (nombre) VALUES ('{nueva_sucursal}')")

    mycursor.execute(f"USE {nueva_sucursal}")#,(nueva_sucursal,))

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
