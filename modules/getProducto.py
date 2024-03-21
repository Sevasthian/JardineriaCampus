
from tabulate import tabulate
import requests
import os



#Devuelve un lisstado con todos los productos que pertenecen a la gama Ornamentales y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, mostrando en primer lugar los de mayor precio.
def getAllData():
    try:
        peticion =  requests.get("http://154.38.171.54:5008/productos")
        dat = peticion.json()
        return dat
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def DeleteProductoID(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def getProductoC(codigo):
    try:
        peticion = requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
def getProductoCodigo(codigo):
    for val in getAllData():
        if val.get("codigo_producto")  == codigo:
            return [val] 
    
def getAllStocksPriceGama(gama, stock):
    condiciones = list()
    for val in getAllData():
        if((val.get("gama") == gama) and (val.get("cantidadEnStock") >= stock)):
            condiciones.append(val)
            
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse = True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidadEnStock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones  
def menu():
    while True:
        os.system("clear")
        print('''
          

    ____                        __                   __                             __           __      
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____ 
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ sevas
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ /
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/ 
          /_/                                             /_/                                            


            1. Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su 
              cantidad de inventario sea superior (ejem: Ordamentales 100)
            2. Regrese al menu principal   
            3. Salir del programa  
           ''')
        try:
            opcio = int(input("Escribe una opcion: "))
            if (opcio == 1):
                gama = input("Escriba la categoria deceada: ")
                stock = int(input("Ingrese las unidades que tiene el precio de venta: "))
                print(tabulate(getAllStocksPriceGama(gama, stock)))
                input("Oprima una tecla para continuar...")
            elif(opcio == 2):
                break
            elif(opcio == 3):
                exit()
        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")