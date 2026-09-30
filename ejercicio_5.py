#Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al
#segundo informar su suma y diferencia, en caso contrario informar el producto y la división del
#primero respecto al segundo.
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    suma = numero1 + numero2
    diferencia = numero1 - numero2
    print(f"La suma de {numero1} y {numero2} es: {suma}")
    print(f"La diferencia de {numero1} y {numero2} es: {diferencia}")
else:
    producto = numero1 * numero2
    print(f"El producto de los numeros {numero1} y {numero2} es: {producto}")
    if numero2 > 0:
        division = numero1 / numero2
        print(f"El cociente de los numeros {numero1} y {numero2} es: {division}")
    else:
        print("No se puede dividir por cero")