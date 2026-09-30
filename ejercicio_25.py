#Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de
#multiplicar del mismo (los primeros 12 términos). Ejemplo: Si ingreso 3 deberá aparecer en 
#pantalla los valores 3,6,9 hasta el 36.
valor_tabla = int(input("Ingresar la tabla de multiplicar (1 - 10): "))
print()
print(f"Tabla de multplicar del {valor_tabla}")
print()
for i in range(1,12 + 1):
    print(f"{valor_tabla} X {i} = {valor_tabla * i}")