import storage.empleado as em
#devulve un listado con el nombre, apellidos y email de los empleados cuyo juefe tiene un codigo de jefe igual a7.

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleados:
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
    for val in em.empleados:
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

