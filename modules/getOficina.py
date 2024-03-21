
from tabulate import tabulate
import requests
import os
#devuelve un listado con el codigo de oficina y al ciudad donde hay oficinas.
def getAllData():
    try:
        peticion =  requests.get("http://154.38.171.54:5005/oficinas")
        data = peticion.json()
        return data
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
def DeleteofinaID(id):
    try:
        peticion = requests.get(f"hhttp://154.38.171.54:5005/oficinas/{id}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
    
def getOficinaCodigo(codigo):
    try:
        peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{codigo}")
        return [peticion.json()] if peticion.ok else []
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []

def getAllCodigCiudad():
    codigoCiudad = []
    for val in getAllData():
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "ciudad" : val.get("ciudad")
        })
    return codigoCiudad

#devuelve un listado con la ciudad y el telefono de las oficnas de españa.

def getAllCiudadTelefono(pais):
    CiudadTelefono = []
    for val in getAllData():
        if(val.get("pais") == pais):
            CiudadTelefono.append({
            "ciudad" : val.get("ciudad"),
            "telefono": val.get("telefono"),
            "oficinas": val.get("codigo_oficina"),
            "pais": val.get("pais")
        })
    return CiudadTelefono

def menu():
    while True:
        os.system("clear")
        print('''
            
        ____                        __                   __              _____      _            
    / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  / __(_)____(_)___  ____ _
    / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ / 
    /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/  
            /_/                                                                                

                0. Atras
                1. Obtener los codigos de la oficina y la ciudad a la q pertenece (codigo_ofina y ciudad)
                2. Obtener los datos del pais que decea buscar (ejem: España)   
                3. Salir del programa
            ''')
        opcio = int(input("Escribe una opcion: "))
        if (opcio == 1):
            print(tabulate(getAllCodigCiudad()))
        elif(opcio == 2):
            pais = input("Escriba el pais que necesita: ")
            print(tabulate(getAllCiudadTelefono(pais)))
        elif(opcio == 3):
            break
        elif(opcio == 0):
            exit()
            
    