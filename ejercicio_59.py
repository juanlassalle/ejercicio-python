#Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
#Implementar las funciones:
#1) Carga de empleados.
#2) Impresión de los empleados y sus sueldos.
#3) Nombre del empleado con sueldo mayor.
#4) Cantidad de empleados con sueldo menor a 1000.
def cargar_empleados():
    empleados = []
    dimension = 5
    for i in range(dimension):
        print(f"Dato empleado {i}")
        nombre = input("Ingresar nombre de empleado: ")
        sueldo = float(input("Ingresar sueldo: "))
        empleados.append((nombre,sueldo))
    return empleados

def impresion(lista):
    print("Nombres y sueldos")
    for nombre,sueldo in lista:
        print(nombre,sueldo)

def sueldo_mayor(lista):
    empleado = lista[0]
    for elemento in lista:
        if elemento[1] > empleado[1]:
            empleado = elemento
    print(f"El empleado de mayor sueldo es {empleado[0]} y su sueldo es {empleado[1]}")

def sueldo_menor1000(lista):
    cantidad = 0
    for ele in lista:
        if ele[1] < 1000:
            cantidad = cantidad + 1
    print(f"La cantidad de sueldos menores a 1000 es {cantidad}")

#Bloque Principal
empleados = cargar_empleados()
impresion(empleados)
sueldo_mayor(empleados)
sueldo_menor1000(empleados)