#Realizar un programa que pida la carga de dos listas númericas enteras de 4 elementos cada una
#Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista.
#Mostrar esta tercer lista.
lista_enteros_A = []
lista_enteros_B = []
lista_enteros_C = []
dimension_listas = 4

for i in range(dimension_listas):
    entero_A = int(input("Ingresar entero A: "))
    lista_enteros_A.append(entero_A)
    entero_B = int(input("Ingresar entero B: "))
    lista_enteros_B.append(entero_B)

print()
print(lista_enteros_A)
print(lista_enteros_B)

for i in range(dimension_listas):
    suma = lista_enteros_A[i] + lista_enteros_B[i]
    lista_enteros_C.append(suma)

print()
print(f"Lista C: {lista_enteros_C}")
