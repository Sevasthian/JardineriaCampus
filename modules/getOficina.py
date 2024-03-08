import storage.oficina as of
#devuelve un listado co nel codigo de oficina y al ciudad donde hay oficinas.

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
#devuelve  un listado con el nombre, apellidos
def menu():
    print('''
          reportes la oficina
            1. Obtener los codigos de la oficina y la ciudad a la q pertenece (codigo_ofina y ciudad)
            2. Obtener un pais  (codigo y nombre)        
           ''')
menu ()