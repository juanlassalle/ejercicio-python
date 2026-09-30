#Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "promocionado"
nota1 = float(input("Ingresar la primera nota: "))
nota2 = float(input("Ingresar la segundo nota: "))
nota3 = float(input("Ingresar la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7 :
    print("Promocionado")
else:
    print("No promocionado")