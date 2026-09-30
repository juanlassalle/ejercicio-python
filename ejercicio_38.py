#Crear una lista y almacenar los nombres de 5 paises. Ordenar alfabéticamente
#la lista e imprimirla
lista_paises = []
dimension_lista = 5

for i in range(dimension_lista):
    pais = input("Ingresar pais: ")
    lista_paises.append(pais)
print()
print(lista_paises)
print()
print("==========Lista Ordenada==========")
for i in range(dimension_lista):
    for j in range(dimension_lista - i - 1):
        if lista_paises[j] > lista_paises[j + 1]:
            auxiliar = lista_paises[j]
            lista_paises[j] = lista_paises[j + 1]
            lista_paises[j + 1] = auxiliar

print(lista_paises)