#Crear y cargar en una lista los nombres de 5 países y en otra lista paralela la cantidad
#de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último
#ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente
lista_paises = ["Perú","Francia","China","Argentina","Zambia"]
lista_Habitantes = [50,80,1500,45,70]

for i in range(len(lista_paises)):
    for j in range(len(lista_paises) - i - 1):
        if lista_paises[j] > lista_paises[j + 1]:
            aux = lista_paises[j]
            lista_paises[j] = lista_paises[j + 1]
            lista_paises[j + 1] = aux
            aux1 = lista_Habitantes[j]
            lista_Habitantes[j] = lista_Habitantes[j + 1]
            lista_Habitantes[j + 1] = aux1
print(lista_paises)
print(lista_Habitantes)