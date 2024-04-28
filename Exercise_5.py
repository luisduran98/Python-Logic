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

def saludar(name: str)->str:
    """Debe recibir un nombre como argumento

    Args:
        name (_type_): valor del nombre

    Returns:
        str: Devuelve un saludo con el nombre que recibio por argumento
    """
    
    print(f"Hola {name}, me llamo Luis es un placer conocerte")

def brindar():
    print("chin chin..")

def despedir(name: str)-> str:
    """
    Recibe un nombre que sera usado para despedirse

    Args:
        name (str): valor del nombre

    Returns:
        str: Devuelve una despedida con el nombre recibido
    """
    print(f"Chao {name}, Nos vemos pronto")

flag_saludar = 0
flag_brindar = 0

nombre = input("Nombre: ")
while len(nombre) < 3 or nombre.isdigit():
    print("Deberia ser un nombre real")
    nombre = input("nombre:")

while True:

    match menu():
        case "1": 
            saludar(nombre)
            flag_saludar = 1
            
        case "2":
            if not flag_saludar :
                print("Hola deberiamos conocernos antes de brindar no?")
            else:
                flag_brindar = 1
                brindar() 
        case "3":
            if not flag_saludar:
                print("Pero aun no me saludaste...")
            elif not flag_brindar:
                print("No te vayas aun, tenemos que brindar!")
            else:
                despedir(nombre)
                flag_brindar = 0
                flag_saludar = 0
        case "4":
            break

        case _:
            print("debe ser un numero para poder acceder a la opcion")

    pausar()