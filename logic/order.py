import json

def findAllOrders():
    try:
        with open("data/order.json", "r", encoding="utf-8") as file:
            data = file.read()  # Leer el contenido del archivo
            return json.loads(data)  # Convertir el contenido a una estructura de datos
    except FileNotFoundError:
        return [] 

# Función para guardar los datos en el archivo JSON
def saveAll(data):
    with open("data/order.json", "w", encoding="utf-8") as file:
        # Convertir la estructura de datos a formato JSON y escribirla en el archivo
        convertJson = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJson)
        return "Se modificó el archivo order.json"
