import os
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG
import re
import modules.getProducto as gP



def postProducto():
    producto = {}
    while True:
        try:
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo) is not None):
                    data = gP.getProductCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="githud"))
                        raise Exception("El codigo producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("El codigo producto no cumple con el estandar establecido")
            if(not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if(re.match(r'⁽[A-Z][a-z]*\s*)+',nombre)is not None):
                    producto["nombre"]= nombre
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")
            if(not producto.get("gama")):
                gama = input("Ingrese la gama del producto: ")
                if(re.match(r'^(Ornamentales|Frutales|Aromáticas|Herramientas)$', gama)is not None):
                    gama["gama"] = gama
                else:
                    raise Exception("Tiene que elegir entre Ornamentales, Frutales, Aromáticas y Herramientas")
            if(not producto.get("dimenciones")):
                dimenciones = input("Ingrese las dimenciones del producto: ")
                if(re.match(r'^[0-9\s.,!?]+$', dimenciones)is not None):
                    dimenciones["producto"] = dimenciones
                else:
                    raise Exception("Escriba bien ")
            print(producto)
        except Exception as error:
            print(error)
        peticion = requests.post("", data=json.dumps(producto, indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Producto Guardado"
        return [res] 

        
     


    
    
    

# producto = {
#     "codigo_producto":input("Ingrese el codigo del producto: "),
#     "nombre": input("Ingrese el nombre del producto: "),
#     "gama": gG.getAllNombre()[int(input("Selecione la gaa:\n"+"".join([f"\t{i}.{val}\n" for i, val in enumerate(gG.getAllNombre())])))],
#     "dimensiones": input("Ingrse la dimensiones del producto: "),
#     "proveedor": input("Ingrse el proveedor del producto: "),
#     "descripcion": input("Ingrse el descripcion del producto: "),
#     "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
#     "precio_venta": int(input("Ingrse el precio de ventas: ")),
#     "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
#     }
#json-server storage/producto.json -b 5002
# peticion = requests.post("http://172.16.100.145:5003", data=json.dumps(producto, indent = 4).encode(("UTF-8")))
# res = peticion.json()
# res["Mensaje"] = "Producto Guardado"
# return [res]

  
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
        if (opcio == 0):
            break
        elif(opcio == 1):
            print(tabulate(postProducto()))
            input("Precione una tecla para continuar...")
        elif(opcio == 2):
            exit()
        