from logic.products import saveAll as saveAllProducts

def adjustStockAndAddToOrder(product, dataProducts, formulary, codigo_producto, precio_unitario, numero_linea):
    cantidad_en_stock = product["cantidad_en_stock"]
    
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad del producto (Disponible: {cantidad_en_stock}): "))
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