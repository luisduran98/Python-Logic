def  entero_random(lista:list, cant:int, desde:int, hasta:int)->None:
    from random import randint as aleatorio
    for _ in range(cant):
        lista.append(aleatorio(desde,hasta))


def crear_lista_entero_random(cant:int, desde:int, hasta:int)->list:
    lista = []
    entero_random(lista, cant, desde, hasta)
    return lista

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

def entero_in_lista(lista:list, target:int)->bool:
    resultado = False
    for num in lista:
        if num == target:
            resultado = True
            break
    return resultado
    
def buscar_entero(lista:list, target:int)->int:
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def ordenar_lista(lista:list, valor:bool)->None:
 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    print(lista)
    

def sorteador(lista:list)->None:
    from time import sleep
    from random import randint as random
    resultado = random(0,len(lista) - 1)
    sleep(3)
    print(f"El ganador es {resultado}, recibe tu premio {lista[resultado]}")


lista = crear_lista_entero_random(10, 1, 10)
print(lista)

# ordenar_lista_ascendente(lista)