from os import system

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")

def menu()->str:
    limpiar_pantalla()
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")

    return input("Ingrese opcion: ")

def saludar():
    print("Hola como estas")

def brindar():
    print("chin chin..")

def despedir():
    print("Chao, Nos vemos pronto")

flag_saludar = 0
flag_brindar = 0


while True:

    match menu():
        case "1": 
            saludar()
            flag_saludar = 1
            
        case "2":
            if not flag_saludar :
                print("Hola deberiamos conocernos antes de brindar no?")
            else:
                brindar() 
                flag_brindar = 1
                
        case "3":
            if not flag_saludar:
                print("Pero aun no me saludaste...")
            elif not flag_brindar:
                print("No te vayas aun, tenemos que brindar!")
            else:
                despedir()
                flag_brindar = 0
                flag_saludar = 0
        case "4":
            break

        case _:
            print("debe ser un numero para poder acceder a la opcion")

    pausar()





        
    
  