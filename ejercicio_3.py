#Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.
numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))
numero3 = int(input("Ingresar el tercer número: "))
numero4 = int(input("Ingresar el cuarto número: "))

suma = numero1 + numero2 + numero3 + numero4
promedio = suma / 4

print("La suma de los cuatro números es: ", suma)
print("El promedio de los cuatro números es: ", promedio)