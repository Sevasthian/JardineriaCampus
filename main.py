
import json
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPagos as pago
import modules.getProducto as producto
import modules.postProducto as postpro
import modules.getGamas as gama
from tabulate import tabulate
import modules.postEmpleado as PEmp
import modules.postPedido as PstPedi
import modules.postPagos as pstpag
import modules.postOficina as pstOfi
import modules.postGamas as pstGam
import modules.postCliente as pstCli
import requests
import modules.updateProducto as upPro
import os
import modules.updatePedido as upPed
import modules.updateCliente as upCli
import modules.updatePago as upPa
import modules.updateOficina as upOfi
import modules.updateGama as upGam
import modules.updateEmpleado as upEmp

# def menu():
#     print('''
# Menu principal
#           1. cliente
#           2. oficina
#           3. empleado
#           4. pedidos
#           ''')
# print(dir())

# # print(pedido. getAllPedidosEntregadosEnero())
# def menu():
#     contador = 1
#     print("Menu principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modulo"):
#             modulo = getattr(objeto, "__name__", None)
#         if(modulo != "modulo"):
        
# }

#    file = modulo.split("get")[- 1]
#             print(f'''{contador}.{file}''')
# #             contador += 1
# """ 
def menuCliente():
      while True:
            os.system("clear")
            print('''

    

    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     _____/ (_)__  ____  / /____  _____                                               
 / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/                                               
/ /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  )                                                
\__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/                                                 
                                                                                                 

                  0.Atras
                  1. Reportes de los clientes
                  2. Guardas algun cliente
                  3. Actualizar algun cliente
                  4. Eliminar algun cliente
                  5. Cerrar el programa''')
            try:
                opciones = int(input("Ingrese el numero de la opcion deceada: "))
                if opciones == 0:
                        break
                elif opciones == 1:
                        cliente.menu()
                elif opciones == 2:
                        pstCli.postClientes()
                elif opciones == 5:
                        exit()
                elif opciones == 4:
                        pstCli.menu()
                elif opciones == 3:
                        print(tabulate(upCli.updateCliente(idCliente), headers="keys", tablefmt="github"))
                idCliente = input("Ingrese el id del cliente: ")
                
            except ValueError as error:
                    input("Oprima enter para continuar con el programa")
                    print(error)
                    
            except KeyboardInterrupt as error:
                    input("Oprima enter para continuar con el programa")
                    print(error)     
                  
def menuEmpleado():
      while True:
        os.system("clear")
        print('''

    ____  _                            _     __               __                                  
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /                                  
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /                                   
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /                                    
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/        __               __          
   ____ ___  ___  ____  __/_/_   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / / / / / /  __/ / / / /_/ /  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                          /_/                                     
        0. Atras
        1. Reportes de los empleados
        2. Guardar alguna empleado
        3. Actualizar algun empleado
        4. Eliminar algun empleado
        5. Cerrar el programa

''')
        try:
                opciones = int(input("Ingrese el numero de la opcion deceada: "))
                if opciones == 0:
                        break
                elif opciones == 1:
                        empleado.menu()
                elif opciones == 2:
                        PEmp.menu()
                elif opciones == 3:
                        upEmp.updateEmpleado()
                elif opciones == 4:
                        PEmp.deleteEmpleado()
        except ValueError as error:
              input("Oprima enter para continuar con el programa")
              print(error)
              
        except KeyboardInterrupt as error:
              input("Oprima enter para continuar con el programa")
              print(error)          
