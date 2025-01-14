from logic.products import findAll as findAllProducts, saveAll as saveAllProducts
from logic.order import findAllOrders, saveAll
from tabulate import tabulate
from datetime import datetime
from formula.order import *
import random


def designClient(): #Menu de clientes
    print("""
          *********************
            Menu de clientes
        1. Realizar pedido
        2. Ver pedidos realizados
        0. Salir
          *********************
        """)
    opc = (input())
    return opc


def formularyTakeOrder(): #Formulario para realizar un pedido
    dataProducts = findAllProducts() #Busca los productos en el archivo JSON
    dataOrders = findAllOrders()  #Busca los pedidos en el archivo JSON
    print("Lista de productos en stock")
    findProductsMajor = list(filter(lambda product: product.get("cantidad_en_stock") > 0, dataProducts)) #Filtra los productos que tienen stock
    #El lambda sirve para crear una función llamada product el cual recibe un argumento y retorna si el stock es mayor a 0
    findProducts = [{key: product[key] for key in product if key not in ["descripcion", "proveedor", "precio_proveedor", "categoria"]} for product in findProductsMajor]
    #Busca todos los productos filtrados y les asigna sus llaves correspondientes
    print(tabulate(findProducts, headers="keys", tablefmt="grid", numalign="center", showindex="always"))

    now = datetime.now()
    format = now.strftime("%d/%m/%Y") #Importación de tiempo
    new_order_code = dataOrders[-1]["codigo_pedido"] + 1 if dataOrders else 1   #Genera un nuevo código de pedido automaticamente

    formulary = {
        "codigo_pedido": new_order_code,
        "codigo_cliente": input("Ingrese el código del cliente (EJ: CL-001): "),
        "fecha_pedido": format,
        "detalles_pedido": []
    }
#Diccionario para poder guardar los datos del pedido
    while True:  #Ciclo para añadir productos al pedido
        while True:
            codigo_producto = input("Ingrese el código del producto: ")
            product = next((prod for prod in dataProducts if prod["codigo_producto"] == codigo_producto), None)
            #Un iterador que busca el producto en la lista de productos
            if product: #Si encontró algún producto
                precio_unitario = product["precio_venta"] #Asigna el precio del producto mediante el json de productos con el nombre de precio_venta
                numero_linea = random.randint(1, 5) #Genera una linea aleatoria
                adjustStockAndAddToOrder(product, dataProducts, formulary, codigo_producto, precio_unitario, numero_linea)
                #Función que ajusta el stock y añade el producto al pedido
                break  
            else:
                print("Código no encontrado, vuelva a digitar.")

        otra = input("¿Desea agregar otro producto? (s/n): ") #Añadir más de un producto al pedido
        if otra.lower() != 's':
            break  


    if formulary["detalles_pedido"]: #Si los detalles en el pedido están completos
        dataOrders.append(formulary) #Añade el pedido al archivo JSON
        saveAll(dataOrders) #Los almacena 
        print("Se guardó el pedido correctamente")
    else:
        print("No se guardó el pedido porque no se añadieron productos válidos.")

def seeOrders(): #Función para ver las ordenes realizadas
    data = findAllOrders() #Data va a tomar la informacion de todos los pedidos

    for pedido in data: #Recorre todos los pedidos en la data
        print(f"--- Pedido: {pedido['codigo_pedido']} | Cliente: {pedido['codigo_cliente']} | Fecha: {pedido['fecha_pedido']}") 
        #Toma los valores de la llave en la que está posicionado actualmente para poder imprimir despues
        print(tabulate  (pedido["detalles_pedido"], headers="keys", tablefmt="grid", numalign="center"))
        print("\n" + "="*50 + "\n")
    input("Presione Enter para continuar: ")
    