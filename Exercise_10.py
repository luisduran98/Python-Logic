lista_nombres_aleatorios = ["Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Diego", "Carolina", "Carlos", "Valentina", "Javier", "Mónica", "Sara", "José", "Lucía", "Andrés", "Gabriela", "Ricardo", "Elena", "Fernando"]

lista_generos = ["masculino", "femenino", "masculino", "femenino", "masculino", "femenino", "masculino", "femenino", "masculino", "femenino", "masculino", "femenino", "femenino", "masculino", "femenino", "masculino", "femenino", "masculino", "femenino", "masculino"]

def nombres_aleatorios(lista_nombres:list, lista_generos)-> list:
    from random import randint 
    resultado = []
    nueva_lista_nombres = []
    nueva_lista_generos = []
    numeros_randint = []
    for _ in range(10):
        numeros_randint.append(randint(0, len(lista_nombres_aleatorios) - 1))

    while True:
        conjunto = set(numeros_randint)
        lista_conjunto = list(conjunto)

        if len(lista_conjunto) < 10:
            numeros_randint.append(randint(0, len(lista_nombres_aleatorios) - 1))
        else:
            break
    
    for i in range(10):
        nueva_lista_nombres.append(lista_nombres[lista_conjunto[i]])

    for i in range(10):
        nueva_lista_generos.append(lista_generos[lista_conjunto[i]])

    resultado = [nueva_lista_nombres, nueva_lista_generos]
    return resultado


def notas_aleatorias()->list:
    from random import randint 
    notas = []
    for _ in range(10):
        notas.append(randint(0,10)) 
    return notas


def promedios_parciales(notas_uno:list, notas_dos:list)->list:
    resultados_promedio = []
    for i in range(10):
        promedio_por_iteraciones = (notas_uno[i] + notas_dos[i]) / 2
        resultados_promedio.append(promedio_por_iteraciones)
    return resultados_promedio

def mostraralumnos(info_filtrada:list)->None:
    print("Legajos   Nombres    Generos     1er-Parcial   2do-Parcial   Promedio")
    for i in range(info_filtrada[0]):
        print(f"   {i}       {info_filtrada[1][i]}     {info_filtrada[2][i]}       {info_filtrada[3][i]}       {info_filtrada[4][i]}               {info_filtrada[5][i]}")


def utn_programacion_312(lista_alumnos:list, lista_alumnos_generos:list)->None:
    archivo_aula_312 = nombres_aleatorios(lista_alumnos,lista_alumnos_generos)
    legajos = len(archivo_aula_312[0])
    nombres = archivo_aula_312[0]
    generos = archivo_aula_312[1]
    notas_p1 = notas_aleatorias()
    notas_p2 = notas_aleatorias()
    promedios = promedios_parciales(notas_p1,notas_p2)
    info_filtrada = [legajos, nombres, generos, notas_p1, notas_p2, promedios]

    return info_filtrada

cache = utn_programacion_312(lista_nombres_aleatorios,lista_generos)

mostraralumnos(cache)