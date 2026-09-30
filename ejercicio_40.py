#Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y mostrar
#por pantalla, luego ordenar de mayor a menor e imprimir nuevamente
lista_enteros = [3,4,2,10,9]

for i in range(len(lista_enteros)):
    for j in range(len(lista_enteros) - i - 1):
        if lista_enteros[j] > lista_enteros[j + 1]:
            aux = lista_enteros[j]
            lista_enteros[j] = lista_enteros[j + 1]
            lista_enteros[j + 1] = aux

print("==========Lista ordenada de menor a mayor=========")
print(lista_enteros)

for i in range(len(lista_enteros)):
    for j in range(len(lista_enteros) - i - 1):
        if lista_enteros[j] < lista_enteros[j + 1]:
            aux = lista_enteros[j]
            lista_enteros[j] = lista_enteros[j + 1]
            lista_enteros[j + 1] = aux

print("==========Lista ordenada de mayor a menor=========")
print(lista_enteros)