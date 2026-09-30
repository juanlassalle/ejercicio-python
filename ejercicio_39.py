#Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar
#una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos
#ordenados de menor a mayor.
cantidad_empleados = int(input("Ingresar la cantidad de empleados: "))
lista_sueldos = []

for i in range(1,cantidad_empleados + 1):
    sueldo = float(input(f"{i}º Sueldo: "))
    lista_sueldos.append(sueldo)

print()
print(lista_sueldos)
print()

for i in range(cantidad_empleados):
    for j in range(cantidad_empleados - i - 1):
        if lista_sueldos[j] > lista_sueldos[j + 1]:
            aux = lista_sueldos[j]
            lista_sueldos[j] = lista_sueldos[j + 1]
            lista_sueldos[j + 1] = aux
print(lista_sueldos)