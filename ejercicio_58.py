#Confeccionar un programa que permita la carga de una lista de 5 enteros por  teclado.
#Luego en otras funciones:
#1) Imprimirla en forma completa.
#2) Obtener y mostrar el mayor.
#3) Mostrar la suma de todas sus componentes.
#Utilizar la nueva sintaxis de for vista en este concepto.
def cargar_lista():
    lista = []
    for elemento in range(5):
        entero = int(input("Ingresar entero: "))
        lista.append(entero)
    return lista

def imprimir(lista):
    print("Lista completa")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    may = lista[0]
    for elemento in lista:
        if elemento > may:
            may = elemento
    print(f"El mayor elemento de la lista es {may}")

def suma(lista):
    sum = 0
    for elemento in lista:
        sum = sum + elemento
    print(f"La suma de los elementos de la lista es {sum}")

lista = cargar_lista()
imprimir(lista)
mayor(lista)
suma(lista)