from tkinter.messagebox import showinfo as alert

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

def suma (a,b):
    return int(a + b) 

def resta(a,b):
    return int(a - b)

def division(a,b):
    try:
         print(int(a/b))
    except:
        alert("Error","No se puede dividir por cero")
    


# a = input("Ingresar 1er operando: ")
# while not a.isdigit():
#     a = input("Ingresar 1er operando: ")

# b = input("Ingresar 2do operando: ")
# while not b.isdigit():
#     b = input("Ingresar 2do operando: ")

 