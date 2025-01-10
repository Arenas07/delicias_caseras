from logic.products import findAll
from tabulate import tabulate

def obtener_opcion():
    while True:
        try:
            print("""
            Menu de productos
                1. Ver productos
                2. Ver productos por categoria
                3. Buscar producto por código
                4. Buscar producto por nombre
                5. Actualizar el inventario de un producto
                6. Agregar un nuevo producto al stock
                0. Salir 
            """)
            opcion = int(input())
            if 0 <= opcion <= 6:  # Asegura que la opción esté dentro de un rango válido
                return opcion
            else:
                print("Por favor, ingrese un número entre 1 y 4.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

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

