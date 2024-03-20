import json
import requests
import modules.getProducto as gP
from tabulate import tabulate
def updateProductoNombre(codigo):
    while True:

        producto = gP.getProductCodigo(codigo)
        if(len(producto)):
            if(codigo != None):
                producto = gP.getProductCodigo(codigo)
                if(len(producto)):

                    print(tabulate(producto))
                    opc = int(input('''
                  ¿Este es el producto que desea actualiza
                            1. Si
                            0. No
                  '''))
                    if(opc):
                        hearders = {'Content= type': 'aplicacion/json', 'charset':'UTF-8'}
                        producto[0]["nombre"] = input("Ingrese el nuevo nombre del producto: ")
                        peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', hearders = )
                        data = peticion.json()
                        return [data]
                    else:
                        codigo = None
                else:
                    print(f'El producto {codigo} no existe')
                    codigo = None

        else:
            codigo = input("Ingrese el codigo del producto")

            

                
