# Tarea pedir 10 numeros usando una lista y calcular la sumatoria, el promedio, el mayor y cuantas veces esta repetido.

lista = []
suma = 0
contador_repetidos = 0

for i in range(10):
    numeros = int(input("Coloca un numero aca: "))
    suma += numeros
    lista.append(numeros)

mayor = 0

for num in lista:
    if num > mayor:
        mayor = num
        contador_repetidos = 0
    if num == mayor:
        contador_repetidos += 1 
    
    
print(f"SUMA: {suma}, PROMEDIO: {suma/10}, MAYOR: {mayor}, REPETIDOS: {contador_repetidos}")



