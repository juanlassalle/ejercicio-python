#Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule 
#se informe su rango de variación (debe mostrar el mayor y el menor de ellos).
valor1 = int(input("Ingresar el primer valor: "))
valor2 = int(input("Ingresar el segundo valor: "))
valor3 = int(input("Ingresar el tercer valro: "))

if valor1 < valor2 and valor1 < valor3:
    print(f"El valor menor es {valor1}")
else:
    if valor2 < valor3:
       print(f"El valor menor es {valor2}")
    else:
        print(f"El valor menor es {valor3}")

if valor1 > valor2 and valor1 > valor3:
    print(f"El valor mayor es {valor1}")
else:
    if valor2 > valor3:
       print(f"El valor mayor es {valor2}")
    else:
        print(f"El valor mayor es {valor3}")