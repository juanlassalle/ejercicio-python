#Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
#Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente 
#más baja. En el bloque principal iniciamos por asignación la lista de string:
def mas_caracteres(palabras):
    posicion = 0

    for i in range(len(palabras)):
        if len(palabras[i]) > len(palabras[posicion]):
            posicion = i
    return palabras[posicion]

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mas_caracteres(palabras))