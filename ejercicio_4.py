#Calcular el sueldo mensual de un operario conociendo la cantidad de horas
#trabajadas y el valor por hora.
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_por_hora = float(input("Ingrese el valor por hora: "))

sueldo_mensual = horas_trabajadas * valor_por_hora
print("El sueldo mensual del operario es: ", sueldo_mensual)