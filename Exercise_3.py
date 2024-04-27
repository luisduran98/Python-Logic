from math import pi

# --------------------{ DOCSTRING }----------------------------------------

def suma(a: int, b: int)-> int:
    """sumatoria de los dos parametros (a + b)

    Args:
        a (int): primer valor entero
        b (int): segundo valor entero

    Returns:
        int: resultado de la suma de (a + b)
    """
    return a + b

a = int(input("Coloca un numero: "))
b = int(input("Coloca otro numero: "))

print(suma(a,b))

# -------------------------------------------------------------

def suma()-> int:
    """ Debes escribir por consola dos numeros enteros 

    Returns:
        int: devuelve la sumatoria de los numeros solicitados
    """
    a = int(input("Coloca un numero: "))
    b = int(input("Coloca otro numero: "))

    return a + b

print(suma())

# --------------------------------------------------------------

def suma()-> None:
    """Debes escribir por consola dos numeros enteros 

    Args:
        a (int): primer valor entero
        b (int): segundo valor entero
    """
    a = int(input("Coloca un numero: "))
    b = int(input("Coloca otro numero: "))
    print(a + b)

suma()

# -----------------------------------------------------------

def calcular_perimetro_circunferencia(radio: float)-> float:
    """ De acuerdo al parametro calcula el perimetro de una circunferencia 

    Args:
        radio (int): valor que pertenece al radio

    Returns:
        int: devuelve el perimetro
    """
    return 2 * pi * radio

# ----------------------------------------------------

def calcular_perimetro_rectangulo(base: float, altura: float)-> float:
    """De acuerdo a los parametros calcula el perimetro de un rectangulo 

    Args:
        base (float): valor de la base
        altura (float): valor de la altura

    Returns:
        float: devuelve el perimetro
    """
    return base * 2 + altura * 2

# ------------------------------------------------------

def calcular_superficie_rectagulo (base: int, altura:int)-> int:
    """calcula la superficie de un rectangulo

    Args:
        base (int): valor base
        altura (int): valor altura

    Returns:
        int: devuelve la superficie del rectanfulo 
    """
    return base * altura

# -------------------------------------------------------

# def calcular_superficie_circunferencia ():
#     pass

# -------------------------------------------------------

def calcular_superficie_cuadrado(lado:int)-> int:
    """calcula la superfice de un cuadrado

    Args:
        lado (int): valor del lado

    Returns:
        int: devuelve el valor de la superficie del cuadrado
    """
    return calcular_superficie_rectagulo(lado,lado)

# --------------------------------------------------------

def validar_rango_200_500(numero:int)->bool:
    """ valida que el numero este entre 200 y 500

    Args:
        numero (int): valor del numero

    Returns:
        bool: devuelve un booleano
    """
    if numero >= 200 and numero <= 500:
        return True
    else:
        return False

# ---------------------------------------------------------

def validar_fuera_rango(num:int, min:int, max:int)->bool:
    """ valida si el num esta fuera del rango de min y max

    Args:
        num (int): valor del numero
        min (int): valor del numero menor
        max (int): valor del numero maximo

    Returns:
        bool: devuelve True si esta fuera de rango y si no False
    """
    return not(num >= min and num <= max)

print(validar_fuera_rango(5,100,500))


# ---------------------------------------------------------

def calcular_resto(dividendo:int, divisor:int)-> int:
    """busca el cociente de la division

    Args:
        dividendo (int): valor dividendo
        divisor (int): valor divisor

    Returns:
        int: devuele el cociente de la division
    """
    return dividendo - divisor * (dividendo // divisor)


print(calcular_resto(2,2))

# -------------------------------------------------------------

def es_multiplo(a:int, b:int)->bool:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        bool: _description_
    """
    return a % b == 0

print(es_multiplo(2,3))