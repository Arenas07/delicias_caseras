from logic.products import findAll as findAllProducts, saveAll as saveAllProducts
from logic.order import findAllOrders, saveAll
from tabulate import tabulate
from datetime import datetime
from formula.order import *
import random


def designClient():
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


def formularyTakeOrder():
    dataProducts = findAllProducts()  # Obtener todos los productos
    dataOrders = findAllOrders()  # Obtener los pedidos actuales

    # Mostrar productos disponibles
    print("Lista de productos en stock")
    findProductsMajor = list(filter(lambda product: product.get("cantidad_en_stock") > 0, dataProducts))
    findProducts = [{key: product[key] for key in product if key not in ["descripcion", "proveedor", "precio_proveedor", "categoria"]} for product in findProductsMajor]
    print(tabulate(findProducts, headers="keys", tablefmt="grid", numalign="center", showindex="always"))

    # Obtener la fecha actual
    now = datetime.now()
    format = now.strftime("%d/%m/%Y")

    # Generar el código del nuevo pedido
    new_order_code = dataOrders[-1]["codigo_pedido"] + 1 if dataOrders else 1  # Si no hay pedidos, empezar desde 1

    # Crear un formulario para el nuevo pedido
    formulary = {
        "codigo_pedido": new_order_code,
        "codigo_cliente": input("Ingrese el código del cliente (EJ: CL-001): "),
        "fecha_pedido": format,
        "detalles_pedido": []
    }

    while True:  # Añadir productos al pedido
        while True:
            codigo_producto = input("Ingrese el código del producto: ")

            # Buscar el producto en la base de datos para obtener el precio de venta
            product = next((prod for prod in dataProducts if prod["codigo_producto"] == codigo_producto), None)

            if product:
                precio_unitario = product["precio_venta"]
                numero_linea = random.randint(1, 5)

                # Llamar a la función para ajustar el stock y añadir el producto al pedido
                adjustStockAndAddToOrder(product, dataProducts, formulary, codigo_producto, precio_unitario, numero_linea)
                break  # Salir del bucle una vez que el producto se ha agregado correctamente
            else:
                print("Código no encontrado, vuelva a digitar.")

        # Preguntar si desea agregar otro producto
        otra = input("¿Desea agregar otro producto? (s/n): ")
        if otra.lower() != 's':
            break  # Salir del ciclo si no se desea agregar más productos

    # Si el pedido tiene productos, lo guardamos
    if formulary["detalles_pedido"]:
        # Añadir el nuevo pedido a la lista de pedidos
        dataOrders.append(formulary)

        # Guardar los pedidos actualizados en el archivo JSON
        saveAll(dataOrders)
        print("Se guardó el pedido correctamente")
    else:
        print("No se guardó el pedido porque no se añadieron productos válidos.")

def seeOrders():
    data = findAllOrders()

    for pedido in data:
        print(f"--- Pedido: {pedido['codigo_pedido']} | Cliente: {pedido['codigo_cliente']} | Fecha: {pedido['fecha_pedido']}")
        print(tabulate  (pedido["detalles_pedido"], headers="keys", tablefmt="grid", numalign="center"))
        print("\n" + "="*50 + "\n")
    input("Presione Enter para continuar: ")
    