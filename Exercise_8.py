def duplicar(valor):
    return valor * 2

numero = duplicar(20)
print(numero)

# ------------------------------

numero = 20 
print(numero)


def duplicar(valor):
    valor = valor * 2
    return valor
    

print(duplicar(numero))
print(numero)

# -------------------------------

def duplicar_lista(valores):
    for i in range(len(valores)):
        valores[i] = valores[i] * 2


lista = [3, 5, 6, 8, 3]
print(lista)

duplicar_lista(lista)

print(lista)

# --------------------------------

def factorial(n:int)->int:
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n - 1)
    return fact


# -------------------------



