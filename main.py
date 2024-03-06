import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
from tabulate import tabulate
 

 

print(tabulate(empleado.getAllNombreDelPuestoApellidosEmailJefe()))
