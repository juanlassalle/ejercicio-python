#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la 
#primera función definida.

def orden_menor_mayor(entero_a,entero_b,entero_c):
    enteros = [entero_a,entero_b,entero_c]

    for i in range(len(enteros)):
        for j in range(len(enteros) - i - 1):
            if enteros[j] > enteros[j + 1]:
                aux = enteros[j]
                enteros[j] = enteros[j + 1]
                enteros[j + 1] = aux
    print(enteros)

def cargar_enteros():
    entero_a = int(input("Ingresar el primer entero: "))
    entero_b = int(input("Ingresar el segundo entero: "))
    entero_c = int(input("Ingresar el tercer entero: "))

    orden_menor_mayor(entero_a,entero_b,entero_c)

cargar_enteros()