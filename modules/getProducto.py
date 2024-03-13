
from tabulate import tabulate
import requests
import modules.postProducto as pstProducto
import json


#Devuelve un lisstado con todos los productos que pertenecen a la gama Ornamentales y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, mostrando en primer lugar los de mayor precio.
def getAllData():
    peticion = requests.get("http://172.16.100.145:5003")
    data = peticion.json()
    return data

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("precio_venta") >= stock) :
            condiciones.append(val)
        def price(val):
            return val.get("precio_venta")
    condiciones.sort(key = price)
    for i, val in enumerate(condiciones):
        if(condiciones[i].get("descripcion")):
            condiciones[0] = {
                "codigo": val.get("codigo_producto"),
                "venta" : val.get("precio_venta"),
                "nombre" : val.get("nombre"),
                "gama" : val.get("gama"),
                "dimenciones" : val.get("dimensiones"),
                "proveedor" : val.get("proveedor"),
                "descripcion" :f'''{val.get("descripcion")[:5]}...'''if condiciones[i].get("descripcion") else None ,
                "stock" : val.get("cantidad_en_stock"),
                "base" : val.get("precio_provedor"),
            }
            condiciones[i]["descripcion"] = f'''{condiciones[i]["descripcion"][:5]}...'''
    return []
    
    
  
def menu():
    while True:
        print('''
          
    ____                        __                   __              _____      _            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  / __(_)____(_)___  ____ _
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ / 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/  
          /_/                                                                                

            1. Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea superior (ejem: Ordamentales 100)
            2. Regrese al menu principal   
            3. Salir del programa  
           ''')
        opcio = int(input("Escribe una opcion: "))
        if (opcio == 1):
            gama = input("Escriba la categoria deceada")
            stock = int(input("Ingrse las unidades: "))
            print(tabulate(getAllStocksPriceGama(gama, stock)))
        elif(opcio == 2):
            producto = {
            "codigo_producto": input("Ingrese el codigo del producto"),
            "nombre": input("Ingrese el nombre del producto: "),
            "gama":gG.getAllNombre() [int(input("\t\n".join([f"{i}.{val}" for i in val enumerate(gG.getAllNombre())])),
            "dimensiones": input("Ingrese las dimensiones del prducto: "),
            "proveedor":input("Ingrese el nombre del proevedor: "),
            "cantidad del stock":int(input("stock")),
            "descripcion": (input("Ingrese la descripcion del producto: ")),
            "precio_venta": int(input("Xd")),
            "precio_proveedor":int(input("XD"))
        }
            pstProducto.postProducto(producto)
            print("Producto guardado")
        elif(opcio == 3):
            exit()
        menu ()