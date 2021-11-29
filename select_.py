#!/usr/bin/python3
import mysql.connector

cliColumns = ["id","nombre","apellidoPaterno","apellidoMaterno","RFC"]
dirColumns = ["id_cliente","id","calle","numero","Colonia","Estado","CP"]


def selectMenu():
    print("-"*20)
    print("SELECCIONAR CLIENTE Y/O DIRECCIÓN\n")
    print("1. Seleccionar todos los clientes y/o direcciones")
    print("2. Seleccionar por valores de columnas")
    print("3. Cancelar")


def printColValues():
    print("DATOS DE CLIENTE:")
    print("1. Nombre")
    print("2. Apellido Paterno")
    print("3. Apellido Materno")
    print("4. RFC")
    print("5. ID")
    print("\nDATOS DE DOMICILIO:")
    print("6. Calle")
    print("7. Número")
    print("8. Colonia")
    print("9. Estado")
    print("10. Código Postal")


#Menu de parametros
def paramMenu():
    print("-"*20)
    print("SELECCIONE LOS PARÁMETROS QUE DESEA UTILIZAR PARA FILTRAR")
    printColValues()
    print("\nFUNCIONES GENERALES:")
    print("11. Quitar parámetro/columna")
    print("12. Cancelar Proceso")
    print("13. Terminado")
    print("14. Imprimir condiciones/columnas actuales")


#Escoger columnas para un SELECT columnas FROM 
def chooseColumns():
    print("ESCOJA LAS COLUMNAS QUE QUIERE VER")
    printColValues()
    print("\nBÚSQUEDAS GENERALES")
    print("11. Todas las de clientes")
    print("12. Todas las de direcciones")
    print("13. Todas las de clientes y direcciones")
    print("\nFUNCIONES GENERALES")
    print("14. Quitar columna")
    print("15. Terminado")
    print("16. Imprimir columnas actuales")
    options = {}
    params = ["nombre","apellidoPaterno","apellidoMaterno","RFC","id","calle","numero","Colonia","Estado","CP"]
    for i in range(len(params)):
        options[str(i+1)] = params[i]
    
    columns = []

    while(True):
        op = input("Opción: ")
        if(op == "11"):
            return cliColumns
        elif(op == "12"):
            return dirColumns
        elif(op == "13"):
            return cliColumns + dirColumns

        elif(op == "14"):
            if(options[op] in columns):
                print(f"Quitando {options[op]}")
                columns.remove(options[op])
        
        elif(op == "15"):
            return columns

        elif(op == "16"):
            print("Columnas actuales: ")
            for col in columns:
                print(col)
            print("")

        elif(op in [str(i) for i in range(1,11)]):
            if(options[op] not in columns):
                columns.append(options[op])
                print(f"Se añadió la columna {options[op]}")
        

