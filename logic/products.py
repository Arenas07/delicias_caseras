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

def newProduct():
    data = findAll()
    codigo_producto = input("Ingrese el código del producto: ")
    findProducts = list(filter(lambda product: product.get("codigo_producto") == codigo_producto, data))
    if(not len(findProducts)):
        newProduct = {
            "codigo_producto": codigo_producto,
            "nombre": input("Ingrese el nombre del producto: "),
            "categoria": input("Ingrese la categoria del producto ('Panes', 'Pastel', 'Postre'): ").capitalize(),
            "descripcion": input("Ingrese la descripción del producto: "),
            "proveedor": input("Ingrese el proveedor de dicho producto: "),
            "cantidad_en_stock": int(input("Ingrese la cantidad en stock del producto: ")),
            "precio_venta": float(input("Ingrese el precio de venta del producto: ")),
            "precio_proveedor": float(input("Ingrese el precio del proveedor: "))
     }
        data.append(newProduct)
        saveAll(data)
        return "Producto agregado exitosamente"
    else:
        print("""
        *********************
            ERROR-ERROR 
        El producto ya existe
        *********************""")



