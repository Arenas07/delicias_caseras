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
            newProduct() 
        case 0:
            print("Chao")
            break

#NECESITO CORREGIR LOS CASES    