#Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro
#de la lista (es decir si dicho valor se encuentra en 2 o más opciones en la lista).
lista_enteros = []
dimension_lista = 5
cantidad = 0

for i in range(dimension_lista):
    elemento = int(input("Ingresar elemento a la lista: "))
    lista_enteros.append(elemento)

print("\n")
print("==========Lista de enteros==========")
print(lista_enteros)

mayor = lista_enteros[0]

for i in range(len(lista_enteros)):
    if lista_enteros[i] > mayor:
        mayor = lista_enteros[i]
        
   
print(f"Mayor de la lista {mayor}")
print()
for i in range(len(lista_enteros)):
    if lista_enteros[i] == mayor:
        cantidad = cantidad + 1
if cantidad > 1:
    print("El mayor se repite en la lista")