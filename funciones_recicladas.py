# def mapear_lista_nombre_sector(lista:list)->list:
#     lista_retorno = []
#     for emp in lista:
#         lista_retorno.append((emp["nombre"], emp["sector"]))
#     return lista_retorno


def mostar_lista_tuplas(lista:list)->None:
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"{lista[i][j]:5}", end="")
        print()   

prueba = [1,2,3,4,5]

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

def reducer_lista(funcion,lista:list)->int:
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            resultado = funcion(lista[i], lista[j])
    return resultado

        


# print(reducer_lista(lambda a,b : ,prueba))


# *METODOS
# metodo items() : te devuelve los cada elemento del diccionario en fromato tupla
# metodo type() : te devuelvo el tipo de valor que representa
# metodo capitalize() : tranforma la primera poscicion en mayuscula
# metodo upper(): tranforma todo a mayuscula



# importaciones
# from time import sleep ////  sleep() : detiene el programa durante el tiempo que quieras


# Operador Ternario

# x if x > y else y

# Print
# end="" : es el espacio de cada print

# funcion anonima : lambda x,y : x + y