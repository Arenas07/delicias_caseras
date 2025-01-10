from logic.products import findAll as findAllProducts
from logic.order import findAll as findAllOrders
from tabulate import tabulate
from datetime import datetime

def designClient():
    print("""
          *********************
            Menu de clientes
        1. Realizar pedido
        2. Ver pedidos realizados
        0. Salir
          *********************
        """)
    opc = int(input())
    return opc

def formularyTakeOrder():
    dataProducts = findAllProducts()
    dataOrders = findAllOrders()
    findProductsMajor = list(filter(lambda product: product.get("cantidad_en_stock") > 0, dataProducts))
    findProducts = list(filter(lambda product: (product.pop("descripcion"), (product.pop("proveedor"), (product.pop("precio_proveedor"), (product.pop("categoria"))))), findProductsMajor))
    print("Lista de productos en stock")
    print (tabulate(findProducts, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    now = datetime.now()
    format = now.strftime("%d/%m/%Y")
    
    for indice, product in enumerate(dataOrders):
        dataOrders[indice] = product.get("codigo_pedido")   
        
    
    
    formulary = dict({
        "codigo_pedido": dataOrders[-1] + 1,
        "codigo_cliente": input("Ingrese el código del cliente (EJ: CL-001): "),
        "fecha_pedido": format,
        "detalles_pedido": []            
        })