#!/usr/bin/python3

import getpass
import mysql.connector

sucursales = ['apatzingan','morelia']

def updateDirecciones(mydb,sucursal,n):
    #sucursal: str, sucursal
    #n: int, cantidad de direcciones a actualizar.

    mycursor= mydb.cursor()

    campos = ['id','calle', 'numero', 'Colonia', 'Estado', 'CP']

    for i in range(n):
        print("-"*20)
        idCliente = input("¿Cuál es el id del cliente? ")

        query1 = "SELECT * FROM {}.direcciones WHERE id_cliente=%s".format(sucursal)

        mycursor.execute(query1,(idCliente,))

        print(f"El cliente {idCliente} tiene las direcciones")

        
        for direccion in mycursor.fetchall():
            print("-"*20)
            for i in range(len(campos)):
                print(campos[i],":",direccion[i+1])
        print("-"*20)

        id_dir = input("¿Cuál es el id de la dirección del cliente que quieres actualizar? ")

        query1 = f"SELECT Nombre,ApellidoPaterno,ApellidoMaterno from {sucursal}.clientes WHERE id='{idCliente}'"
        mycursor.execute(query1)

        updateQuery = "UPDATE {}.direcciones SET".format(sucursal)
        
        print("Se va a actualizar la dirección %s de"%id_dir," ".join(mycursor.fetchall()[0]))

        values = []

        for i in range(len(campos)-1):
            decision = input(f"¿Desea actualizar el {campos[i+1]}?(Sí|No) ")
            if decision.lower()=="no":
                continue
            nuevo_valor = input(f"Inserte el nuevo valor para el {campos[i+1]}: ")
            values.append(nuevo_valor)
            updateQuery += " "+campos[i+1]+"=%s,"

        updateQuery = updateQuery[:-1]
        updateQuery += " WHERE id_cliente=%s AND id=%s"

        values.extend([idCliente, id_dir])
        values = tuple(values)

        mycursor.execute(updateQuery,values)
        mydb.commit()

        print(f"Se ha actualizado los registros del cliente {idCliente}")
        print("-"*20)


def updateClientes(mydb,sucursal,n):
    #sucursal: str, sucursal
    #n: int, cantidad de clientes a actualizar.
    
    mycursor= mydb.cursor()

    campos = ['Nombre', 'ApellidoPaterno', 'ApellidoMaterno', 'RFC']
      
    for i in range(n):
        print("-"*20)
        idCliente = input("¿Cuál es el id del cliente? ")

        query1 = f"SELECT * from {sucursal}.clientes WHERE id='{idCliente}'"
        mycursor.execute(query1)

        updateQuery = "UPDATE {}.clientes SET".format(sucursal)
        
        print("Se va a actualizar a\n"+" ".join(mycursor.fetchall()[0]))

        values = []

        for i in range(len(campos)):
            decision = input(f"¿Desea actualizar el {campos[i]}?(Sí|No) ")
            if decision.lower()=="no":
                continue
            nuevo_valor = input(f"Inserte el nuevo valor para el {campos[i]}: ")
            values.append(nuevo_valor)
            updateQuery += " "+campos[i]+"=%s,"

        updateQuery = updateQuery[:-1]
        updateQuery += " WHERE id=%s"

        values.append(idCliente)
        values = tuple(values)

        mycursor.execute(updateQuery,values)
        mydb.commit()


        print(f"Se ha actualizado los registros del cliente {idCliente}")
        print("-"*20)


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

#################

def updateRegistro(mydb,sucursal):
    #cursor: mysql.connector.connect.cursor

    #mycursor = mydb.cursor()
    tabla = input('¿Qué tabla deseas actualizar? (cliente|dirección) ')

    n = int(input('¿Cuántos registros vas a actualizar? '))

    if tabla=='cliente':
      updateClientes(mydb,sucursal,n)
    elif tabla=='dirección':
      updateDirecciones(mydb,sucursal,n)

    return ""