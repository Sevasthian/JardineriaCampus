import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
from tabulate import tabulate
 

 

print(tabulate(pedido.getAllPedidosRechazadosEn2009()))
