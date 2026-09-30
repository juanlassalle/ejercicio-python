#Confeccionar un programa que permita:
#1) Cargar una lista de 10 elementos enteros.
#2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en la otra los
#negativos
#3) Imprimir las dos listas generadas.
def cargar_lista():
    lista_enteros = []
    dimension_lista = 10
    for i in range(dimension_lista):
        entero = int(input(f"Ingresar el {i}º entero: "))
        lista_enteros.append(entero)
    return lista_enteros

def generar_lista_positiva(lista):
    lista_positiva = []
    for i in range(len(lista)):
        if lista[i] > 0:
            lista_positiva.append(lista[i])
    return lista_positiva

def generar_lista_negativa(lista):
    lista_negativa = []
    for i in range(len(lista)):
        if lista[i] < 0:
            lista_negativa.append(lista[i])
    return lista_negativa

lista_principal = cargar_lista()
print()
print(f"Lista principal {lista_principal}")
print()
print(f"Lista positiva {generar_lista_positiva(lista_principal)}")
print()
print(f"Lista negativa {generar_lista_negativa(lista_principal)}")