#Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde
#el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una
#estructura repetitiva)
def calcular_numero_menor():
    num1 = int(input("Ingresar el primer valor: "))
    num2 = int(input("Ingresar el segundo valor: "))
    num3 = int(input("Ingresar el tercer valor: "))

    if num1 < num2 and num1 < num3:
        print(f"El valor menor es {num1}")
    else:
        if num2 < num1 and num2 < num3:
            print(f"El valor menor es {num2}")
        else:
            print(f"El valor menor es {num3}")

calcular_numero_menor()
print("===================")
calcular_numero_menor()