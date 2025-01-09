from design.products import design, tableProducts, tableProductsByCategory
from logic.products import updateInventoryByCode

match design():
    case 1:
        tableProducts()
    case 2:
        tableProductsByCategory(input("Ingrese la categoria. Ejemplo ('panes', 'pastel', 'postres'): ").lower())
    case 3:
        updateInventoryByCode(input("Ingrese el codigo del producto: "))
    case 0:
        print("Chao")
    case _:
        print("Esa opción no existe")