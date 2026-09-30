#Definir una función que cargue una lista con palabras y la retorne.
#Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de
#cinco carácteres.
def cargar_lista():
    palabras = []
    dimension = 5
    for i in range(dimension):
        palabra = input("Ingresar palabra: ")
        palabras.append(palabra)
    return palabras

def mostrar_palabras(lista):
    