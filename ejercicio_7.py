#Se ingresa por teclado un número positivo de un o dos dígitos (1...99) mostrar un mensaje indicando si el
#número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos
#un número entero)

numero = int(input("Ingresar el número: "))

if numero >= 1 and numero <= 9:
    print(f"El número {numero} tiene un dígito")
else:
    if numero >= 10 and numero <= 99:
        print(f"El número {numero} tiene dos dígitos")
    else:
        print(f"El número tiene más de tres dígitos")