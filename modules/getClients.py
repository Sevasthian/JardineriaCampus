from tabulate import tabulate
import requests

#json-server storage/cliente.json -b 1000

def getAllDataClientes():
    try:
        peticion =  requests.post("http://154.38.171.54:5001/cliente")
        peticion.raise_for_status()
        data = peticion.json()
        return data
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return [] 


def getAllClientesName():
    clienteName = list()
    data_clientes = getAllDataClientes()
    for val in data_clientes:
        data_clientes.append = {
            "codigo_cliente": val('codigo_cliente'),
            "nombre_cliente": val()('nombre_cliente')
        }


    return clienteName
    
def getOneClientCodigo(codigo):
    for val in getAllDataClientes():
        if(val.get('codigo_cliente') == codigo):
            return[{ 
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            }]

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in getAllDataClientes():
        if (val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append({
                "Codigo": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f''' {val.get("nombre_contacto")}{val.get("apellido_contacto")}''',
                "Telefono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Direcciones": f'''{val.get("linea_direccion1")}{val.get("linea_direccion2")}''',
                "Origen": f'''{val.get("ciudad")}{val.get("region")}{val.get("pais")}{val.get("codigo_postal")} ''',
                "Codigo del asesor": val.get("codigo_empleado_rep_ventas"),
                "Credito": val.get("limite_credito")
            })
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None , ciudad=None):
    clientZone = list()
    for val in getAllDataClientes():
        if(
        val.get('pais') == pais and 
        (val.get('region') == region or val.get('region') == None) or
        (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone


def getAllClientsMismoFax(Fax):
    ClientFax = list()
    for val in getAllDataClientes():
        if (val.get("fax") == Fax):
            ClientFax.append(val)
    return ClientFax

def getAllClientsMismoCodigo_empleado_rep_ventas(Codigo):
    CodigoEmpleado = list()
    for val in getAllDataClientes():
        if val.get("codigo_empleado_rep_ventas") == Codigo:
            CodigoEmpleado.append(val)
    return CodigoEmpleado

def getAllClientsNombrePostal():
    NombreYPostal = list()
    for val in getAllDataClientes():
        datos = dict({"Nombre_Cliente": val.get("nombre_cliente"), "Codigo_Postal": val.get("codigo_postal")})
        NombreYPostal.append(datos)
    return NombreYPostal

def getAllClientsLineaDirecciones():
    direcciones = list()
    for val in getAllDataClientes():
        direccion1y2 = dict({"Nombre":val.get("nombre_cliente"), "Direccion_1":val.get("linea_direccion1"),"Direccion_2":val.get("linea_direccion2")})
        direcciones.append(direccion1y2)
    return direcciones

def getAllclientsApellidoContacto(apellido):
    apellidos = list()
    for val in getAllDataClientes():
        if (val.get("apellido_contacto") == apellido):
            apellidos.append(val)
    return apellidos

def getAllNombresSpain():
    nombresEspaña = list()
    for val in getAllDataClientes():
        if val.get("pais") == "Spain":
            nombresEspaña.append({"nombre":val.get("nombre_cliente"),
                                  "Pais":val.get("pais")})
    return nombresEspaña

def menu():
    while True:
        print('''
          
    ____                        __              __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                              

            1. Obtener todos los clientes (codigo y nombre)
            2. Obtener un cliente por el codigo (codigo y nombre)
            3. Obtener toda la indormacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 1500.0 , Fuenlabrada)
            4. Obtiene un reporte del los quientes que esten en el mismo pais region o ciudad (ejem: USA, None, New York)
            5. Obtiene caracteristicas del cliente de acuerdo al tipo de fax (ejem: '5552323128')
            6. Obtiene caracteristicas del cliente con el mismo codigo de empreado de ventas (ejem: 19)
            7. Obtiene todos los clientes con su nombre y su codigo postal.
            8. Obtiene las direcciones con los clientes.
            9. Obtiene todos los datos apartir de apellido del cliente (ejem: Wright)
            10.Obtiene todos los nombres de los clientes que esten en españa
            11.Cerrar el programa
            
          
           ''')
        opcion = int(input("selecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllClientesName(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            codigo = int(input("Dame el codigo del cliente: "))
            print(tabulate(getOneClientCodigo(codigo), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            limiteDeCredito = float(input("Escribe un limite de credito: "))
            ciudad = input("Escriba una ciudad que corresponda con ese credito: ")
            data = getAllClientCreditCiudad(limiteDeCredito,ciudad)
            print(tabulate(data ,headers = "Head", tablefmt ="gird"))
        elif(opcion == 4):
            pais = input("Escriba el pais: ")
            Region = input("Escriba la region: ")
            Ciudad = input("Escriba la ciudad: ")
            print(tabulate(getAllClientPaisRegionCiudad(pais, Region, Ciudad),headers = 'firstrow', tablefmt = 'gird'))
        elif(opcion == 5):
            fax = input("Escriba el codigo fax: ")
            print(tabulate(getAllClientsMismoFax(fax)))
        elif(opcion == 6):
            codigo = int(input("Escriba el codigo de un empleado de ventas: "))
            print(tabulate(getAllClientsMismoCodigo_empleado_rep_ventas(codigo)))
        elif(opcion == 7):
            print(tabulate(getAllClientsNombrePostal()))
        elif(opcion == 8):
            print(tabulate(getAllClientsLineaDirecciones()))
        elif(opcion == 9):
            apellido = input("Escriba el apellido del cliente: ")
            print(tabulate(getAllclientsApellidoContacto(apellido)))
        elif(opcion == 10):
            print(tabulate(getAllNombresSpain()))
        elif(opcion == 11):
            exit()
        elif(opcion == 12):
            break
        
        

 