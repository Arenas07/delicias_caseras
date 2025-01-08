import json
def findAll():
    with open("data/products.json", "r") as file:
        data = file.read() #Read es para hacerlo un string
        converted = json.loads(data) #Lo convierte a estructura de datos
        return converted