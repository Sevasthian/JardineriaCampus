import os
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG
import re
import modules.getProducto as gP



def postProducto():
    producto = dict()
    while True:
        try:
            if not producto.get("codigo_producto"):
                codigo = input("Ingrese el codigo del producto: ")
                if re.match(r'^[A-Z]{2}-\d{3}$', codigo) is not None:
                    if gP.getProductoCodigo(codigo):
                        raise Exception("El codigo ingresado ya existe.")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception(f"El codigo no cumple con el estandar establecido ( ejm: XX-111 ).")
                
            if not producto.get("nombre"):
                nombre = input(f"Ingrese el nombre del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    producto["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not producto.get("gama"):
                gama = input("Ingrese la gama del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', nombre) is not None:
                    asd = gG.getAllNombre(gama)
                    if asd:
                        producto["gama"] = gama
                    else:
                        raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                else:
                    raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                
            if not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones del producto: ")
                if re.match(r'^\d+-\d+$', dimensiones) is not None:
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas, la forma correcta es ( numero-numero ).")
                
            if not producto.get("proveedor"): 
                proveedor = input("Ingrese el proveedor: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("Proveedor no valido, recuerde que la primera palabra debe iniciar con mayúsculas.")
                
            if not producto.get("descripcion"):
                descripcion = input("Ingrese una descripción: ")
                producto["descripcion"] = descripcion
            
            if not producto.get("cantidadEnStock"):
                cantidad = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', cantidad) is not None:
                    cantidad = int(cantidad)
                    producto["cantidadEnStock"] = cantidad
                else:
                    raise Exception("Cantidad no valida, asegurese de ingresar solo dígitos numéricos.")
                
            if not producto.get("precio_venta"):
                PrecioVenta = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', PrecioVenta) is not None:
                    PrecioVenta = int(PrecioVenta)
                    producto["precio_venta"] = PrecioVenta
                else:
                    raise Exception("Precio de venta no valido, asegurese de ingresar solo dígitos numéricos.")
                
            if not producto.get("precio_proveedor"):
                PrecioProveedor = input("Ingrese el precio del proveedor: ")
                if re.match(r'^[0-9]+$', PrecioProveedor) is not None:
                    PrecioProveedor = int(PrecioProveedor)
                    producto["precio_proveedor"] = PrecioProveedor
                    break
                else:
                    raise Exception("Precio de proveedor no valido, asegurese de ingresar solo dígitos numéricos.")
        
        except Exception as error:
            print(error)                     
    
    peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


def deleteProducto(id):
    data = gP.DeleteProductoID(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Producto no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
    print("Producto eliminado correctamente")


    
    
    

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

 