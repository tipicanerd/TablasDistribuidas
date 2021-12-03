#!/usr/bin/python3

import getpass
import mysql.connector
from insert import *


def updateDirecciones(mydb,sucursal,n):
    #mydb: mysql.connector.connect, 
    #sucursal: str, sucursal
    #n: int, cantidad de direcciones a actualizar.

    mycursor= mydb.cursor()

    campos = ['id','calle', 'numero', 'Colonia', 'Estado', 'CP']

    for i in range(n):
        omitir = False
        print("-"*20)
        idCliente = input("¿Cuál es el id del cliente? ")

        query1 = "SELECT * FROM {}.direcciones WHERE id_cliente=%s".format(sucursal)
        mycursor.execute(query1,(idCliente,))

        clienteDirs = mycursor.fetchall()

        while len(clienteDirs)==0:
            print(f"El cliente {idCliente} no tiene direcciones registradas.\nLas opciones disponibles son:")
            print("1. Omitir la actualización.")
            print("2. Corregir el id.")
            print("3. Insertar direccion.")
            op = int(input("¿Qué operación va a realizar? "))
            if op==1:
                omitir = True
                break
            elif op==2:
                id_cliente = input("id del cliente: ")
                mycursor.execute(query1,(id_cliente,))
                clienteDirs = mycursor.fetchall()
            else:
                insertDirecciones(mydb, sucursal, 1)
                omitir = True
                break

        if omitir:
            continue

        print(f"El cliente {idCliente} tiene las direcciones")

        
        for direccion in clienteDirs:
            print("-"*20)
            for i in range(len(campos)):
                print(campos[i],":",direccion[i+1])
        print("-"*20)

        id_dir = input("¿Cuál es el id de la dirección del cliente que desea actualizar? ")

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
    #mydb: mysql.connector.connect, 
    #sucursal: str, sucursal
    #n: int, cantidad de clientes a actualizar.
    
    mycursor= mydb.cursor()

    campos = ['Nombre', 'ApellidoPaterno', 'ApellidoMaterno', 'RFC']
      
    for i in range(n):
        omitir = False
        print("-"*20)
        idCliente = input("¿Cuál es el id del cliente? ")

        query1 = f"SELECT * from {sucursal}.clientes WHERE id='{idCliente}'"
        mycursor.execute(query1)
        clienteDatos = mycursor.fetchall()

        updateQuery = "UPDATE {}.clientes SET".format(sucursal)
        
        while len(clienteDatos)==0:
            print(f"El cliente {idCliente} no está registrado.\nLas opciones disponibles son:")
            print("1. Omitir la actualización.")
            print("2. Corregir el id.")
            print("3. Insertar nuevo cliente.")
            op = int(input("¿Qué operación va a realizar? "))
            if op==1:
                omitir = True
                break
            elif op==2:
                idCliente = input("id del cliente: ")
                query1 = f"SELECT * from {sucursal}.clientes WHERE id='{idCliente}'"
                mycursor.execute(query1)
                clienteDatos = mycursor.fetchall()
            else:
                insertClientes(mydb, sucursal, n)
                omitir=True
                break

        if omitir:
            continue

        print("Se va a actualizar a\n"+" ".join(clienteDatos[0]))
        values = []
        rfc = ""
        hasRfc = False

        for campo in campos:
            decision = input(f"¿Desea actualizar el {campo}?(Sí|No) ")
            if decision.lower()=="no":
                continue

            nuevo_valor = input(f"Inserte el nuevo valor para el {campo}: ")

            if(campo == 'RFC'):
                rfc = nuevo_valor
                hasRfc = True

            values.append(nuevo_valor)
            updateQuery += " "+campo+"=%s,"

        updateQuery = updateQuery[:-1]
        updateQuery += " WHERE id=%s"

        if(values == []):
            continue
        
        if(hasRfc):
            while len(rfc)!=13:
                print("El RFC actualizado no es válido.\nLas opciones disponibles son:")
                print("1. Omitir actualización.")
                print("2. Cambiar valor de actualización.")
                dec = int(input("¿Qué desea hacer? "))
                if dec==1:
                    omitir=True
                    break
                else:
                    rfc = input("RFC: ")
        if omitir:
            continue

        #values[-1] = rfc

        values.append(idCliente)
        #print(values)
        values = tuple(values)
        #print(updateQuery,values)

        mycursor.execute(updateQuery,values)
        mydb.commit()


        print(f"Se ha actualizado los registros del cliente {idCliente}")
        print("-"*20)


#################

def updateRegistro(mydb,sucursal):
    #cursor: mysql.connector.connect.cursor

    #mycursor = mydb.cursor()
    tabla = input('¿Qué tabla desea actualizar? (cliente|dirección) ')

    n = int(input('¿Cuántos registros va a actualizar? '))

    if tabla.lower() == 'cliente':
      updateClientes(mydb,sucursal,n)
    elif tabla.lower() =='dirección':
      updateDirecciones(mydb,sucursal,n)
