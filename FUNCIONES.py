def mapear_lista_nombre_sector(lista:list)->list:
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["nombre"], emp["sector"]))
    return lista_retorno

def mostar_lista_tuplas(lista:list)->None:
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"{lista[i][j]:5}", end="")
        print()   

def for_each_lista(funcion, lista)->None:
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])

def mapear_lista(funcion, lista:list)->list:
    lista_mapeada = []
    for el in lista:
        lista_mapeada.append(funcion(el))
    return lista_mapeada

def filtrar_lista(funcion, lista:list)->list:
    lista_filtrada = []
    for el in lista:
        if funcion(el):
            lista_filtrada.append(el)
    return lista_filtrada

def reducer_lista(funcion, lista:list, valor_inicial=None ):
    if valor_inicial != None:
        ant = valor_inicial
        indice = 0

    else:
        ant = lista[0]
        indice = 1
    for act in lista[indice]:
        ant = funcion(ant,act)
    return ant

def obtener_path(nombre:str):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual,nombre)

def ordenar_lista(comparador, lista:list)->None:
    tam = len(lista)
    for i in range(tam -1):
        for j in range (i + 1, tam):
            if comparador(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def obtener_mayor(lista:list)->int:
     mayor = 0
     for num in lista:
         if num > mayor:
             mayor = num
     return mayor

def obtener_menor(lista:list)->int:
     menor = lista[0]
     for i in range(1,len(lista)):
         if menor > lista[i]:
             menor = lista[i]
     return menor

def sumar_lista(lista:list)->int:
    suma = 0
    for num in lista:
        suma += num 
    return suma

def promedio_lista(lista:list)->float:
    if len(lista) != 0:
        suma = sumar_lista(lista)
        return suma / len(lista)
    else:
        return 0
    
def limpiar():
    from os import system
    system("cls")

def pausar():
    from os import system
    system("pause")



# print(reducer_lista(lambda a,b : ,prueba))

# *METODOS
# metodo items() : te devuelve los cada elemento del diccionario en fromato tupla
# metodo type() : te devuelvo el tipo de valor que representa
# metodo capitalize() : tranforma la primera poscicion en mayuscula
# metodo upper(): tranforma todo a mayuscula


# importaciones
# from time import sleep ////  sleep() : detiene el programa durante el tiempo que quieras
# from random import randint as random


# Operador Ternario

# x if x > y else y

# Print
# end="" : es el espacio de cada print

# funcion anonima : lambda x,y : x + y

# ----------------------------------------------------------------------------------------------------------------------------------------

