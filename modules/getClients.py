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
            clienteCredic.append(val)
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

import storage.empleado as emp

def getAllEmpleados ():
    empleadosName = list()
    for val in emp.empleados:
        empleadosName = dict({
            "codigo_empleado": val.get('nombre_empleado'),
            "puesto": val.get('nombre_empleado')
        })
        empleadosName.append(codigoName)