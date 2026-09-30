#Desarrollar una función que reciba un string como parametro y nos muestre la cantidad
#de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos

def cantidad_vocales(cadena):
    cantidad = 0

    for i in range(len(cadena)):
        if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
            cantidad = cantidad + 1
    print(f"La cantidad de vocales en la palabra {cadena} es {cantidad}")

cantidad_vocales("paralepipedo")