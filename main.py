from design.products import design, tableProducts

match design():
    case 1:
        tableProducts()
    case _:
        print("Esa opción no existe")