import json
from tabulate import tabulate
from logic.products import findAll, saveAll as saveProduct
from formula.products import restarStock, sumarStock, updateQuantityInventory
def findAllOrders(): #Encontrar todos los archivos en el JSON
        with open("data/order.json", "r", encoding="utf-8") as file:
                data = file.read() 
                return json.loads(data) 

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
                [detalle["codigo_producto"], detalle["cantidad"], detalle["precio_unitario"], detalle["numero_linea"]]
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

            # Guardar cambios en el archivo JSON
            saveAll(data_orders)

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
    print("El codigo no existe")

def removeProductFromOrder(productCode):
    data = findAllOrders()  # Obtener todas las órdenes
    dataProducts = findAll()  # Obtener todos los productos
    # Buscar el pedido específico por el código de pedido
    findOrder = list(filter(lambda product: product.get("codigo_pedido") == int(productCode), data))
    if not findOrder:
        print(f"Pedido con código {productCode} no encontrado.")
        return
    
    findOrder = findOrder[0]  # Obtener el primer pedido encontrado
    print(f'Pedido # {findOrder.get("codigo_pedido")} - Fecha: {findOrder.get("fecha_pedido")} - Cliente: {findOrder.get("codigo_cliente")}')
    print(tabulate(findOrder.get("detalles_pedido"), headers="keys", tablefmt="orgtbl", numalign="center", showindex="always"))
    
    codigoProduct = input("Ingrese el codigo que desea remover (EJ: PN-001): ")
    findProduct = list(filter(lambda product: product.get("codigo_producto") == codigoProduct, findOrder.get("detalles_pedido")))
    
    if len(findProduct) == 0: 
        print("El producto no se encuentra en el pedido")
    else:
        productRemove = None
        for indice, product in enumerate(findOrder.get("detalles_pedido")):
            if product.get("codigo_producto") == codigoProduct:
                productRemove = findOrder.get("detalles_pedido").pop(indice)
                break  # Una vez que encuentras y eliminas el producto, salimos del bucle

        # Actualizar inventario
        for product in dataProducts:
            if product.get("codigo_producto") == codigoProduct:
                quantity = productRemove.get("cantidad")
                stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
                product.update({"cantidad_en_stock": stock})

        # Guardar el producto actualizado en el inventario
        print(saveProduct(dataProducts))  # Si es necesario, puedes eliminar esto si no es necesario imprimir
        
        # Actualizar la lista de órdenes
        print(f'Pedido # {findOrder.get("codigo_pedido")} - Fecha: {findOrder.get("fecha_pedido")} - Cliente: {findOrder.get("codigo_cliente")}')
        print(tabulate(findOrder.get("detalles_pedido"), headers="keys", tablefmt="orgtbl", numalign="center", showindex="always"))
        
        # Actualizar la lista completa de órdenes, reemplazando el pedido modificado
        for i, order in enumerate(data):
            if order.get("codigo_pedido") == int(productCode):
                data[i] = findOrder  # Reemplazar el pedido actualizado en la lista de órdenes
        
        # Guardar todas las órdenes, no solo el pedido
        saveAll(data)  # Guardar el archivo con todos los pedidos actualizados

