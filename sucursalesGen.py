from newOffice import createTables

def initSucursal(mydb, sucursales):
    if(sucursales == []):
        print("No hay ninguna sucursal disponible, para comenzar crea una nueva.")
        createTables(mydb)
        sucs = getSucursales(mydb)
        print(f"Estás en la sucursal {sucs[0]}")
        return  sucs[0]
    else:
        sucursal = sucursales[0]
        print(f"Estás en la sucursal {sucursal}, para cambiar puedes usar la opción 5")
        return sucursal

def changeSucursal(mydb,sucursal,sucursales):
    print(f"Escoge una de las sucursales disponibles ")
    printSucursales(mydb,sucursales,sucursal)

    suc = input("Nombre de la sucursal: ")
    if(suc in sucursales):
        print(f"Cambiando a sucursal {suc}")
        return suc
    else:
        print("Sucursal inexistente, use el nombre de alguna de las disponibles")
        return sucursal

def printSucursales(mydb,sucursales, sucursal):
    print("\nSucursales:",end="")
    for s in sucursales:
        print(f"\n- {s}",end="")
        if s == sucursal:
            print("(*)",end="")
    print("\n")

#Obtener lista de todas las sucursales que hay
def getSucursales(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nombre FROM adminSucursales.sucursales")
    sucursales = mycursor.fetchall()
    sucursales = [sucursal[0] for sucursal in sucursales]
    return sucursales