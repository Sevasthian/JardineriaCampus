import json
import requests
import modules.getPedido as gP
from tabulate import tabulate
import modules.postProducto as pstP



def updatePedido(id):
    data = gP.DeletePedidoID(id)
    if data is None:
            print(f"""

Id del producto no encontrado. """)
    
    while True:
        try:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
            print(f"""
Datos para modificar: """)
            for i, (val) in enumerate(data[0].items()):
                print(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if datoModificar == "cantidadEnStock" or "precio_venta" or "precio_proveedor":
                    data[0][datoModificar] = int(nuevoValor)
                    break
                else:
                    data[0][datoModificar] = nuevoValor
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            print(error)
    
    peticion = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Modificado"
    return [res]
            