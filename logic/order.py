import json
from tabulate import tabulate
from logic.products import findAll, saveAll as saveAllProducts
from formula.products import *
def findAllOrders(): #Encontrar todos los archivos en el JSON
        try:
            with open("data/order.json", "r", encoding="utf-8") as file:
                data = file.read() 
                return json.loads(data) 
        except FileNotFoundError:
            return [] 

def saveAll(data): #Editar los archivos en el JSON
        with open("data/order.json", "w", encoding="utf-8") as file:
            str(data).encode('utf-8')
            convertJson = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(convertJson)
            return "Se modificó el archivo order.json"

def editOrder(order_code): #Funcion para poder editar la cantidad pedida en la orden
    data_orders = findAllOrders() #Muestra todas las ordenes
    data_products = findAll() #Muestra todos los productos

    for order in data_orders: #Va pasando por la info de cada llave 
        if order.get("codigo_pedido") == order_code:   #Hasta que encuentra que el codigo proporcionado es igual al codigo de la orden
            print(f"Detalles actuales del pedido {order_code}:\n")

            detalles_tabla = [
                [detalle["codigo_producto"], detalle["cantidad"], detalle["precio_unidad"], detalle["numero_linea"]]
                for detalle in order["detalles_pedido"]
            ]
            print(tabulate(detalles_tabla, headers=["Código Producto", "Cantidad", "Precio Unidad", "Número Línea"], tablefmt="fancy_grid"))

            for detalle in order["detalles_pedido"]:
                print(f"\nModificando detalle: {detalle}")
                nuevo_codigo_producto = input(f'Digite el codigo actual del producto" (actual: {detalle["codigo_producto"]}): ') or detalle["codigo_producto"]
                nueva_cantidad = input(f'Nueva "cantidad" (actual: {detalle["cantidad"]}): ') 

                cantidad_actual = detalle["cantidad"]
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else cantidad_actual #Si la cantidad es igual a 0, se mantiene la cantidad actual
                diferencia = nueva_cantidad - cantidad_actual #Se hace el proceso para saber si el cliente quiere más o menos cosas
                if diferencia > 0: #Si el cliente quiere más cosas
                    resultado = restarStock(nuevo_codigo_producto, diferencia, data_products)
                    if isinstance(resultado, str):  #Validador
                        print(resultado)
                        return
                elif diferencia < 0: #Si el cliente quiere menos cosas
                    resultado = sumarStock(nuevo_codigo_producto, abs(diferencia), data_products)
                    if isinstance(resultado, str):   #Validador
                        print(resultado)
                        return
                detalle.update({
                    "codigo_producto": nuevo_codigo_producto,
                    "cantidad": nueva_cantidad
                })

            print(f"\nPedido {order_code} actualizado con éxito.")
            break
    else: #Si no encuentra el codigo de la orden
        print(f"No se encontró ningún pedido con codigo_pedido {order_code}.")
        input("Presione enter para continuar: ")

def deleteJSON(product_code): #Borrar un pedido realizado
    info = findAllOrders()
    
    for code in info: 
        if product_code == code.get("codigo_pedido"): #Si el codigo es igual al codigo del pedido
            security = input("¿Está seguro de eliminar el pedido? (s/n): ")
            if security.lower() == "s":  
                info.remove(code)  
                saveAll(info)  
                return "Pedido eliminado correctamente."
            else:
                return input("Operación cancelada, presione enter para continuar: ")
        else:
            print(input("Código no encontrado, presione enter para continuar: "))
            break
    