def menuGamas():
      while True:
            os.system("clear")
            print('''

    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____ _____ _____ ___  ____ ______                                                
 / __  / _ \   / __ `/ __ `/ __ `__ \/ __ `/ ___/                                                
/ /_/ /  __/  / /_/ / /_/ / / / / / / /_/ (__  )                                                 
\__,_/\___/   \__, /\__,_/_/ /_/ /_/\__,_/____/                                                  
             /____/                                                                              

                  0. atras
                  1. Reportes de las gamas
                  2. Guardar alguna gama
                  3. Actualizar las gamas
                  4. Eliminar una gama
                  5. Cerrar el Programa''')
            try:
                opciones = int(input("Ingrese el numero de la opcion deceada: "))
                if opciones == 0:
                        break
                elif opciones == 1:
                        gama.menu()
                elif opciones == 2:
                        pstGam.menu()
                elif opciones == 3:
                        upGam.updateGama()
                elif opciones ==  4:
                        pstGam.deleteGama()
                elif opciones == 5:
                        exit()
            except ValueError as error:
              input("Oprima enter para continuar con el programa")
              print(error)
              
            except KeyboardInterrupt as error:
              input("Oprima enter para continuar con el programa")
              print(error)          
def menuOficina():
      while True:
            os.system("clear")
            print('''

    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____  / __(_)____(_)___  ____ _                                                  
 / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/                                                  
/ /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ /                                                   
\__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/                                                    
                                                                                                 

                  0.Atras
                  1.Reportes de las gamas
                  2.Guardar alguna gama
                  3.Actualizar una oficina
                  4.Eliminar una oficina
                  5.Cerrar el programa''')
            try:
                opciones = int(input("Ingrese el numero de la opcion deceada: "))
                if opciones == 0:
                        break
                elif opciones == 1:
                        oficina.menu()
                elif opciones == 2:
                        pstOfi.menu()
                elif opciones == 3:
                        upOfi.updateOficina()
                elif opciones == 4:
                        pstOfi.deleteOficina()
                elif opciones == 5:
                        exit()
                        
            except ValueError as error:
              input("Oprima enter para continuar con el programa")
              print(error)
              
            except KeyboardInterrupt as error:
              input("Oprima enter para continuar con el programa")
              print(error)          
def menuPagos():
      while True:
            os.system("clear")
            print('''
 
    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____  ____ _____ _____  _____                                                    
 / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/                                                    
/ /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  )                                                     
\__,_/\___/  / .___/\__,_/\__, /\____/____/                                                      
            /_/          /____/                                                                  

                  0. Atras
                  1.Reportes de los pagos
                  2.Guardas algun pago
                  3.Actualizar algun pago
                  4.Eliminar algun pago
                  5.Cerrar el programa''')
            try:
                opciones = int(input("Ingrese el numero de la opcion deceada: "))
                if opciones == 0:
                        break
                elif opciones == 1:
                        pago.menu()
                elif opciones == 2:
                        pstpag.menu()
                elif opciones == 3:
                        upPa.updatePago()
                elif opciones == 4:
                        pstpag.detelePago()
                elif opciones ==  5:
                        exit()

                        
                            
            except ValueError as error:
                    input("Oprima enter para continuar con el programa")
                    print(error)
                    
            except KeyboardInterrupt as error:
                    input("Oprima enter para continuar con el programa")
                    print(error)          
def menuPedido():
      while True:
            os.system("clear")
            print(''''
                  
   
    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
       __                       ___     __                                                       
  ____/ /__     ____  ___  ____/ (_)___/ /___  _____                                             
 / __  / _ \   / __ \/ _ \/ __  / / __  / __ \/ ___/                                             
/ /_/ /  __/  / /_/ /  __/ /_/ / / /_/ / /_/ (__  )                                              
\__,_/\___/  / .___/\___/\__,_/_/\__,_/\____/____/                                               
            /_/                                                                                  

                  }
                  0. Atras
                  1. Reportes de los pedidos
                  2. Guardar algun pedido
                  3. Actualizar un pedido
                  4. Eliminar Pedido
                  5. Cerrar el programa''')
            try:
                opciones = int(input("Ingrese el numero de la opcion deceada: "))
                if opciones == 0:
                        break
                elif opciones == 1:
                        pedido.menu()
                elif opciones == 2:
                        PstPedi.menu()
                elif opciones == 5:
                        exit()
                elif opciones == 4:
                      PstPedi.menu()
                elif opciones == 3:
                        idEmpleado = input("Ingrese el id del Pedido: ")
                        print(tabulate(upPed.updatePedido(idEmpleado), headers="keys", tablefmt="github"))

            except ValueError as error:
                    input("Oprima enter para continuar con el programa")
                    print(error)
                    
            except KeyboardInterrupt as error:
                    input("Oprima enter para continuar con el programa")
                    print(error)          
