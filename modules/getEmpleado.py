import requests
from tabulate import tabulate
import os
#devulve un listado con el nombre, apellidos y email de los empleados cuyo juefe tiene un codigo de jefe igual a7.
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
def DeleteEmpleadosID(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def getEmpleadosCodigo(codigo):
    try:
        peticion = requests.get(f"http://154.38.171.54:5003/empleados/{codigo}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def getAllNombreApellidoEmailJefe(puesto):
        try:
            puesto = input("Digite el puesto del empleado que decea buscar: ")
            peticion =  requests.post(f"http://154.38.171.54:5003/empleados?{puesto}puesto")
            data = peticion.json()
            return data
        except requests.RequestException as e:
            print("Error en la solicitud HTTP:", e)
            return []
        except ValueError as e:
            print("Error al cargar JSON:", e)
            return [] 
   

#devuleve el nombre del puesto, nombre apellidos y email del jefe de la empresa

def getAllNombreDelPuestoApellidosEmailJefe():
    nombrePuestoApellidoEmail = []
    for val in getAllDataEmpleados():
        if (val.get("codigo_jefe")) == None:
            nombrePuestoApellidoEmail.append(
            {
                "puesto":val.get("puesto"),
                "nombre" : val.get("nombre"),
                "apellidos" : f'''{val.get("apellido1")}{val.get("apellido2")}''',
                "emailDelJefe": val.get( "email")
            }
        )
    return nombrePuestoApellidoEmail

def getAllNombreApellidosPuestoNoRepVentas():
    InfoNoRepVentas = list()
    for val in getAllDataEmpleados():
        if val.get("puesto") != "Representante Ventas":
            InfoNoRepVentas.append({
                "Puesto":val.get("puesto"),
                "Nombre":val.get("nombre"),
                "Apellido": val.get("apellido1"),
            })
    return InfoNoRepVentas

def menu():
    while True:
        os.system("clear")
        print(
            '''
        ____                        __                   __        __                                   __               __          
    / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
    / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
    /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
            /_/                                                                            /_/                                     
                    0. Atras
                    1. Obtiene un listado de caracteristicas del empleado (ejem: 7)
                    2. Obtiene los datos del jefe de la empresa
                    3. Obtiene un listado de las personas que no tiene un puesto de representante de ventas
                    4. Cerrar el programa
    '''
        )
        opcion = int(input("Escriba la opcion que decea: "))
        if (opcion == 1):
            codigo = int(input("Escriba el codigo del empleado que necesita: "))
            print(tabulate(getAllNombreApellidoEmailJefe(codigo)))
            input("Presione una tecla para continuar...")
        elif (opcion == 2):
            print(tabulate(getAllNombreDelPuestoApellidosEmailJefe()))
            input("Presione una tecla para continuar...")
        elif (opcion == 3):
            print(tabulate(getAllNombreApellidosPuestoNoRepVentas()))
            input("Presione una tecla para continuar...")
        elif(opcion == 4):
            exit()
        elif(opcion == 0):
            break