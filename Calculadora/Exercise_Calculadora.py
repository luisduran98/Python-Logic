from funciones_matematicas.matematica import *

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

flag_primer_operando = False
flag_segundo_operando = False
resultado = 0
parametro_uno = None
parametro_dos = None

while True: 
    match menu(parametro_uno,parametro_dos):

        case "1":
            caso_uno = input("Coloca tu primer numero: ")
            while not caso_uno.isdigit():
                limpiar()
                print("Debe ser un numero natural")
                caso_uno = input("Intenta de nuevo: ")
    
            flag_primer_operando = True
            primer_operando = int(caso_uno)
            parametro_uno = caso_uno
           
        case "2":
            if flag_primer_operando:
                caso_dos = input("Coloca tu segundo numero: ")
                while not caso_dos.isdigit():
                    limpiar()
                    print("Debe ser un numero natural")
                    caso_dos = input("Intenta de nuevo: ")
    
                flag_segundo_operando = True
                segundo_operando = int(caso_dos)
                parametro_dos = caso_dos
            else:
                limpiar()
                print("Deberias colocar el primer operando")
                pausar()
        
        case "3":
                while True:
                     match operaciones():
                          case "1":
                                if flag_primer_operando and flag_segundo_operando:
                                    resultado = suma(primer_operando, segundo_operando)
                                    break
                                if flag_primer_operando and not flag_segundo_operando:
                                    limpiar()
                                    print("Para poder sumar te hace falta el segundo operador")
                                    pausar()
                                    break 
                                else: 
                                    limpiar()
                                    print("Para poder sumar te faltan los dos operadores")
                                    pausar()
                                    break
                          case "2":
                                if flag_primer_operando and flag_segundo_operando:
                                    resultado = resta(primer_operando, segundo_operando)
                                    break
                                if flag_primer_operando and not flag_segundo_operando:
                                    limpiar()
                                    print("Para poder restar te hace falta el segundo operador")
                                    pausar()
                                    break 
                                else: 
                                    limpiar()
                                    print("Para poder restar te faltan los dos operadores")
                                    pausar()
                                    break
                          case "3":
                                if flag_primer_operando and flag_segundo_operando:
                                    try:
                                        resultado = division(primer_operando, segundo_operando)
                                        break
                                    except ZeroDivisionError as error:
                                        limpiar()
                                        print(error)
                                        pausar()                                       
                                        break
                                if flag_primer_operando and not flag_segundo_operando:
                                    limpiar()
                                    print("Para poder dividir te hace falta el segundo operador")
                                    pausar()
                                    break 
                                else: 
                                    limpiar()
                                    print("Para poder dividir te faltan los dos operadores")
                                    pausar()
                                    break
                          case "4":
                                if flag_primer_operando and flag_segundo_operando:
                                    resultado = multiplicar(primer_operando, segundo_operando)
                                    break
                                if flag_primer_operando and not flag_segundo_operando:
                                    limpiar()
                                    print("Para poder multiplicar te hace falta el segundo operador")
                                    pausar()
                                    break 
                                else: 
                                    limpiar()
                                    print("Para poder multiplicar te faltan los dos operadores")
                                    pausar()
                                    break
                          case "5":
                                if flag_primer_operando and flag_segundo_operando:
                                    valor_factorial_uno = factorial(primer_operando)
                                    valor_factorial_dos = factorial(segundo_operando)
                                    break
                                if flag_primer_operando and not flag_segundo_operando:
                                    limpiar()
                                    print("Necesitas el segundo operador para saber cual es el factorial")
                                    pausar()
                                    break 
                                else: 
                                    limpiar()
                                    print("Te faltan los dos operadores")
                                    pausar()
                                    break
                          case "6":
                                break
        case "4":
            if flag_primer_operando and flag_segundo_operando:
                if resultado:
                    limpiar()
                    print(resultado)
                    pausar()
                    continue
                if valor_factorial_dos and valor_factorial_uno:
                    limpiar()
                    print(f"El Valor de A = {valor_factorial_uno} y el valor de B = {valor_factorial_dos} ")
                    pausar()
                    continue
                else:
                    limpiar()
                    print("Necesitas seleccionar alguna operacion para poder mostrar los resultados")
                    pausar()
            if flag_primer_operando and not flag_segundo_operando:
                limpiar()
                print("Para poder avanzar te hace falta el segundo operador y seleccionar una operacion")
                pausar()
            else: 
                limpiar()
                print("te faltan los dos operadores y seleccionar una operacion")
                pausar()
        case "5":
            break