#!/usr/bin/python3

import getpass
import mysql.connector

from select_ import *

def insertDirecciones(mydb, sucursal, n):
    mycursor = mydb.cursor()

    suc = "D" + sucursal.upper()[:3]
    mycursor.execute("SET @suc=%s",(suc,))
    #id_dir = 1

    #Lista de direcciones
    Dirs = []
    sucursales = getSucursales(mydb)
    for s in sucursales:
            mycursor.execute(f"SELECT id_cliente, Calle, Numero, Colonia, Estado, CP FROM {s}.direcciones")
            Dirs.extend(mycursor.fetchall())

    direcciones = ""

    for i in range(n):
        omitir = False
        print("-"*20)
        id_cliente = input("id del cliente: ")
        calle = input("Calle: ")
        
        numero = input("No.: ")
        #Nos aseguramos que dé un número
        while numero.isdigit() == False:
            print("Inserte correctamente el número.")
            numero = input("No.: ")
        numero = int(numero)

        Colonia = input("Colonia: ")
        Estado = input("Estado: ")

        CP = input("CP: ")
        #Nos aseguramos que dé un CP válido
        while CP.isdigit() == False or len(CP)!=5:
            print("Inserte un CP válido.")
            CP = input("CP.: ")

        #Revisar que el cliente sí pertenezca a la sucursal
        if id_cliente[:3]!=suc[1:]:
            print(f"El cliente {id_cliente} no pertenece a la sucursal {sucursal}.")
            continue

        #Revisar que el cliente exista
        mycursor.execute(f"SELECT id FROM {sucursal}.clientes WHERE id='{id_cliente}'")
        existe = len(mycursor.fetchall())

        while existe==0:
            print(f"El cliente {id_cliente} no está registrado.\nLas opciones disponibles son:")
            print("1. Omitir el registro.")
            print("2. Corregir el id.")
            op = int(input("¿Qué operación va a realizar? "))
            if op==1:
                omitir = True
                break
            else:
                id_cliente = input("id del cliente: ")
                mycursor.execute(f"SELECT id FROM {sucursal}.clientes WHERE id='{id_cliente}'")
                existe = len(mycursor.fetchall())


        #Verificar que sea una dirección sea única.
        nueva_dir = tuple([id_cliente,calle,numero, Colonia, Estado, CP])
        while nueva_dir in Dirs:
            print("Dirección registrada en la base de datos.\nLas opciones disponibles son:")
            print("1. Omitir registro.")
            print("2. Cambiar valores de inserción.")
            dec = int(input("¿Qué desea hacer? "))
            if dec==1:
                omitir = True
                break
            else:
                id_cliente = input("id del cliente: ")
                calle = input("Calle: ")
                numero = int(input("No.: "))
                Colonia = input("Colonia: ")
                Estado = input("Estado: ")
                CP = input("CP: ")


        if omitir:
            continue


        #mycursor.execute("EXECUTE dirIdUp USING @suc")
        direcciones += f"('{id_cliente}', '{calle}', {numero}, '{Colonia}', '{Estado}', '{CP}'),\n"  

    if direcciones=="":
        return 

    direcciones=direcciones[:-2] #Quitar coma del final
    insertQuery = f"INSERT INTO {sucursal}.direcciones (id_cliente,calle,numero,Colonia,Estado,CP) VALUES {direcciones}"
    #print(insertQuery)
    mycursor.execute(insertQuery)
    mydb.commit()

    print("Se han insertado las direcciones: \n", direcciones)
    print("En la sucursal",sucursal)
    print("-"*20)

def insertClientes(mydb, sucursal, n):

    mycursor = mydb.cursor()

    #Lista de RFCs
    RFCs = []
    sucursales = getSucursales(mydb)
    for s in sucursales:
            mycursor.execute(f"SELECT RFC FROM {s}.clientes")
            RFCs.extend(mycursor.fetchall())
    
    RFCs = set([t[0] for t in RFCs])

    suc = sucursal.upper()[:3]
    mycursor.execute("SET @suc=%s",(suc,))

    clientes = ""

    for i in range(n):
        omitir = False
        print("-"*20)
        Nombre = input("Nombre: ")
        ApellidoPaterno = input("Apellido Paterno: ")
        ApellidoMaterno = input("Apellido Materno: ")
        rfc = input("RFC: ")

        #Revisamos que el RFC sea válido.
        while len(rfc)!=13:
            print("El RFC insertado no es válido.\nLas opciones disponibles son:")
            print("1. Omitir registro.")
            print("2. Cambiar valores de inserción.")
            dec = int(input("¿Qué desea hacer? "))
            if dec==1:
                omitir=True
                break
            else:
                rfc = input("RFC: ")

        #Si el RFC ya está registrado
        while rfc in RFCs:
            print("RFC registrado en la base de datos.\nLas opciones disponibles son:")
            print("1. Omitir registro.")
            print("2. Cambiar valores de inserción.")
            dec = int(input("¿Qué desea hacer? "))
            if dec==1:
                omitir=True
                break
            else:
                Nombre = input("Nombre: ")
                ApellidoPaterno = input("Apellido Paterno: ")
                ApellidoMaterno = input("Apellido Materno: ")
                rfc = input("RFC: ")

        if omitir:
            continue
        
        #Crear id
        mycursor.execute("EXECUTE idGen USING @suc")
        mycursor.execute("SELECT @lastid")
        idCliente = mycursor.fetchall()[0][0]

        mycursor.execute("EXECUTE idUp USING @suc")

        clientes += f"('{idCliente}','{Nombre}','{ApellidoPaterno}','{ApellidoMaterno}','{rfc}'),\n"

    #Si al final no se insertó nada, regresar.
    if clientes=="":
        return

    clientes = clientes[:-2]
    #print(clientes)
    mycursor.execute(f"INSERT INTO {sucursal}.clientes (id,nombre,apellidoPaterno,apellidoMaterno,RFC) VALUES {clientes}")
    mydb.commit()
    print(f"Se han insertado los clientes:\n{clientes}")
    print("En la sucursal",sucursal)
    print("-"*20)

def insertRegistro(mydb,sucursal):
    #mydb: mysql.connector.connect
    #sucursal: str, sucursal desde la que se trabaja.

    mycursor= mydb.cursor()

    #Prepare Staments auxiliares
    mycursor.execute("PREPARE idGen FROM 'SET @lastid = (SELECT CONCAT(base,number) FROM adminSucursales.idConstructor WHERE base=?)'")
    mycursor.execute("PREPARE idUp FROM 'UPDATE adminSucursales.idConstructor SET number= number+1 WHERE base=?';")

    tabla = input('¿Qué desea agregar? (cliente|dirección) ')

    n = int(input('¿Cuántos registros va a añadir? '))

    if tabla.lower() == 'cliente':
      insertClientes(mydb,sucursal,n)
    elif tabla.lower() == 'dirección':
      insertDirecciones(mydb,sucursal,n)