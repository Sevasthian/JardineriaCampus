import storage.pago as pag
from tabulate import tabulate
from datetime import datetime

def getAll2008():
    PagosPaypal2008 = list()
    for val in pag.pago:
        FechaPagoo = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPagoo, "%d/%m/%Y")
        if (val.get("forma_pago") == "Paypal") and start.day == 2008:
            PagosPaypal2008.append({
              val.get("codigo_cliente"): "codigodecliente",
              val.get("fecha_pago"): "fechadepago"
            }
                                   )
    return PagosPaypal2008

def menu():
    print('''
    ____                        __                   __        __                                          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  ____ _____ _____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ __ `/ __ `/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/\__,_/\__, /\____/____/  
          /_/                                                             /_/          /____/              

          
                            1. Obtiene todos los pagos que se realizaron en el 2008
                            2. Cerrar programa
   ''')
    opcion = int(input("Escriba la opcion que decea: "))
    if (opcion == 1):
        print(tabulate(getAll2008()))
    elif (opcion == 2):
        exit()
    menu()