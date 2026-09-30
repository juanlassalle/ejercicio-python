#Confeccionar un programa con las siguientes funciones:
#1) Cargar un lista de 5 enteros.
#2) Retornar el mayor y menor valor de la lista mediante un tupla.
#Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
def cargar_lista():
    lista_enteros = []
    dimension_lista = 5
    for i in range(dimension_lista):
        entero = int(input(f"Ingresar el {i}º entero: "))
        lista_enteros.append(entero)
    return lista_enteros

def obtener_mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        else:
            if lista[i] < menor:
                menor = lista[i]
    return (mayor,menor)

#Bloque principal
lista = cargar_lista()
mayor,menor = obtener_mayor_menor(lista)
print(f"Mayor valor de la lista: {mayor}")
print(f"Menor valor de la lista: {menor}")