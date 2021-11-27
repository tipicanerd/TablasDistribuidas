#!/usr/bin/python3

import getpass
import mysql.connector

"""#Datos de conexion.
sucursal = input("Sucursal: ").lower()
usr = input("Usuario: ")
pwd = getpass.getpass("Contraseña: ")


#Conexión
mydb = mysql.connector.connect(
  host="localhost",
  user=usr,
  password=pwd
  )

mycursor = mydb.cursor()"""

def insertDirecciones(mydb,sucursal,n):
    #mydb: mysql.connector.connect, 
    #sucursal: str, sucursal
    #n: int, cantidad de direcciones a insertar.

    mycursor= mydb.cursor()

    id_dir = 1
  
    for i in range(n):
        print("-"*20)
        id_cliente = input("id del cliente: ")
        calle = input("Calle: ")
        numero = int(input("No.: "))
        Colonia = input("Colonia: ")
        Estado = input("Estado: ")
        CP= input("CP: ")

        
        insertQuery = f"INSERT INTO {sucursal}.direcciones VALUES{id_cliente, id_dir, calle, numero, Colonia, Estado, CP}"
        #print(insertQuery)
        values = (id_cliente, calle, numero, Colonia, Estado, CP)

        mycursor.execute(insertQuery)
        mydb.commit()

        print("Se han insertado la dirección: ",values)
        print("En la sucursal",sucursal)
        print("-"*20)


def insertCientes(mydb,sucursal,n):
    #sucursal: str, sucursal
    #n: int, cantidad de clientes a insertar.
    
    mycursor= mydb.cursor()

    suc = sucursal.upper()[:3]
    mycursor.execute("SET @suc=%s",(suc,))
  
    for i in range(n):
        print("-"*20)
        Nombre = input("Nombre: ")
        ApellidoPaterno = input("Apellido Paterno: ")
        ApellidoMaterno = input("Apellido Materno: ")
        RFC = input("RFC: ")

        
        mycursor.execute("EXECUTE idGen USING @suc")

        mycursor.execute("SELECT @lastid")

        idCliente = mycursor.fetchall()[0][0]
        insertQuery = f"INSERT INTO {sucursal}.clientes VALUES{idCliente,Nombre,ApellidoPaterno, ApellidoMaterno, RFC}"
        #print(insertQuery)
        values = (idCliente,Nombre,ApellidoPaterno, ApellidoMaterno, RFC)

        mycursor.execute(insertQuery)

        mycursor.execute("EXECUTE idUp USING @suc")

        mydb.commit()

        print("Se hainsertado al cliente: ",values)
        print("En la sucursal",sucursal)
        print("-"*20)


def insertRegistro(mydb,sucursal):
    #mydb: mysql.connector.connect
    #sucursal: str, sucursal desde la que se trabaja.

    mycursor= mydb.cursor()

    #Prepare Staments auxiliares
    mycursor.execute("PREPARE idGen FROM 'SET @lastid = (SELECT CONCAT(base,number) FROM adminSucursales.idConstructor WHERE base=?)'")
    mycursor.execute("PREPARE idUp FROM 'UPDATE adminSucursales.idConstructor SET number= number+1 WHERE base=?';")

    tabla = input('¿Qué deseas agregar? (cliente|dirección) ')

    n = int(input('¿Cuántos registros vas a añadir? '))

    if tabla=='cliente':
      insertCientes(mydb,sucursal,n)
    elif tabla=='dirección':
      insertDirecciones(mydb,sucursal,n)
