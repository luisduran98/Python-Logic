# Se coloca un guion bajo _ para avisar que no se usara el indice 
lista = []
for _ in range(5):
    numeros = input("Coloca un numero: ")
    lista.append(int(numeros))


for element in lista:
    print(element, end=" ")
