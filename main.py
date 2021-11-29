#!/usr/bin/python3

import getpass
import mysql.connector

from insert import insertRegistro
from update import updateRegistro
from newOffice import createTables
from select_ import selectDatos
from sucursalesGen import *

def printMenu():
    print("1. Insertar registros")
    print("2. Actualizar registros")
    print("3. Consultar registros")
    print("4. Crear nueva sucursal")
    print("5. Cambiar de sucursal")
    print("6. Imprimir sucursales actuales")
    print("7. Salir")


#Datos de conexion.
#sucursal = input("Sucursal: ").lower()
usr = input("Usuario: ")
pwd = getpass.getpass("Contraseña: ")


#Conexión
mydb = mysql.connector.connect(
  host="localhost",
  user=usr,
  password=pwd
)

sucursales = getSucursales(mydb)
sucursal = initSucursal(mydb, sucursales)

#mycursor = mydb.cursor()


printMenu()
op = int(input("¿Qué operación desea realizar? ")) 

while(True): 
    if op==3:
        selectDatos(mydb)

    elif op==1:
        insertRegistro(mydb,sucursal)

    elif op==2:
        updateRegistro(mydb,sucursal)

    elif op == 4:
        createTables(mydb)
        sucursales = getSucursales(mydb)

    elif op == 5:
        sucursal = changeSucursal(mydb,sucursal,sucursales)

    elif op == 6:
        printSucursales(mydb,sucursales,sucursal)

    elif op == 7:
        break
    printMenu()
    op = int(input("¿Qué operación desea realizar? "))

print("Gracias por usar el programa :)")