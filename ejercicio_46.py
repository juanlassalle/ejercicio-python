#Elaborar una función que reciba tres enteros y nos retorne el valor promedio
#de los mismos
def obtener_promedio(enteros_a,enteros_b,enteros_c):
    suma = enteros_a + enteros_b + enteros_c
    promedio = suma / 3
    return promedio

def mostrar_promedio():
    entero_a = int(input("Ingresar el primer entero: "))
    entero_b = int(input("Ingresar el segundo entero: "))
    entero_c = int(input("Ingresar el tercer entero: "))

    promedio = obtener_promedio(entero_a,entero_b,entero_c)
    print(promedio)

mostrar_promedio()