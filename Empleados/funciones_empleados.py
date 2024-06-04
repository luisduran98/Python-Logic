from data_empleados import *
from random import randint, choice

def cargar_lista_empleados_random(lista: list, cantidad: int)->None:
    EDAD_MIN = 18
    EDAD_MAX = 65
    next_legajo = 20000
    for _ in range(cantidad):
        legajo = next_legajo
        next_legajo += 1
        genero = choice(["f","m"])
        nombre = choice(nombres_m) if genero == "m" else choice(nombres_f)
        apellido = choice(apellidos)
        edad = randint(EDAD_MIN, EDAD_MAX)
        calle = f"{randint(10, 99)} nro {randint(100, 999)}"
        localidad = choice(localidades)
        provincia = choice(provincias)
        email = f"{nombre.lower()+apellido.lower()}{choice(dominios)}"
        sector = choice(sectores)
        sueldo = float(randint(20000, 50000))
        lista.append(new_empleado(legajo,nombre, apellido, genero, edad, calle, localidad, provincia, email, sueldo, sector))

def new_empleado(legajo: int, nombre: str, apellido: str, genero: str, edad: int, calle: str, localidad: str, provincia: str, email: str, sueldo: float, sector: str)-> dict:
    empleados = {}
    empleados["legajo"] = legajo
    empleados["nombre"] = nombre
    empleados["apellido"] = apellido
    empleados["genero"] = genero
    empleados["edad"] = edad
    empleados["calle"] = calle
    empleados["localidad"] = localidad
    empleados["provincia"] = provincia
    empleados["email"] = email
    empleados["sueldo"] = sueldo
    empleados["sector"] = sector
    return empleados

def mostrar_empleados(lista_empleados: list)->None:
    print("                                               ***Lista de Empleados***")
    print("  Legajo    Nombre     Apellido      Genero    Edad          Calle         Localidad       Provincia          Email                            Sector          Sueldo")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(lista_empleados)):
        mostrar_empleado(lista_empleados[i])
    print()


def mostrar_empleado(un_empleado: dict)->None:
    print(f"  {un_empleado["legajo"]:<8}  {un_empleado["nombre"]:<10} {un_empleado["apellido"]:<15} {un_empleado["genero"]:<8} {un_empleado["edad"]:<10} {un_empleado["calle"]:<15} {un_empleado["localidad"]:<15} {un_empleado["provincia"]:<18} {un_empleado["email"]:<32} {un_empleado["sector"]:<15} {un_empleado["sueldo"]:<10.2f}")