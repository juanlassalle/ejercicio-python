#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un
#mensaje indicando si tiene 1,2 o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.
numero = int(input("Ingresar número: "))

if numero > 0:
    if numero >=1 and numero <= 9:
        print(f"El número {numero} es de una cifra")
    else:
        if numero >= 10 and numero <= 99:
            print(f"El número {numero} es de dos cifras")
        else:
            if numero >= 100 and numero <= 999:
                print(f"El número {numero} es de tres cifras")
            else:
                print("ERROR")
else:
    print("Número negativo. No es posible realizar la operación")