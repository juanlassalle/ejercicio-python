#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos
#tienen notas mayores o iguales a 7 y cuántos menores.
x = 1
cantidad_mayores = 0
cantidad_menores = 0

while x <= 10:
    nota_alumno = float(input(f"Ingresar nota {x}: ")) 
    if nota_alumno >= 7:
        cantidad_mayores = cantidad_mayores + 1
    else:
        cantidad_menores = cantidad_menores + 1
    x = x + 1

print(f"La cantidad de notas mayores o iguales a 7 es {cantidad_mayores}")
print(f"La cantidad de notas menores a 7 es {cantidad_menores}")