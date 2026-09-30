#Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir
#en pantalla la leyenda "Todos los números son menores a diez"
numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))
numero3 = int(input("Ingresar el tercer número: "))

if numero1 < 10 and numero2 < 10 and numero3 < 10:
    print("Todos los número menores a 10")
else:
    print("No hay números menores a 10")

