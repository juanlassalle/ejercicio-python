#Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
#(4 por la mañana y 4 por la tarde). Confeccionar un programa que permita almacenar
#los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.
sueldos_manana = []
sueldos_tarde = []
dimension_lista_man = 4
dimension_lista_tar = 4

print("===========Empleados Mañana===========")
for i in range(1,dimension_lista_man + 1):
    sueldo_empleado_man = float(input(f"Ingresar sueldo del empleado {i}º: "))
    sueldos_manana.append(sueldo_empleado_man)

print("===========Empleados Tarde===========")
for i in range(1,dimension_lista_tar + 1):
    sueldo_empleado_tar = float(input(f"Ingresar sueldo del empleado {i}º: "))
    sueldos_tarde.append(sueldo_empleado_tar)

x = 0
while x < len(sueldos_manana):
    print(f"Sueldo mañana: {sueldos_manana[x]}")
    x = x + 1

y = 0
while y < len(sueldos_tarde):
    print(f"Sueldo tarde: {sueldos_tarde[y]}")
    y = y + 1