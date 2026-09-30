#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio
#de las personas
n_alturas = int(input("Ingresar la cantidad de alturas: "))
x = 1
suma = 0
promedio = 0

while x <= n_alturas:
    altura_persona = float(input(f"Ingresar altura de la persona {x}: "))
    suma = suma + altura_persona
    x = x + 1
promedio = suma / n_alturas

print(f"El promedio de las alturas es {promedio}")