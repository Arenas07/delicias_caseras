from design.products import *
from design.general import *
from logic.products import updateInventoryByCode
from design.customer import *
from design.order import *

def menu():
    print("""
          ****************************************
                Bienvenido al menú principal
             Pedidos clientes   |   Productos
                     1          |       2
          ****************************************
          """)
    principal = input("Ingrese el número de la opción: ")
    match principal:
        case "1":
           while True:
               option = designClient()
               match option:
                   case "1":
                       formularyTakeOrder()
                       
        case "2":
            while True:
                option = obtener_opcion()
                match option:
                    case 1:
                        tableProducts()
                    case 2:
                        tableProductsByCategory(input("Ingrese la categoria. Ejemplo ('panes', 'pastel', 'postre'): ").lower())
                    case 3:
                        tableProductsByCode(input("Ingrese el codigo del producto: "))
                    case 4:
                        tableProductsByName(input("Ingrese el nombre del producto: "))
                    case 5:
                        updateInventoryByCode(input("Ingrese el codigo del producto: "))
                    case 6:
                        newProduct() 
                    case 0:
                        return menu()
        case _:
            print("Opción no válida")