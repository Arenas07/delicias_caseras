import json
def findAllOrders():
    try:
        with open("data/order.json", "r", encoding="utf-8") as file:
            data = file.read()  # Leer el contenido del archivo
            return json.loads(data)  # Convertir el contenido a una estructura de datos
    except FileNotFoundError:
        return []  # Si no se encuentra el archivo, retornamos una lista vacía

def findAllProducts():
    # Supongamos que esta función devuelve la lista de productos desde el archivo products.json
    with open("data/products.json", "r", encoding="utf-8") as file:
        data = file.read()  # Leer el contenido del archivo
        return json.loads(data)  # Convertir el contenido a una estructura de datos

# Función para guardar los datos en el archivo JSON
def saveAll(data):
    with open("data/order.json", "w", encoding="utf-8") as file:
        convertJson = json.dumps(data, indent=4, ensure_ascii=False)  # Convertir a formato JSON con indentación
        file.write(convertJson)  # Escribir los datos al archivo
        print("Archivo actualizado correctamente.")