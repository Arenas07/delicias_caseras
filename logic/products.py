import json
from formula.products import updateQuantityInventory

def findAll():
    with open("data/products.json", "r") as file:
        data = file.read() #Read es para hacerlo un string
        convertListOrDict = json.loads(data) #Lo convierte a estructura de datos
        return convertListOrDict

def saveAll(data):
    with open("data/products.json", "w", encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJson = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJson)
        return "Se modificó el archivo products.json"

def updateInventoryByCode(product_code):
    data = findAll()
    for product in data:
        if(product.get("codigo_producto") == product_code):
            quantity = int(input("Ingrese la cantidad de productos que desea actualizar: "))
            stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
            product.update({"cantidad_en_stock": stock})
            print(f"Se actualizó el {product_code} a {stock}")
    print(saveAll(data))

def newProduct(codigo_producto, nombre, categoria, descripcion, proveedor, cantidad_en_stock, precio_venta, precio_proveedor):
    data = findAll()
    newProduct = {
        "codigo_producto": codigo_producto,
        "nombre": nombre,
        "categoria": categoria,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "cantidad_en_stock": cantidad_en_stock,
        "precio_venta": precio_venta,
        "precio_proveedor": precio_proveedor
    }
    data.append(newProduct)
    saveAll(data)
    return "Producto agregado exitosamente"



