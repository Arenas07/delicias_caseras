from logic.products import findAll as findAllProducts
from logic.order import findAllOrders, saveAll, findAllProducts as findAllProducts1
from tabulate import tabulate
from datetime import datetime
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
    findProducts = list(filter(lambda product: (product.pop("descripcion"), (product.pop("proveedor"), (product.pop("precio_proveedor"), (product.pop("categoria"))))), findProductsMajor))
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

    # Añadir productos al pedido
    while True:
        # Pedir los datos de un producto
        while True:
            codigo_producto = input("Ingrese el código del producto: ")

            # Buscar el producto en la base de datos para obtener el precio de venta
            product = next((prod for prod in dataProducts if prod["codigo_producto"] == codigo_producto), None)

            if product:
                # Obtener el precio de venta y generar el número de línea aleatorio
                precio_unitario = product["precio_venta"]
                numero_linea = random.randint(1, 5)

                # Añadir el producto al pedido
                formulary["detalles_pedido"].append({
                    "codigo_producto": codigo_producto,
                    "cantidad": int(input("Ingrese la cantidad del producto: ")),
                    "precio_unitario": precio_unitario,
                    "numero_linea": numero_linea
                })
                break  # Salir del bucle una vez que el producto se ha agregado correctamente
            else:
                # Si no se encuentra el producto, seguir pidiendo el código
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



    