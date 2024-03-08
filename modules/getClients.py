from tabulate import tabulate
import storage.cliente as cli

def getAllClientesName():
    clienteName = list()
    for val in cli.clientes:
        codigoName = dict({
            "codigo_cliente": val.get('nombre_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)

    return clienteName
    
def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return{ 
            "codigo_cliente": val.get('nombre_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            }

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append({
                "Codigo": val.get("codigo_cliente")
                "Responsable":val.get("nombre_cliente")
                "Director":f''' {val.get("nombre_contacto")}{val.get("apellido_contacto")}
                "Telefono":
                "Fax":
                "Direcciones":
                "Origen":
                "Codigo del asesor":
                "Credito":





            })
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None , ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if(
        val.get('pais') == pais and 
        (val.get('region') == region or val.get('region') == None) or
        (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone


def getAllClientsMismoFax(Fax):
    ClientFax = list()
    for val in cli.clientes:
        if (val.get("fax") == Fax):
            ClientFax.append(val)
    return ClientFax

def getAllClientsMismoCodigo_empleado_rep_ventas(Codigo):
    CodigoEmpleado = list()
    for val in cli.clientes:
        if val.get("codigo_empleado_rep_ventas") == Codigo:
            CodigoEmpleado.append(val)
    return CodigoEmpleado

def getAllClientsNombrePostal():
    NombreYPostal = list()
    for val in cli.clientes:
        datos = dict({"Nombre_Cliente": val.get("nombre_cliente"), "Codigo_Postal": val.get("codigo_postal")})
        NombreYPostal.append(datos)
    return NombreYPostal

def getAllClientsLineaDirecciones():
    direcciones = list()
    for val in cli.clientes:
        direccion1y2 = dict({"Nombre":val.get("nombre_cliente"), "Direccion_1":val.get("linea_direccion1"),"Direccion_2":val.get("linea_direccion2")})
        direcciones.append(direccion1y2)
    return direcciones

def getAllclientsApellidoContacto(apellido):
    apellidos = list()
    for val in cli.clientes:
        if (val.get("apellido_contacto") == apellido):
            apellidos.append(val)
    return apellidos

#punto 7
def getAllNombresSpain():
    nombresEspaña = list()
    for val in cli.clientes:
        if val.get("pais") == "Spain":
            nombresEspaña.append({"nombre":val.get("nombre_cliente"),
                                  "Pais":val.get("pais")})
    return nombresEspaña
def menu():
    print('''
          reportes de los clientes
            1. Obtener todos los clientes (codigo y nombre)
            2. Obtener un cliente por el codigo (codigo y nombre)
            3. Obtener toda la indormacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0 , San Francisco)
          
           ''')
opcion = int(input("selecione una de las opciones: "))
if(opcion == 1):
    print(tabulate(getAllClientesName(), headers="keys", tablefmt="github"))
elif(opcion == 2):
    
    print(tabulate(getAllClientesName(), headers="keys", tablefmt="github"))
elif(opcion == 2):
 
menu ()