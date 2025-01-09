from logic.products import findAll
from tabulate import tabulate
def design():
    print("""
    Menu de productos
        1. Ver productos
        2. Ver productos por categoria
        3. Actualizar el inventario de un producto
        4. Agregar un nuevo producto al stock
        0. Salir 
    """)
    return int(input())

def tableProducts():
    data = findAll()
    dataModify = []
    for diccionario in data:
        diccionario.pop("descripcion")
        diccionario.pop("proveedor")
        diccionario.pop("precio_proveedor")
        dataModify.append(diccionario)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))

def tableProductsByCategory(Category):
    data = findAll()
    dataModify = []
    for diccionario in data:
        if(diccionario.get("categoria") == Category):
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))