def menuProducto():
    while True:
        os.system("clear")
        print('''
       
    ____  _                            _     __                    __   
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___  _____   ____ _/ /   
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \/ ___/  / __ `/ /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ (__  )  / /_/ / /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/____/   \__,_/_/      
  ____/ /__     ____  _________  ____/ /_  _______/ /_____              
 / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \             
/ /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ /             
\__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/              
            /_/                                                         
                       
        0. Atras
        1. Reportes de los productos
        2. Guardar algun producto
        3. Actualizar un producto
        4. Eliminar un producto
        6. Cerrar programa
                        
                        ''')
        try:
                
                opcion = int(input("selecione una de las opciones: "))   
                if(opcion == 1):
                        producto.menu()
                elif(opcion == 2):
                        postpro.postProducto()
                elif(opcion == 0):
                      break
                elif(opcion == 6):
                      exit()
                elif(opcion == 3):
                        print(tabulate(upPro.updateProducto(idProducto), headers="keys", tablefmt="github"))
                        input("Presiona Enter para continuar...")
                elif(opcion == 4):
                        print(tabulate(postpro.deleteProducto(idProducto), headers="keys", tablefmt="github"))
                        input("Precione una tecla para Continuar")
                idProducto = input("Ingrese el id del producto: ")
        

                      
        except ValueError as error:
              input("Oprima enter para continuar con el programa", error)
        except KeyboardInterrupt as error:
              input("Oprima enter para continuar con el programa",error)


if(__name__ == "__main__"):
  # numero = 500
  # peticion = requests.get(f"http://172.16.100.145:5000/productos?cantidad_en_stock_gte={numero}")
  # data = peticion.json()
  # print(tabulate((data), headers="keys", tablefmt="github"))
  # print(json.dumps(data, indent=4))

        

    while True:
        os.system("clear")
        print("""
          
    
     __  ___                               _            _             __   
   /  |/  /__  ____  __  __   ____  _____(_)___  _____(_)___  ____ _/ /   
  / /|_/ / _ \/ __ \/ / / /  / __ \/ ___/ / __ \/ ___/ / __ \/ __ `/ /    
 / /  / /  __/ / / / /_/ /  / /_/ / /  / / / / / /__/ / /_/ / /_/ / /     
/_/  /_/\___/_/ /_/\__,_/  / .___/_/  /_/_/ /_/\___/_/ .___/\__,_/_/      
                          /_/                       /_/                   
                                                                      
                             1. Cliente
                             2. Oficina
                             3. Empleado
                             4. Pedidos
                             5. Pagos
                             6. Producto 
                             7. Cerrar el programa
 """)
        try:
            opcion = int(input("\nselecione una de las opciones: "))   
            if(opcion == 1):
                menuCliente()
            elif(opcion == 2):
                menuOficina()
            elif(opcion == 3):
                menuEmpleado()
            elif(opcion == 4):
                menuPedido()
            elif(opcion == 5):
                menuPagos()
            elif(opcion == 6):
                menuProducto()
            elif(opcion == 7):
                break

        except ValueError as error:
            print(error)
            input("Oprima enter para volver a cargar el programa")
        except KeyboardInterrupt as error:
              print(error)
              input("Oprima alguna tecla para continuar con el programa")
             
        



# # try:
#     entrada = input("Ingresa algo: ")
#     # Aquí puedes hacer lo que necesites con la entrada
#     print("Entrada recibida:", entrada)
# except KeyboardInterrupt:
#     print(tabulate(cliente.getAllClientesName()))
          # with open("storage/producto.json", "r") as f:
          #       fichero = f.read()
          #       data = json.loads(fichero)
          # for i, val in enumerate(data):
          #       data[i]["id"] = (i+1)
          #       data = json.dumps(data, indent=4).encode("utf-8")
          # with open("storage/producto.json", "wb+") as f1:
          #         f1.write(data)
          #         f1.close()
