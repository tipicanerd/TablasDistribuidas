#!/usr/bin/python3
import mysql.connector
from sucursalesGen import getSucursales

cliColumns = ["id","nombre","apellidoPaterno","apellidoMaterno","RFC"]
dirColumns = ["id_cliente","dir_id","calle","numero","Colonia","Estado","CP"]
params = ["nombre","apellidoPaterno","apellidoMaterno","RFC","id","calle","numero","Colonia","Estado","CP","dir_id"]
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
    print("11. ID")


#Menu de parametros
def paramMenu():
    print("-"*20)
    print("SELECCIONE LOS PARÁMETROS QUE DESEA UTILIZAR PARA FILTRAR")
    printColValues()
    print("\nFUNCIONES GENERALES:")
    print("12. Quitar parámetro/columna")
    print("13. Cancelar Proceso")
    print("14. Terminado")
    print("15. Imprimir condiciones/columnas actuales")


#Escoger columnas para un SELECT columnas FROM 
def chooseColumns():
    print("-"*20)
    print("ESCOJA LAS COLUMNAS QUE QUIERE VER")
    printColValues()
    print("\nBÚSQUEDAS GENERALES")
    print("12. Todas las de clientes")
    print("13. Todas las de direcciones")
    print("14. Todas las de clientes y direcciones")
    print("\nFUNCIONES GENERALES")
    print("15. Quitar columna")
    print("16. Terminado")
    print("17. Imprimir columnas actuales\n")

    options = {}
    for i in range(len(params)):
        options[str(i+1)] = params[i]
    
    columns = []

    while(True):
        op = input("Opción: ")
        if(op == "12"):
            return cliColumns
        elif(op == "13"):
            return dirColumns
        elif(op == "14"):
            return cliColumns + dirColumns

        elif(op == "15"):
            op2 = input("Columna a remover: ")
            if(options[op2] in columns):
                print(f"Quitando {options[op2]}")
                columns.remove(options[op2])
            else:
                print("Opción inválida o no está dentro de las columnas elegidas")
        
        elif(op == "16"):

            return columns

        elif(op == "17"):
            print("Columnas actuales: ")
            for col in columns:
                print(col)
            print("")

        elif(op in [str(i) for i in range(1,12)]):
            if(options[op] not in columns):
                columns.append(options[op])
                print(f"Se añadió la columna {options[op]}")
        

def printConditions(conditions):
    print("\nCondiciones actuales:")
    for c in conditions:
        print(c,"=",conditions[c])
    print("")


def removeCondition(conditions, options):
    op2 = input("Escoja el parámetro que quiere remover: ")
    if(options[op2] in conditions):
        print(f"Quitando {options[op2]} de las condiciones")
        del conditions[options[op2]]
    else:
        print("Esto no es una opción valida o no está incluida en las condiciones establecidas")

    return conditions


def createCondString(conditions):
    condString = ""

    for c in conditions:
        if(c == "numero"): #Valor int si es el número de la dirección (sin comillas)
            condString += f"{c} = {conditions[c]} AND "
        elif(c == "dir_id"):
            condString += f"direcciones.id = {conditions[c]} AND " #Especificar la id de direcciones
        else:
            condString += f"{c} = '{conditions[c]}' AND "
    condString = condString[:-4] #Quitar AND del final

    return condString

def createColString(columns):
    colString = ""
    aux = ""
    for col in columns:
        if(col in cliColumns):
            aux = "clientes"
        else:
            aux = "direcciones"        
        if(col == "dir_id"):
            aux = "direcciones"
            col = "id"
        
        colString += f"{aux}.{col}, "

    colString = colString[:-2]
    return colString

