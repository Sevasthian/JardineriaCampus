from tabulate import tabulate 
import os
import modules.postEmpleado as PstEmp
def postEmpleado():
    print()

def menu():
    while True:
        os.system("clear")
        print('''
          

    ___       __          _       _      __                         __      __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/ 
                          ____  _________  ____/ /_  _______/ /_____  _____                            
                         / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                            
                        / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                             
                       / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                              
                      /_/                                                                              

            0. Atras
            1. Guardar un producto nuevo
            2. Cerrar programa
           ''')
        
        opcio = int(input("Escribe una opcion: "))
        if (opcio == 0):
            break
        elif(opcio == 1):
            print(tabulate(postEmpleado()))
            input("Precione una tecla para continuar...")
        elif(opcio == 2):
            exit()