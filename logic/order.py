import json
from tabulate import tabulate
from logic.products import findAll, saveAll as saveAllProducts
from formula.products import *
def findAllOrders():
        try:
            with open("data/order.json", "r", encoding="utf-8") as file:
                data = file.read() 
                return json.loads(data) 
        except FileNotFoundError:
            return [] 

def saveAll(data):
        with open("data/order.json", "w", encoding="utf-8") as file:
            str(data).encode('utf-8')
            convertJson = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(convertJson)
            return "Se modificó el archivo order.json"

def editOrder(order_code):
    data_orders = findAllOrders()
    data_products = findAll()

    for order in data_orders:
        if order.get("codigo_pedido") == order_code:
            print(f"Detalles actuales del pedido {order_code}:\n")

            detalles_tabla = [
                [detalle["codigo_producto"], detalle["cantidad"], detalle["precio_unidad"], detalle["numero_linea"]]
                for detalle in order["detalles_pedido"]
            ]
            print(tabulate(detalles_tabla, headers=["Código Producto", "Cantidad", "Precio Unidad", "Número Línea"], tablefmt="fancy_grid"))

            for detalle in order["detalles_pedido"]:
                print(f"\nModificando detalle: {detalle}")
                nuevo_codigo_producto = input(f'Nuevo "codigo_producto" (actual: {detalle["codigo_producto"]}): ') or detalle["codigo_producto"]
                nueva_cantidad = input(f'Nueva "cantidad" (actual: {detalle["cantidad"]}): ')

                cantidad_actual = detalle["cantidad"]
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else cantidad_actual
                diferencia = nueva_cantidad - cantidad_actual
                if diferencia > 0:
                    resultado = restarStock(nuevo_codigo_producto, diferencia, data_products)
                    if isinstance(resultado, str):  
                        print(resultado)
                        return
                elif diferencia < 0:
                    resultado = sumarStock(nuevo_codigo_producto, abs(diferencia), data_products)
                    if isinstance(resultado, str):  
                        print(resultado)
                        return
                detalle.update({
                    "codigo_producto": nuevo_codigo_producto,
                    "cantidad": nueva_cantidad
                })

            print(f"\nPedido {order_code} actualizado con éxito.")
            break
    else:
        print(f"No se encontró ningún pedido con codigo_pedido {order_code}.")

    print(saveAllProducts(data_products))  
    print(saveAll(data_orders))

def deleteJSON(product_code):
    info = findAllOrders()
    for code in info:
        if code.get("codigo_pedido") == product_code:
            security = input("¿Está seguro de eliminar el pedido? (s/n): ")
            if security.lower() == "s":
                info.remove(code)
                saveAll(info)
                return "Pedido eliminado correctamente."
            else:
                   return "Operación cancelada."
        else:
            return print("Pedido no encontrado.")
        