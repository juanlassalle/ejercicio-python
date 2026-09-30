#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa
#que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300
#y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empreasa
#en sueldos al personal.
n_empleados = int(input("Ingresar la cantidad de empleados: "))
cantidad_100_300 = 0
cantidad_mayor_300 = 0
x = 1

while x <= n_empleados:
    sueldo = float(input(f"Ingresa sueldo del empleado {x}: "))
    if sueldo >= 100 and sueldo <= 300:
        cantidad_100_300 = cantidad_100_300 + 1
    if sueldo > 300:
        cantidad_mayor_300 = cantidad_mayor_300 + 1
    x = x + 1

print(f"Los sueldos entre 100 y 300 son {cantidad_100_300}")
print(f"Los sueldos mayores a 300 son {cantidad_mayor_300}")
