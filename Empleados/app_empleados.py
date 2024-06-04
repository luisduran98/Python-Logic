from funciones_empleados import *
from os import system

TAM = 10

empleados = []

cargar_lista_empleados_random(empleados,TAM)

mostrar_empleados(empleados)

def mostrar_empleado_legajo(legajo:int)->None:
    flag_validador_legajo = False
    if int(legajo):
        for i in range(len(empleados)):
            if empleados[i]["legajo"] == legajo:
                print(f"nombre:  {empleados[i]["nombre"]}")
                print(f"apellido: {empleados[i]["apellido"]}")
                print(f"genero: {empleados[i]["genero"]}")
                print(f"edad: {empleados[i]["edad"]}")
                print(f"calle: {empleados[i]["calle"]}")
                print(f"localidad: {empleados[i]["localidad"]}")
                print(f"provincia: {empleados[i]["provincia"]}")
                print(f"email: {empleados[i]["email"]}")
                print(f"sector: {empleados[i]["apellido"]}")
                print(f"sueldo: {empleados[i]["sueldo"]}")

                flag_validador_legajo = True

        if not flag_validador_legajo:
            print("No existe")  
            

def mostrar_nombres_sectores()->None:
    if len(empleados) > 0:
        for i in range(len(empleados)):
            print(f"nombre:  {empleados[i]["nombre"]:<10} |   sector: {empleados[i]["sector"]:<10}")
    else:
        print("no hay empleados para mostrar") 


def busqueda_por_sector(sector:str)->None:
    flag_encontrado = False
    if type(sector) == str:
        for i in range(len(empleados)):
            if empleados[i]["sector"] == sector.capitalize():
                print(f"nombre:  {empleados[i]["nombre"]:<10} |   sector: {empleados[i]["sector"]:<10}")
                flag_encontrado = True
        if not flag_encontrado:
            print("no hay empleados con ese sector")


def mostrar_promedio_de_sector(sector:str)->None:
    cant_sueldos = 0 
    suma_sueldos = 0
    flag_encontrado = False
    if type(sector) == str:
        for i in range(len(empleados)):
            if empleados[i]["sector"] == sector.capitalize():
                cant_sueldos += 1
                suma_sueldos += empleados[i]["sueldo"]
                print(f"El promedio de sueldos en este sector ronda los : {suma_sueldos/cant_sueldos}")
                flag_encontrado = True
        if not flag_encontrado:
            print("no hay empleados en este sector")


def mostrar_promedio_sueldo_sectores()->None:
    sectores_sueldos = []
    if len(empleados) > 0:
        for i in range(len(empleados)):
            for j in range(len(sectores_sueldos)):
                if len(sectores_sueldos) == 0:
                    sectores_sueldos.append({"sector" : empleados[i]["sector"], "sueldo": empleados[i]["sueldo"], "cant_sueldo": 1})

                if empleados[i]["sector"] == sectores_sueldos[j]["sector"]:
                    sectores_sueldos[j]["sueldo"] += empleados[i]["sueldo"]
                    sectores_sueldos[j]["cant_sueldo"] += 1
            else:
                sectores_sueldos.append({"sector" : empleados[i]["sector"], "sueldo": empleados[i]["sueldo"], "cant_sueldo": 1}) 
        print("-------------- Promedio Sueldo -------------")
        for y in range(len(sectores_sueldos)):
            promedio = sectores_sueldos[y]["sueldo"] / sectores_sueldos[y]["cant_sueldo"]
            
            print(f"sector : {sectores_sueldos[y]["sector"]:<15}|           {promedio:<15.2f}")
    else:
        print("No hay empleados para mostrar")


def mostrar_sueldo_mas_alto()->None:
    salario_mas_alto = 0
    empleado = {}
    for i in range(len(empleados)):
        if empleados[i]["sueldo"] > salario_mas_alto:
            salario_mas_alto = empleados[i]["sueldo"]
            empleado = {"nombre": empleados[i]["nombre"],"sector": empleados[i]["sector"],"sueldo": empleados[i]["sueldo"]}
    print("--------------------- Sueldo mas alto -------------------------")
    print(f"nombre: {empleado["nombre"]:<10} | sector: {empleado["sector"]:<15} | sueldo: {empleado["sueldo"]}")
    

def mostrar_email_mas_corto()->None:

    tamaño_mail = len(empleados[0]["email"])
    empleado_mail = {"nombres": [], "mails": []}
    for i in range(1, len(empleados)):
        if tamaño_mail > len(empleados[i]["email"]):
            tamaño_mail = len(empleados[i]["email"])

    for i in range(len(empleados)):
        if len(empleados[i]["email"]) == tamaño_mail:
            empleado_mail["nombres"].append(empleados[i]["nombre"])
            empleado_mail["mails"].append(empleados[i]["email"])

    for i in range(len(empleado_mail["nombres"])):
        print(f"nombre: {empleado_mail["nombres"][i]:<10}   |   email: {empleado_mail["mails"][i]}   |   caracteres: {tamaño_mail}")


def mostrar_mayor_sueldo()->None:
    mayor_sueldo = 0

    for i in range(len(empleados)):
        if empleados[i]["sueldo"] > mayor_sueldo:
            mayor_sueldo = empleados[i]["sueldo"]
            sector = empleados[i]["sector"]

    print(f"El sector que mas cobra es {sector}")


# def mostar_sector_con_mas_personal()->None:
#     contador_sectores = contador
#     contador = 0
#     for i in range(len(empleados)):

#         for j in range(1, len(empleados)):
#             empleados[i]["sector"] == empleados[j]["sector"]
#             contador += 1
#     conta