#SELECT * FROM {} WHERE (condiciones) para todas las sucursales
def selectByParam(sucursales,mydb):
    paramMenu()
    op = 0
    params = ["nombre","apellidoPaterno","apellidoMaterno","RFC","id","calle","numero","Colonia","Estado","CP"]
    options = {}
    
    counter = 1
    for i in range(len(params)):
        options[str(i+1)] = params[i]

    conditions = {}

    #Obtener condiciones de columna = valor
    while(True):
        op = input("Opción: ")
        if(op == "11"):
            op2 = input("Escoja el parámetro que quiere remover: ")
            if(options[op2] in conditions):
                print(f"Quitando {options[op2]} de las condiciones")
                del conditions[options[op2]]
            else:
                print("Esto no es una opción valida o no está incluida en las condiciones establecidas")

        if(op == "12"):
            return 

        if(op == "13"):
            break
    
        if(op == "14"):
            print("\nCondiciones actuales:")
            for c in conditions:
                print(c,"=",conditions[c])
            print("")

        if(op in [str(i) for i in range(1,11)]):
            val = input(f"Valor ({options[op]}): ")
            conditions[options[op]] = val
        
    print("Condiciones finales:",conditions)
    condString = ""
    for c in conditions:
        if(c == "numero"): #Valor int si es el número de la dirección (sin comillas)
            condString += f"{c} = {conditions[c]} AND "
        else:
            condString += f"{c} = '{conditions[c]}' AND "
    condString = condString[:-4] #Quitar AND del final

    op = 0

    mycursor = mydb.cursor()
    clientes = []
    columns = []

    print("-"*20)
    print("Escoja los datos del cliente quiere observar:")
    print("Para elegir columnas específicas escoja con base en los valores previos de cada dato")
    print("También se pueden usar las mismas funciones generales del paso anterior")
    print("15. Toda la tabla de clientes")
    print("16. Toda la tabla de direcciones")
    print("17. Tabla de clientes y direcciones")

    while(True):
        op = input("Opción: ")
        if(op == "12"): #Cancelar select
            return
        elif(op == "13"): #Pasar a hacer select por columnas
            break
        elif(op == "14"):
            print("\nDatos actuales:")
            print(columns)
            print("")
            
        elif(op == "15"): #SELECT * FROM clientes WHERE (condiciones)
            clientes = []
            columns = cliColumns
            for s in sucursales:
                mycursor.execute(f"SELECT * FROM {s}.clientes WHERE {condString}")
                clientes += mycursor.fetchall()
            return clientes, columns

        elif(op == "16"): #SELECT * FROM direcciones WHERE (condiciones)
            clientes = []
            columns = dirColumns
            for s in sucursales:
                mycursor.execute(f"SELECT * FROM {s}.direcciones WHERE id_cliente IN (SELECT id FROM {s}.clientes WHERE {condString})")
                clientes += mycursor.fetchall()
            return clientes, columns
        
        elif(op == "17"): #SELECT * FROM clientes y direcciones WHERE (condiciones)
            clientes = []
            columns = cliColumns + dirColumns
            for s in sucursales:
                mycursor.execute(f"SELECT * FROM {s}.clientes INNER JOIN {s}.direcciones ON {s}.clientes.id = {s}.direcciones.id_cliente WHERE {condString}")
                clientes += mycursor.fetchall()
            return clientes, columns

        elif(op in ([str(i) for i in range(1,11)])): #Añadir columnas a mostrar
            if(options[op] not in columns):
                columns.append(options[op])
                print(f"Se añadió {options[op]}")

        elif(op == "11"): #Quitar columnas a mostrar
            op2 = input("Escoja la columna que quiere remover: ")
            if(options[op2] in columns):
                print(f"Quitando {options[op2]} de los datos")
                columns.remove(options[op2])
            else:
                print("Esto no es una opción valida o no está incluida en las condiciones establecidas")

    #Seleccionar con base en columnas seleccionadas y filtros
    colString = ""
    aux = ""
    tieneDirecciones = False
    for col in columns:
        if(col in cliColumns):
            aux = "clientes"
        else:
            aux = "direcciones"
            tieneDirecciones = True
        colString += f"{aux}.{col}, "

    colString = colString[:-2]
    for s in sucursales:
        if(tieneDirecciones):
            mycursor.execute(f"SELECT {colString} FROM {s}.clientes INNER JOIN {s}.direcciones ON {s}.clientes.id = {s}.direcciones.id_cliente WHERE {condString}")
            clientes += mycursor.fetchall()

        else:
            mycursor.execute(f"SELECT {colString} FROM {s}.clientes WHERE {condString}")
            clientes += mycursor.fetchall()

    return clientes, columns


#SELECT columns FROM {tabla} para todas las sucursales
def selectAll(mydb, sucursales):
    mycursor = mydb.cursor()
    datos = []
    colString = ""
    columns = chooseColumns()
    tieneDirecciones = False

    for col in columns:
        if(col in cliColumns):
            aux = "clientes"
        else:
            aux = "direcciones"
            tieneDirecciones = True
        colString += f"{aux}.{col},"

    colString = colString[:-1]
    for s in sucursales:
        if(tieneDirecciones):
            mycursor.execute(f"SELECT {colString} FROM {s}.clientes INNER JOIN {s}.direcciones ON {s}.clientes.id = {s}.direcciones.id_cliente")
            datos += mycursor.fetchall()
        else:
            mycursor.execute(f"SELECT {colString} FROM {s}.clientes")
            datos += mycursor.fetchall()

    return datos, columns


#Obtener lista de todas las sucursales que hay
def getSucursales(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nombre FROM adminSucursales.sucursales")
    sucursales = mycursor.fetchall()
    sucursales = [sucursal[0] for sucursal in sucursales]
    return sucursales


#Imprimir por columnas la búsqueda
def printColumns(clientes):
    col_width = max(len(str(word)) for row in clientes for word in row) + 2  # padding
    for row in clientes:
        print("".join(str(word).ljust(col_width) for word in row))

#Validar la búsqueda y llamar a imprimir
def printSearch(datos,columns):
    if(datos == []):
        print("No hay coincidencias")
    else:
        printColumns([columns]+datos)

#Función principal para seleccionar
def selectDatos(mydb):
    op = 0
    selectMenu()

    while(op not in ["1","2","3"]):
        op = input("Opción: ")
    
        sucursales = getSucursales(mydb)
        if(op == "1"):
            clientes, columns = selectAll(mydb, sucursales)
            print("")
            printSearch(clientes,columns)
            print("")

        elif(op == "2"):
            clientes,columns = selectByParam(sucursales,mydb)
            print("")
            printSearch(clientes,columns)
            print("")
        
        elif(op == "3"):
            return 