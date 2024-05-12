from os import system



def suma (a,b):
    return int(a + b) 
    

def menu():
    system("cls")
    print("1. Ingresar 1er operando: ")
    print("2. Ingresar 2do operando: ")
    print("3. Sumar")
    print("4. Restar")
    print("5. Dividir")
    print("6. Multiplicar")
    print("7. Factorial")
    print("8. Salir")
    return input("Introduce una opcion :")

flag_primer_operando = False
flag_segundo_operando = False

while True:
    match menu():

        case "1":
            caso_uno = input("Coloca tu primer numero: ")
            while not caso_uno.isdigit():
                system("cls")
                print("Debe ser un numero natural")
                caso_uno = input("Intenta de nuevo: ")
    
            flag_primer_operando = True
            primer_operando = int(caso_uno)
           
        case "2":
            if flag_primer_operando:
                caso_dos = input("Coloca tu segundo numero: ")
                while not caso_dos.isdigit():
                    system("cls")
                    print("Debe ser un numero natural")
                    caso_dos = input("Intenta de nuevo: ")
    
                flag_segundo_operando = True
                segundo_operando = int(caso_dos)
            else:
                system("cls")
                print("Deberias colocar el primer operando")
                system("pause")
        
        case "3":
            if flag_primer_operando and flag_primer_operando:
                valor_suma = suma(primer_operando, segundo_operando)
            # if not flag_primer_operando:


        # case "4":

        # case "5":

        # case "6":

        # case "7":

        # case "8":


# def resta(a,b):
#     return int(a - b)

# def division(a,b):
#     try:
#          print(int(a/b))
#     except:
#         alert("Error","No se puede dividir por cero")



# Calculadora / video hora = 1:00:00

# Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
# 1. Ingresar 1er operando (A=x) ***

# 2. Ingresar 2do operando (B=y) *** 

# 3. Calcular todas las operaciones
# a) Calcular la suma (A+B)
# b) Calcular la resta (A-B)
# c) Calcular la división(A/B)
# d) Calcular la multiplicación(A*B)
# e) Calcular factorial(A!)

# 4. Informar resultados
# a) “El resultado de A+B es: r”
# b) “El resultado de A-B es: r”
# c) “El resultado de A/B es: r” o “No es posible dividir por cero”
# d) “El resultado de A*B es: r”
# e) “El factorial de A es: r1 y El factorial de B es: r2”

# 5. Salir

# • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
# para realizar las cinco operaciones.

# • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
# se debe mostrar el número cargado)

# • Deberán contemplarse los casos de error (división por cero, etc.)

# • Documentar todas las funciones