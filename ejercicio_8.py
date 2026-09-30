#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
numero1 = int(input("Ingresar el primero número: "))
numero2 = int(input("Ingresar el segundo número: "))
numero3 = int(input("Ingresar el tercer número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El número {numero1} es el mayor")
else:
    if numero2 > numero1 and numero2 > numero3:
        print(f"El número {numero2} es el mayor")
    else:
        print(f"El número {numero3} es el mayor")