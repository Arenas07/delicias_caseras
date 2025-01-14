from logic.products import saveAll as saveAllProducts

def adjustStockAndAddToOrder(product, dataProducts, formulary, codigo_producto, precio_unitario, numero_linea): #Funcion para validar la suma del producto al json
    cantidad_en_stock = product["cantidad_en_stock"]
    
    while True:
        try:
            if cantidad_en_stock >= 10: #Si la cantidad en stock es mayor o igual a 10
                cantidad = int(input(f"Ingrese la cantidad del producto (Disponible: {cantidad_en_stock}): "))
                if cantidad > 0 and cantidad <= cantidad_en_stock: #La cantidad tiene que ser mayor a 0 pero menor que la que hay en stock en el JSON de productos
                    product["cantidad_en_stock"] -= cantidad #Resta el stock del producto
                    formulary["detalles_pedido"].append({
                    "codigo_producto": codigo_producto,
                    "cantidad": cantidad,
                    "precio_unitario": precio_unitario,
                    "numero_linea": numero_linea
                    })
                    saveAllProducts(dataProducts) #Guarda los cambios
                    print(f"Producto {codigo_producto} añadido correctamente al pedido.")
                    break
                else:
                    print(f"Cantidad inválida. Debe ser entre 1 y {cantidad_en_stock}.")
            else:
                cantidad = int(input(f"--QUEDAN POCAS EXISTENCIAS-- Ingrese la cantidad del producto (Disponible: {cantidad_en_stock}): ")) 
                #Si el producto tiene menos de 10 existencias, se muestra un mensaje de alerta pero hace lo mismo
                if cantidad > 0 and cantidad <= cantidad_en_stock:
                    product["cantidad_en_stock"] -= cantidad
                    formulary["detalles_pedido"].append({
                    "codigo_producto": codigo_producto,
                    "cantidad": cantidad,
                    "precio_unitario": precio_unitario,
                    "numero_linea": numero_linea
                    })
                    saveAllProducts(dataProducts)
                    print(f"Producto {codigo_producto} añadido correctamente al pedido.")
                    break
                else:
                    print(f"Cantidad inválida. Debe ser entre 1 y {cantidad_en_stock}.")
        except ValueError:
            print("Ingrese un valor numérico válido.")