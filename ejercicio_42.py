#Desarrollar un programa con dos funciones. La primera que solicite el ingreso de un entero
#y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre
#el producto de los mismos. Llamar desde el bloque del programa principal a ambas funciones.
def cuadrado_numero():
    entero = int(input("Ingresar un número entero: "))
    cuadrado_numero = entero * entero
    print(f"El cuadrado de {entero} es {cuadrado_numero}")

def producto():
    valor_A = int(input("Ingresar el primer valor: "))
    valor_B = int(input("Ingresar el segundo valor: "))

    prod = valor_A * valor_B
    print(f"El producto de {valor_A} y {valor_B} es {prod}")

#Programa Principal
cuadrado_numero()
producto()