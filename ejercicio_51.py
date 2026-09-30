#Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba
#la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque 
#principal de nuestro programa.
def producto_lista(lista):
    producto = 1
    for i in range(len(lista)):
        producto = producto * lista[i]
    return producto

lista = [2, 3, 4, 5, 6, 7]

print(f"El producto de los elementos de la lista es {producto_lista(lista)}")