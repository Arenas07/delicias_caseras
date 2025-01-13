def updateQuantityInventory(stock, quantity):
    if(quantity>0):
        stock = stock + quantity
        return stock
    else:
        return stock
    
def restarStock(codigo_producto, cantidad_a_restar, data_products):
    for product in data_products:
        if product["codigo_producto"] == codigo_producto:
            if product["cantidad_en_stock"] >= cantidad_a_restar:
                product["cantidad_en_stock"] -= cantidad_a_restar
                print(f"Restado {cantidad_a_restar} del stock de {codigo_producto}. Stock actual: {product['cantidad_en_stock']}")
                return True
            else:
                return f"Error: Stock insuficiente para el producto {codigo_producto}. Stock disponible: {product['cantidad_en_stock']}"
    return f"Error: Producto {codigo_producto} no encontrado en el inventario."


def sumarStock(codigo_producto, cantidad_a_sumar, data_products):
    for product in data_products:
        if product["codigo_producto"] == codigo_producto:
            product["cantidad_en_stock"] += cantidad_a_sumar
            print(f"Sumado {cantidad_a_sumar} al stock de {codigo_producto}. Stock actual: {product['cantidad_en_stock']}")
            return True  
    return f"Error: Producto {codigo_producto} no encontrado en el inventario."