#FUNCIÓN DE SELECT
def select(mydb,sucursales,columns,conditions = None):
    mycursor = mydb.cursor()
    clientes = []
    colString = createColString(columns)
    query = ""
    tieneDirecciones = False
    for col in columns:
        if(col in dirColumns):
            tieneDirecciones = True
            break


    if(conditions in [None, {}]):
        if(tieneDirecciones):
            for s in sucursales:
                query = f"SELECT {colString} FROM {s}.clientes INNER JOIN {s}.direcciones ON {s}.clientes.id = {s}.direcciones.id_cliente"
                #print(query)
                mycursor.execute(query)
                clientes += mycursor.fetchall()
        else:
            for s in sucursales:
                query = f"SELECT {colString} FROM {s}.clientes"
                #print(query)
                mycursor.execute(query)
                clientes += mycursor.fetchall()
        return clientes
            

    condString = createCondString(conditions)

    for cond in conditions:
        if(cond in dirColumns):
            tieneDirecciones = True
            break

    if(tieneDirecciones):
        for s in sucursales:
            query = f"SELECT {colString} FROM {s}.clientes INNER JOIN {s}.direcciones ON {s}.clientes.id = {s}.direcciones.id_cliente WHERE {condString}"
            print(query)
            mycursor.execute(f"SELECT {colString} FROM {s}.clientes INNER JOIN {s}.direcciones ON {s}.clientes.id = {s}.direcciones.id_cliente WHERE {condString}")
            clientes += mycursor.fetchall()

    else:
        for s in sucursales:
            query = f"SELECT {colString} FROM {s}.clientes  WHERE {condString}"
            print(query)
            mycursor.execute(query)
            clientes += mycursor.fetchall()
    return clientes


#SELECT * FROM {} WHERE (condiciones) para todas las sucursales
def selectByParam(sucursales,mydb):
    paramMenu()
    op = 0
    
    options = {}
    
    counter = 1
    for i in range(len(params)):
        options[str(i+1)] = params[i]

    conditions = {}

    #Obtener condiciones de columna = valor
    while(True):
        op = input("Opción: ")
        if(op == "12"):
            conditions = removeCondition(conditions,options)

        if(op == "13"):
            return [],[]

        if(op == "14"):
            break
    
        if(op == "15"):
            printConditions(conditions)

        if(op in [str(i) for i in range(1,12)]):
            val = input(f"Valor ({options[op]}): ")
            conditions[options[op]] = val
        
    print("Condiciones finales:",conditions)
    op = 0

    mycursor = mydb.cursor()
    clientes = []
    columns = []

    print("-"*20)
    print("Escoja los datos del cliente quiere observar:")
    print("Para elegir columnas específicas escoja con base en los valores previos de cada dato")
    print("También se pueden usar las mismas funciones generales del paso anterior")
    print("16. Toda la tabla de clientes")
    print("17. Toda la tabla de direcciones")
    print("18. Tabla de clientes y direcciones")


    while(True):
        op = input("Opción: ")
        if(op == "13"): #Cancelar select
            return [],[]
        elif(op == "14"): #Pasar a hacer select por columnas
            break
        elif(op == "15"):
            print("\nDatos actuales:")
            print(columns)
            print("")
            
        elif(op == "16"): #SELECT * FROM clientes WHERE (condiciones)
            clientes = select(mydb,sucursales,cliColumns,conditions)
            return clientes, cliColumns

        elif(op == "17"): #SELECT * FROM direcciones WHERE (condiciones)
            clientes = select(mydb,sucursales,dirColumns,conditions)
            return clientes, dirColumns
        
        elif(op == "18"): #SELECT * FROM clientes y direcciones WHERE (condiciones)
            columns = cliColumns + dirColumns
            clientes = select(mydb,sucursales, columns, conditions)
            return clientes, columns

        elif(op in ([str(i) for i in range(1,12)])): #Añadir columnas a mostrar
            if(options[op] not in columns):
                columns.append(options[op])
                print(f"Se añadió {options[op]}")

        elif(op == "12"): #Quitar columnas a mostrar
            op2 = input("Escoja la columna que quiere remover: ")
            if(options[op2] in columns):
                print(f"Quitando {options[op2]} de los datos")
                columns.remove(options[op2])
            else:
                print("Esto no es una opción valida o no está incluida en las condiciones establecidas")

    #Seleccionar con base en columnas seleccionadas y filtros    
    clientes = select(mydb,sucursales,columns,conditions)

    return clientes, columns


#SELECT columns FROM {tabla} para todas las sucursales
def selectAll(mydb, sucursales):
    columns = chooseColumns()
    if(columns == []):
        return [],[]
    datos = select(mydb,sucursales,columns)

    return datos, columns


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
            clientes, columns  = selectAll(mydb,sucursales)
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
