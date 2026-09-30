#Plantear una función que reciba un string en mayúsculas o minúsculas y retorne
#la cantidad de letras "a" o "A".

def cantidad_letras(cadena):
    cantidad = 0
    for i in range(len(cadena)):
        if cadena[i] == "a" or cadena[i] == "A":
            cantidad = cantidad + 1
    return cantidad

print(f"La cantidad de letras a o A que tiene la cadena es {cantidad_letras("America")}")