from logic.products import findAll, saveAll
from tabulate import tabulate

def obtener_opcion():
    while True:
        try:
            print("""
        *****************************************************
            Menu de productos
                1. Ver productos
                2. Ver productos por categoria
                3. Ver producto por código
                4. Ver producto por nombre
                5. Actualizar el inventario de un producto
                6. Agregar un nuevo producto al stock
                0. Salir
        *****************************************************           
            """)
            opcion = int(input("--> "))
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
    input("--> Presione enter para continuar")
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
    input("--> Presione enter para continuar")

def tableProductsByCode(Code):
    data = findAll()
    dataModify = []
    for diccionario in data:
        if(diccionario.get("codigo_producto") == Code):
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")  

def tableProductsByName(Name):
    data = findAll()
    dataModify = []
    for diccionario in data:
        if(diccionario.get("nombre") == Name):
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")        
def newProduct():
    data = findAll()
    codigo_producto = input("Ingrese el código del producto: ")
    findProducts = list(filter(lambda product: product.get("codigo_producto") == codigo_producto, data))
    if(not len(findProducts)):
        newProduct = {
            "codigo_producto": codigo_producto,
            "nombre": input("Ingrese el nombre del producto: "),
            "categoria": input("Ingrese la categoria del producto ('panes', 'pastel', 'postre'): ").lower(),
            "descripcion": input("Ingrese la descripción del producto: "),
            "proveedor": input("Ingrese el proveedor de dicho producto: "),
            "cantidad_en_stock": int(input("Ingrese la cantidad en stock del producto: ")),
            "precio_venta": float(input("Ingrese el precio de venta del producto: ")),
            "precio_proveedor": float(input("Ingrese el precio del proveedor: "))
     }
        data.append(newProduct)
        saveAll(data)
        return "Producto agregado exitosamente"
        
    else:
        print("""
        *********************
            ERROR-ERROR 
        El producto ya existe
        *********************""")
