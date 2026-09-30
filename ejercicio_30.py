#Almacenar en una lista los sueldos (valores float) de 5 operarios.
#Imprimir la lista y el promedio de sueldos.
sueldos = []
operarios = 5
suma = 0

for i in range(1,operarios + 1):
    sueldo = float(input(f"Ingresar sueldo del {i} operario: "))
    sueldos.append(sueldo)
    suma = suma + sueldo

promedio = suma / len(sueldos)
print(f"La suma de los sueldos es {suma}")
print(f"El promedio de los sueldos es {promedio}")
    