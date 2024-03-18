import json
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPagos as pago
import modules.getProducto as producto
import modules.postProducto as post
from tabulate import tabulate
import modules.postEmpleado as PEmp
import requests

import os

# def menu():
#     print('''
# Menu principal
#           1. cliente
#           2. oficina
#           3. empleado
#           4. pedidos
#           ''')
# print(dir())

# # # print(pedido. getAllPedidosEntregadosEnero())
# def menu():
#     contador = 1
#     print("Menu principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modulo"):
#             modulo = getattr(objeto, "__name__", None)
#         if(modulo != "modulo"):
#         
# }

#    file = modulo.split("get")[- 1]
#             print(f'''{contador}.{file}''')
# #             contador += 1
# """ 
# def menuEmpleado():
#       os.system("clear")
#       while True:
#         print('''

#     ____  _                            _     __               __                                  
#    / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /                                  
#   / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /                                   
#  / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /                                    
# /_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/        __               __          
#    ____ ___  ___  ____  __/_/_   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
#   / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
#  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
# /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
#                                                           /_/                                     
#         0. Atras
#               1.Reportes de los empleados
#               2.Guardar alguna empleado
#         3. Cerrar el programa

# ''')
#         try:
#                 opciones = int(input("Ingrese el numero de la opcion deceada: "))
#                 if opciones == 0:
#                         break
#                 elif opciones == 1:
#                         cliente.menu()
#                 elif opciones == 2:
#                         PEmp.menu()
#                 elif opciones == 3:
#                       exit()
#         except ValueError as error:
#               print("Oprima enter para continuar con el programa", error)
#         except KeyboardInterrupt as error:
#               print("Oprima enter para continuar con el programa", error)          
# def menuGamas():
#       print()
# def menuOficina():
#       print()
# def menuPagos():
#       print()
# def menuPedido():
#       print()
# def menuProducto():
#     while True:
#         print('''
                        
#           ____  _                            _     __               __                             
#          / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __
#         / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /
#         / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ / 
#         /_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/ __\__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/  
#         ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____                            
#         / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                            
#         / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                             
#         \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                              
#                 /_/                                                                              
#         0. Atras
#                 1. Reportes de los productos
#                 2. Guardar algun producto
#         3. Cerrar programa
                        
#                         ''')
#         try:
#                 opcion = int(input("selecione una de las opciones: "))   
#                 if(opcion == 1):
#                         producto.menu()
#                 elif(opcion == 2):
#                         post.menu()
#                 elif(opcion == 0):
#                       break
#                 elif(opcion == 3):
#                       exit()
#         except ValueError as error:
#               print("Oprima enter para continuar con el programa", error)
#         except KeyboardInterrupt as error:
#               print("Oprima enter para continuar con el programa", error)

if(__name__ == "__main__"):
  numero = 500
  peticion = requests.get(f"http://172.16.100.145:5000/productos?cantidad_en_stock_gte={numero}")
  data = peticion.json()
#   print(tabulate((data), headers="keys", tablefmt="github"))
  print(json.dumps(data, indent=4))
        # with open("storage/producto.json", "r") as f:
        #         fichero = f.read()
        #         data = json.loads(fichero)
        # for i, val in enumerate(data):
        #         data[i]["id"] = (i+1)
        #         data = json.dumps(data, indent=4).encode("utf-8")
        # with open("storage/producto.json", "wb+") as f1:
        #         f1.write(data)
        #         f1.close()

        

#     while True:
#         os.system("clear")
#         print("""
          
    
#      __  ___                               _            _             __   
#    /  |/  /__  ____  __  __   ____  _____(_)___  _____(_)___  ____ _/ /   
#   / /|_/ / _ \/ __ \/ / / /  / __ \/ ___/ / __ \/ ___/ / __ \/ __ `/ /    
#  / /  / /  __/ / / / /_/ /  / /_/ / /  / / / / / /__/ / /_/ / /_/ / /     
# /_/  /_/\___/_/ /_/\__,_/  / .___/_/  /_/_/ /_/\___/_/ .___/\__,_/_/      
#                           /_/                       /_/                   
                                                                      
#                              1. Cliente
#                              2. Oficina
#                              3. Empleado
#                              4. Pedidos
#                              5. Pagos
#                              6. Producto 
#                              7. Cerrar el programa
#  """)
#         try:
#             opcion = int(input("\nselecione una de las opciones: "))   
#             if(opcion == 1):
#                     cliente.menu()
#             elif(opcion == 2):
#                     oficina.menu()
#             elif(opcion == 3):
#                     empleado.menu()
#             elif(opcion == 4):
#                     pedido.menu()
#             elif(opcion == 5):
#                 pago.menu()
#             elif(opcion == 6):
#                 menuProducto()
#             elif(opcion == 7):
#                 break

#         except ValueError as error:
#             print(error)
#             input("Oprima enter para volver a cargar el programa")
#         except KeyboardInterrupt as error:
#               print(error)
#               input("Oprima alguna tecla para continuar con el programa")
             
        



# # try:
#     entrada = input("Ingresa algo: ")
#     # Aquí puedes hacer lo que necesites con la entrada
#     print("Entrada recibida:", entrada)
# except KeyboardInterrupt:
#     print(tabulate(cliente.getAllClientesName()))
