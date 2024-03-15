import json
import os
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG



def postProducto():
    producto = {
        "codigo_producto":input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gaa:\n"+"".join([f"\t{i}.{val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
        }
    #json-server storage/producto.json -b 5002
    peticion = requests.post("http://172.16.100.145:5003", data=json.dumps(producto, indent = 4).encode(("UTF-8")))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

  
def menu():
    while True:
        os.system("clear")
        print('''
          

    ___       __          _       _      __                         __      __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/ 
                          ____  _________  ____/ /_  _______/ /_____  _____                            
                         / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                            
                        / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                             
                       / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                              
                      /_/                                                                              

            0. Atras
            1. Guardar un producto nuevo
            2. Cerrar programa
           ''')
        
        opcio = int(input("Escribe una opcion: "))
        if (opcio == 1):
            break
        elif(opcio == 2):
            print(tabulate(postProducto()))
            input("Precione una tecla para continuar...")
        elif(opcio == 3):
            exit()
        