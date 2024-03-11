import storage.oficina as of
from tabulate import tabulate
#devuelve un listado con el codigo de oficina y al ciudad donde hay oficinas.

def getAllCodigCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "ciudad" : val.get("ciudad")
        })
    return codigoCiudad

#devuelve un listado con la ciudad y el telefono de las oficnas de españa.

def getAllCiudadTelefono(pais):
    CiudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
            CiudadTelefono.append({
            "ciudad" : val.get("ciudad"),
            "telefono": val.get("telefono"),
            "oficinas": val.get("codigo_oficina"),
            "pais": val.get("pais")
        })
    return CiudadTelefono

def menu():
    print('''
          
    ____                        __                   __              _____      _            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  / __(_)____(_)___  ____ _
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ / 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/  
          /_/                                                                                

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
        exit()
    menu ()