import requests
from tabulate import tabulate
#devulve un listado con el nombre, apellidos y email de los empleados cuyo juefe tiene un codigo de jefe igual a7.
def getAllNombre():
    peticion = requests.get("")
    data = peticion.json()
    return data

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in getAllNombre():
        if (val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellidos":f'''{val.get("apellido1")}{val.get("apellido2")}''',
                    "email":val.get("email"),
                    "jefe":val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

#devuleve el nombre del puesto, nombre apellidos y email del jefe de la empresa

def getAllNombreDelPuestoApellidosEmailJefe():
    nombrePuestoApellidoEmail = []
    for val in getAllNombre():
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
    for val in getAllNombre():
        if val.get("puesto") != "Representante Ventas":
            InfoNoRepVentas.append({
                "Puesto":val.get("puesto"),
                "Nombre":val.get("nombre"),
                "Apellido": val.get("apellido1"),
            })
    return InfoNoRepVentas

def menu():
    print(
        '''
    ____                        __                   __        __                                   __               __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                                            /_/                                     
             
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
    elif (opcion == 2):
        print(tabulate(getAllNombreDelPuestoApellidosEmailJefe()))
    elif (opcion == 3):
        print(tabulate(getAllNombreApellidosPuestoNoRepVentas()))
    elif(opcion == 4):
        exit()
    menu()