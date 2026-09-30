#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo,
#negativo o nulo.
numero = int(input("Ingresar el primer número: "))

if numero < 0:
    print(f"El número {numero} es negativo")
else:
    if numero == 0:
        print(f"El número {numero} es nulo")
    else:
        print(f"El número es {numero} es positivo")