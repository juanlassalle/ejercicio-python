#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base
#y la altura de un triángulo. El programa deberá informar:
#a)De cada triángulo la medida de su base, su altura y su superficie.
#b)La cantidad de triángulos cuya superficie es mayor a 12.
n_datos = int(input("Ingresar N Datos: "))

print()
for i in range(1,n_datos + 1):
    print(f"{i}º Triángulo")
    base = int(input("Ingresar base del triángulo: "))
    altura = int(input("Ingresar altura del triángulo: "))
    superficie = (base * altura) / 2
    print(f"El triángulo de base {base} y altura {altura} tiene una superficie de {superficie}")
    print()
    print("=====================================================================================")