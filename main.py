import modules.getClients as cliente
 
from tabulate import tabulate
 

 

print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain","Fuenlabrada", "Madrid")))
