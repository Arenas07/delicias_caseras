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
                print("Por favor, ingrese un número entre 0 y 6.")
                input("Presione enter para continuar: ")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def tableProducts(): #Muestra todos los productos dispnibles
    data = findAll() #Toma la información de los productos
    dataModify = []
    for diccionario in data: #Ciclo para modificar la longitud de la tabla a mostrar
        diccionario.pop("descripcion")
        diccionario.pop("proveedor")
        diccionario.pop("precio_proveedor")
        dataModify.append(diccionario) #Almacena los cambios realizados
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")
def tableProductsByCategory(Category): #Busca los productos por categoría
    data = findAll() #Toma la información de los productos
    dataModify = []
    for diccionario in data: #Ciclo para ir pasando por cada uno de los productos
        if(diccionario.get("categoria") == Category): #Si la categoría del producto es igual a la categoría ingresada
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario) #Almacena los cambios realizados
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")

def tableProductsByCode(Code): #Muestra los productos por código
    data = findAll()#Toma la información de los productos
    dataModify = []
    for diccionario in data: #Ciclo para ir pasando por cada uno de los productos
        if(diccionario.get("codigo_producto") == Code): #Si el codigo del producto es igual al codigo ingresada
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario) #Almacena los cambios realizados
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")  

def tableProductsByName(Name): #Muestra los productos por nombre
    data = findAll()#Toma la información de los productos
    dataModify = []
    for diccionario in data: #Ciclo para ir pasando por cada uno de los productos
        if(diccionario.get("nombre") == Name): #Si la categoría del producto es igual a la categoría ingresada
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            dataModify.append(diccionario) #Almacena los cambios realizados
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")        
def newProduct(): #Agregar un nuevo producto
    data = findAll() #Toma la información de los productos
    codigo_producto = input("Ingrese el código del producto: ")
    findProducts = list(filter(lambda product: product.get("codigo_producto") == codigo_producto, data)) #Filtro para comparar si el dato ingresado existe
    if(not len(findProducts)): #Si no existe registra los datos
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
        data.append(newProduct) #Une los datos a la variable y la guarda
        saveAll(data)
        return "Producto agregado exitosamente"
        
    else:
        print("""
        *********************
            ERROR-ERROR 
        El producto ya existe
        *********************""")
