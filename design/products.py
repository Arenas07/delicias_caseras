from logic.products import findAll

def design():
    print("""
    Menu de productos
        1. Ver productos
        0. Salir 
    """)
    return int(input())

def tableProducts():
    data = findAll()
    print("    Todos los productos\n")
    indice = 0
    for product in data:
        print(f'{indice}. {product.get("nombre")} | category: {product.get("categoria")} | price: ${product.get("precio_venta")}')
        indice += 1