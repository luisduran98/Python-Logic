
def suma (a,b):
    return int(a + b) 

def resta(a,b):
    return int(a - b)

def division(a,b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir con cero")
    else:
        return int(a/b)

def multiplicar(a,b):
    return a * b

def factorial(n:int)->int:
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n - 1)
    return fact
    
def limpiar():
    from os import system
    system("cls")

def pausar():
    from os import system
    system("pause")

def menu(a,b):
    limpiar()
    print(f"1. Ingresar 1er operando: {a}")
    print(f"2. Ingresar 2do operando: {b}")
    print("3. Operaciones")
    print("4. Mostrar Resultados")
    print("5. Salir")
    return input("Introduce una opcion :")

def operaciones():
    limpiar()
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Factorial")
    print("6. Atras")
    return input("Introduce una opcion :")