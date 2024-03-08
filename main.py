import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPagos as pago
# from tabulate import tabulate


# def menu():
#     print('''
# Menu principal
#           1. cliente
#           2. oficina
#           3. empleado
#           4. pedidos
#           ''')
# print(dir())
import sys

# # # print(pedido. getAllPedidosEntregadosEnero())
# def menu():
#     contador = 1
#     print("Menu principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modulo"):
#             modulo = getattr(objeto, "__name__", None)
#         if(modulo != "modulo"):
#             file = modulo.split("get")[- 1]
#             print(f'''{contador}.{file}''')
#             contador += 1
if(__name__ == "__main__"):
  
    print("""
          
                                                                                                                                                     
          ____                                            ,-.----.                                                                                   
        ,'  , `.                                          \    /  \                                                                          ,--,    
     ,-+-,.' _ |                                          |   :    \            ,--,                           ,--,   ,-.----.             ,--.'|    
  ,-+-. ;   , ||              ,---,          ,--,         |   |  .\ :  __  ,-.,--.'|         ,---,           ,--.'|   \    /  \            |  | :    
 ,--.'|'   |  ;|          ,-+-. /  |       ,'_ /|         .   :  |: |,' ,'/ /||  |,      ,-+-. /  |          |  |,    |   :    |           :  : '    
|   |  ,', |  ':  ,---.  ,--.'|'   |  .--. |  | :         |   |   \ :'  | |' |`--'_     ,--.'|'   |   ,---.  `--'_    |   | .\ :  ,--.--.  |  ' |    
|   | /  | |  || /     \|   |  ,"' |,'_ /| :  . |         |   : .   /|  |   ,',' ,'|   |   |  ,"' |  /     \ ,' ,'|   .   : |: | /       \ '  | |    
'   | :  | :  |,/    /  |   | /  | ||  ' | |  . .         ;   | |`-' '  :  /  '  | |   |   | /  | | /    / ' '  | |   |   |  \ :.--.  .-. ||  | :    
;   . |  ; |--'.    ' / |   | |  | ||  | ' |  | |         |   | ;    |  | '   |  | :   |   | |  | |.    ' /  |  | :   |   : .  | \__\/: . .'  : |__  
|   : |  | ,   '   ;   /|   | |  |/ :  | : ;  ; |         :   ' |    ;  : |   '  : |__ |   | |  |/ '   ; :__ '  : |__ :     |`-' ," .--.; ||  | '.'| 
|   : '  |/    '   |  / |   | |--'  '  :  `--'   \        :   : :    |  , ;   |  | '.'||   | |--'  '   | '.'||  | '.'|:   : :   /  /  ,.  |;  :    ; 
;   | |`-'     |   :    |   |/      :  ,      .-./        |   | :     ---'    ;  :    ;|   |/      |   :    :;  :    ;|   | :  ;  :   .'   \  ,   /  
|   ;/          \   \  /'---'        `--`----'            `---'.|             |  ,   / '---'        \   \  / |  ,   / `---'.|  |  ,     .-./---`-'   
'---'            `----'                                     `---`              ---`-'                `----'   ---`-'    `---`   `--`---'             
                                                                                                                                                     
                                                  1. Cliente
                                                  2. Oficina
                                                  3. Empleado
                                                  4. Pedidos
""")

opcion = int(input("selecione una de las opciones: "))
if(opcion == 1):
    cliente.menu()
elif(opcion == 2):
    oficina.menu()
elif(opcion == 3):
    empleado.menu()
elif(opcion == 4):
    pedido.menu()
  
