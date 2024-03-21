
from tabulate import tabulate
from datetime import datetime
import requests
import os
#json-server storage/pago.json -b 5001
def dataPagos():
    try:
        peticion =  requests.get("http://154.38.171.54:5006/pagos")
        data = peticion.json()
        return data
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def DeletePagosID(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def getPagosCodigo(codigo):
    try:
        peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []

    

#json-server storage/cliente.json -b 5002
def getAllDataClientes():
    try:
        peticion =  requests.get("http://154.38.171.54:5001/cliente")
        data = peticion.json()
        return data
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return [] 
#json-server storage/empleados.json -b 5003
def getAllDataEmpleados():
    try:
        peticion =  requests.get("http://154.38.171.54:5003/empleados")
        data = peticion.json()
        return data
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return [] 

def getAllPagos2008():
    Pagos2008SinRepetir = list()
    PagosRepetidos = set()
    for val in dataPagos():
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            if val.get("codigo_cliente") not in PagosRepetidos:
                Pagos2008SinRepetir.append(val)
                PagosRepetidos.add(val.get("codigo_cliente"))
    return Pagos2008SinRepetir
        
def getAllPaypal2008():
    Paypal2008 = list()
    for val in dataPagos():
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            Paypal2008.append(val)
    return Paypal2008

def getAllFormasDePago():
    FormaPago = list()
    FormaPagoRepetida = set()
    for val in dataPagos():
        if val.get("forma_pago") not in FormaPagoRepetida:
            FormaPago.append({"Formas De Pago:": val.get("forma_pago")})
            FormaPagoRepetida.add(val.get("forma_pago"))
    return FormaPago

def getAllNombreClientesYSuRepresentanteConPago():

    Repetidos = [set()]
    for val in getAllDataClientes():
        for nel in getAllDataEmpleados():
            for fil in dataPagos():
                if(fil.get("codigo_cliente") == val.get("codigo_cliente"))and(val.get("codigo_empleado_rep_ventas") == nel.get("codigo_empleado")):
                    if val.get("nombre_cliente") not in Repetidos:
                        Repetidos.append({
                        "Nombre Cliente": val.get("nombre_cliente"),
                        "Representante de ventas": f'{nel.get("nombre")} {nel.get("apellido1")}'
                    })
                        Repetidos.add(val.get("nombre_cliente"))
    return Repetidos

def getAllNombreClientesYSuRepresentantesSINPago():
    ListoNose = list()
    for val in getAllDataClientes():
        for nel in getAllDataEmpleados():
            for fil in dataPagos():
                if(fil.get("codigo_cliente") != val.get("codigo_cliente"))and(val.get("codigo_empleado_rep_ventas") == nel.get("codigo_empleado")):
                    ListoNose.append({
                        "Nombre Cliente": val.get("nombre_cliente"),
                    "Representante de ventas": f'{nel.get("nombre")} {nel.get("apellido1")}'
                    })
    return ListoNose

def menu():
    while True:
        os.system("clear")
        print('''
    ____                        __                   __        __                                          
    / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  ____ _____ _____  _____
    / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ __ `/ __ `/ __ \/ ___/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ / /_/ / /_/ / /_/ (__  ) 
    /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/\__,_/\__, /\____/____/  
            /_/                                                             /_/          /____/              

            0. Atras
            1. Obtiene todos los pagos que se realizaron en el 2008
            2. Obtiene la lista de pagos realizados por medio de "Paypal".
            3. Obtiene la lista de las formas de pago.  
            4. Obtiene los clientes y su representante de los que tienen pago.
            5. Obtiene los clientes y su representante de los que NO tienen pago.
            6. Cerrar programa
            
    ''')
        try:
            opcion = int(input("Escriba el número de la opcion que decea: "))
            if (opcion == 1):
                print(tabulate(getAllPagos2008()))
                input("Presione Enter para continuar... ")
            elif (opcion == 0):
                break
            elif(opcion == 2):
                print(tabulate(getAllPaypal2008()))
                input("Presione Enter para continuar... ")
            elif(opcion == 3):
                print(tabulate(getAllFormasDePago()))
                input("Presione Enter para continuar... ")
            elif(opcion == 4):
                print(tabulate(getAllNombreClientesYSuRepresentanteConPago()))
                input("Presione Enter para continuar... ")
            elif(opcion == 5):
                print(tabulate(getAllNombreClientesYSuRepresentantesSINPago()))
                input("Presione Enter para continuar... ")
            elif(opcion == 6):
                exit()
        except ValueError as error:
            print(error)
        except KeyboardInterrupt as error:
            print("Oprima enter para continuar con el programa", error)
