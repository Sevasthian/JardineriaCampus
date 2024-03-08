import storage.pedido as ped

def getAllEstadosPedido():
    pedidoEstado = []
    for val in ped.pedido:
        pedidoEstado.append({
            "codigo_pedido": val.get('codigo_pedido'),
            "estado": val.get('estado')
        })
    return pedidoEstado

#Devuelve un listado con el código de pedido, código de cliente, fecha esperada y fecha de entrega de los pedidos que no han sido entregados a tiempo.
from datetime import datetime
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") == None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                })
    return pedidosEntregado

            # pedidosEntregado.append(val)
            # if(val.get("fecha_entrega") == None):
            #     val["fecha_entrega"] = val.get("fecha_esperada")
            #     pedidosEntregado.append(val)
            # else:
            #     pedidosEntregado.append(val)

# date_1  = '2008-11-14'
# date_2 = '2008-11-14'
# Debuelve un listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos cuya fecha de entrega hga sido al menos dos dias antes de la fecha esperada.

def getAllPedidosClienteFechaEsperadaFechaEntrega():
    pedidosEntregado = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") == None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days >= 2):
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                })
    return pedidosEntregado

#Devuelve un listado de todos los pedidos que fueron rechazados en 2009
def getAllPedidosRechazados2009():
    rechazados2009 = []
    for val in ped.pedido:
        FechaPedido = "/".join(val.get("fecha_pedido").split("-")[::-1])
        start = datetime.strptime(FechaPedido, "%d/%m/%Y")
        if val.get("estado") == "Rechazado" and start.year == 2009:
            rechazados2009.append(val)
    return rechazados2009

def getAllPedidosEntregadosEnero():
    EntregadosEnero = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                EntregadosEnero.append(val)
    return EntregadosEnero