#!/usr/bin/python3

import getpass
import mysql.connector

from insert import insertRegistro
from update import updateRegistro


def printMenu():
    print("1. Insertar registros")
    print("2. Actualizar registros")
    print("3. Consultar registros")
    print("4. Crear nueva sucursal")
    print("5. Salir")


#Datos de conexion.
sucursal = input("Sucursal: ").lower()
usr = input("Usuario: ")
pwd = getpass.getpass("Contraseña: ")


#Conexión
mydb = mysql.connector.connect(
  host="localhost",
  user=usr,
  password=pwd
  )

#mycursor = mydb.cursor()

printMenu()
op = int(input("¿Qué quieres hacer? ")) 

while op>0 or op<=5:
    if op==4 or op==5:
        print("Aún no está implementado")
        break
    elif op==1:
        insertRegistro(mydb,sucursal)
    elif op==2:
        updateRegistro(mydb,sucursal)
    printMenu()
    op = int(input("¿Qué quieres hacer? "))

print("Gracias por usar el programa")