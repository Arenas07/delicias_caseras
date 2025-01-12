from logic.products import saveAll as saveAllProducts

def adjustStockAndAddToOrder(product, dataProducts, formulary, codigo_producto, precio_unitario, numero_linea):
    cantidad_en_stock = product["cantidad_en_stock"]
    
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad del producto (Disponible: {cantidad_en_stock}): "))
            if cantidad > 0 and cantidad <= cantidad_en_stock:
                # Actualizar el stock del producto
                product["cantidad_en_stock"] -= cantidad
                saveAllProducts(dataProducts)  # Guardar los cambios en el inventario

                # Añadir el producto al pedido
                formulary["detalles_pedido"].append({
                    "codigo_producto": codigo_producto,
                    "cantidad": cantidad,
                    "precio_unitario": precio_unitario,
                    "numero_linea": numero_linea
                })
                print(f"Producto {codigo_producto} añadido correctamente al pedido.")
                break
            else:
                print(f"Cantidad inválida. Debe ser entre 1 y {cantidad_en_stock}.")
        except ValueError:
            print("Ingrese un valor numérico válido.")