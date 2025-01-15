from logic.order import findAllOrders
from tabulate import tabulate
def designOrder():
    print("""
          *********************
            Menu de pedidos
        1. Editar el stock de un pedido
        2. Eliminar pedido
        3. Remover un producto del pedido
        0. Salir
          *********************
        """)
    opc = input()
    return opc

def seeOrders(): #Función para ver las ordenes realizadas
    data = findAllOrders() #Data va a tomar la informacion de todos los pedidos

    for pedido in data: #Recorre todos los pedidos en la data
        print(f"--- Pedido: {pedido['codigo_pedido']} | Cliente: {pedido['codigo_cliente']} | Fecha: {pedido['fecha_pedido']}") 
        #Toma los valores de la llave en la que está posicionado actualmente para poder imprimir despues
        print(tabulate  (pedido["detalles_pedido"], headers="keys", tablefmt="grid", numalign="center"))
        print("\n" + "="*50 + "\n")
    input("Presione Enter para continuar: ")

