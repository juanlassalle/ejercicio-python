#Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos
#valores fueron pares y cuántos impares. Emplear el operador "%" en la condición de la estructura
#condicional (este operador retorna el resto de la división de dos valores, por ejemplo
#11%2 retorna 1)

n_numeros = int(input("Ingresar N enteros: "))
x = 1
pares = 0
impares = 0

while x <= n_numeros:
    entero = int(input(f"Ingresar un número entero {x}: "))
    if entero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    x = x + 1

print(f"La cantidad de números pares es {pares}")
print(f"La cantidad de números impares es {impares}")
    