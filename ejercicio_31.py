#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio
#y cuántas más bajas.
lista_alturas = []
dimension = 5
suma = 0
promedio = 0

for i in range(1,dimension + 1):
    altura = float(input(f"Ingresar altura de la {i}º persona: "))
    lista_alturas.append(altura)
    suma = suma + altura

promedio = suma / len(lista_alturas)

x = 0
personas_altas = 0
personas_bajas = 0

while x < len(lista_alturas):
    if lista_alturas[x] > promedio:
        personas_altas = personas_altas + 1
    else:
        personas_bajas = personas_bajas + 1
    x = x + 1

print(f"El promedio de las alturas es {promedio}")
print(f"Las personas más altas que el promedio son {personas_altas}")
print(f"Las personas más bajas que el promedio son {personas_bajas}")