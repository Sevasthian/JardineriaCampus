import json
import requests
import modules.getGamas as gG



def postProducto(data):
    import requests
    #json-server storage/producto.json -b 5002
    peticion = requests.post("http://172.16.100.145:5003", data=json.dumps(data))
    res = peticion.json()
    return res

  
def menu():
    while True:
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

            1. Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea superior (ejem: Ordamentales 100)
            2. Salir del programa  
           ''')
        
        # opcio = int(input("Escribe una opcion: "))
        # if (opcio == 1):
        #     gama = input("Escriba la categoria deceada")
        #     stock = int(input("Ingrse las unidades: "))
        #     print(tabulate(getAllStocksPriceGama(gama, stock)))
        # elif(opcio == 2):
        #     producto = {
        #     "codigo_producto": input("Ingrese el codigo del producto"),
        #     "nombre": input("Ingrese el nombre del producto: "),
        #     "gama":gG.getAllNombre() [int(input("\t\n".join([f"{i}.{val}" for i in val enumerate(gG.getAllNombre())])),
        #     "dimensiones": input("Ingrese las dimensiones del prducto: "),
        #     "proveedor":input("Ingrese el nombre del proevedor: "),
        #     "cantidad del stock":int(input("stock")),
        #     "descripcion": (input("Ingrese la descripcion del producto: ")),
        #     "precio_venta": int(input("Xd")),
        #     "precio_proveedor":int(input("XD"))
        # }
        #     pstProducto.postProducto(producto)
        #     print("Producto guardado")
        # elif(opcio == 3):
        #     exit()
        # menu ()