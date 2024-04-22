# -------------------------------------2--------------------------------------------------------

# Crear diferentes funciones que cumplan con las siguientes consignas:
# 1- Dividir dos números enteros. *
# 2- Calcular el cubo y el cuadrado de un numero entero.*
# 3- Un conversor que reciba un valor en Celsius y lo convierta a Fahrenheit.*
# 4- Tomar un numero entero y devolver su tabla de multiplicación.*
# 5- Un validador de contraseñas, si la contraseña introducida es valida devuelve True, caso
# contrario devuelve False.
# 6- Una función que tome nombre, apellido, edad, DNI y numero de teléfono de una
# persona y lo muestre por terminal. Validar que la edad sea mayor a 16, que el DNI tenga 8
# dígitos y que el numero de teléfono contenga solo números.

# Exercise 1:
def division(a,b):
    if isinstance(a, str) or isinstance(b, str):
        return "It is not an integer"
    if int(a) != a or int(b) != b:
        return "It is not an integer"
    else:
        resultado = int(a/b)
        return resultado
    
# Exercise 2:
def exponent(element):
    if isinstance(element, str):
        return "It is not an integer"
    if int(element) != element:
        return "It is not an integer"
    else:
        cuadrado = element*element
        cubo = element*element*element
        return f"cuadrado: {cuadrado}, cubo: {cubo}"
    
# Exercise 3:
def Fahrenheit(Celsius):
    result = (Celsius * 9/5) + 32
    return result

# Exercise 4:
def whole(number):
    if not isinstance(number, int):
        return "It is not an integer"
    else:
        for i in range(11):
            return number*i

# Exercise 5:
def validator(element):
    password = "Chocolate"
    if element == password:
        return True
    else:
        return False

# Exercise 6
def validador_2(name, lastname, age, dni, phonenumber):
    if age <= 16:
        return "must be over 16 years old"
    elif len(dni) != 8:
        return "The dni must contain 8 digits"
    elif isinstance(phonenumber, int):
        return f"name: {name}, last name: {lastname}, age: {age}, dni: {dni}, phone number: {phonenumber}"
    else:
        return "check that the data is correct"
