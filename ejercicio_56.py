#Confeccionar un programa con las siguientes funciones:
#1) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores.
#2) Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados
#y muestre el nombre del empleado con su sueldo mayor.
#En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar
#a la función que muestra el nombre de empleado con sueldo mayor.
def cargar_empleado():
    empleado = input("Ingresar el nombre del empleado: ")
    sueldo = float(input("Ingresar el sueldo del empleado: "))

    return (empleado,sueldo)

def mayor_sueldo(empleado_A,empleado_B):
    if empleado_A[1] > empleado_B[1]:
        print(f"El empleado {empleado_A[0]} tiene el mayor sueldo")
    else:
        print(f"El empleado {empleado_B[0]} tiene el mayor sueldo")

primer_empleado = cargar_empleado()
segundo_empleado = cargar_empleado()

mayor_sueldo(primer_empleado,segundo_empleado)