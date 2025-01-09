from design.products import tableProducts, tableProductsByCategory, obtener_opcion
from logic.products import updateInventoryByCode, newProduct
while True:
    option = obtener_opcion()
    match option:
        case 1:
            tableProducts()
        case 2:
            tableProductsByCategory(input("Ingrese la categoria. Ejemplo ('panes', 'pastel', 'postre'): ").capitalize())
        case 3:
            updateInventoryByCode(input("Ingrese el codigo del producto: "))
        case 4:
            newProduct(
            input("Ingrese el codigo del producto: "),
            input("Ingrese el nombre del producto: "),
            input("Ingrese la categoria del producto (Panes, Pasteles, Postres): ".capitalize()),
            input("Ingrese la descripcion del producto: "),
            input("Ingrese el proveedor del producto: "),
            int(input("Ingrese la cantidad en stock del producto: ")),
            float(input("Ingrese el precio de venta del producto: ")),
            float(input("Ingrese el precio del proveedor del producto: "))
            )
            
        case 0:
            print("Chao")
            break