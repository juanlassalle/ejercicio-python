#En una empresa se almacenaron los sueldos 10 personas.
#Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#1) Carga de los sueldos en una lista
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos.
#5) Mostrar todos los sueldos que están por debajo del promedio.
def cargar_lista():
    lista_sueldos = []
    dimension_lista = 10

    for i in range(1,dimension_lista + 1):
        sueldo = float(input(f"Ingresar sueldo {i}: "))
        lista_sueldos.append(sueldo)
    return lista_sueldos

sueldos = cargar_lista()
print(f"Sueldos: {sueldos}")

def sueldos_superiores_4000():
    cantidad = 0
    for i in range(len(sueldos)):
        if sueldos[i] > 4000:
            cantidad = cantidad + 1
    return cantidad

def sueldo_promedio():
    suma = 0
    promedio = 0
    for i in range(len(sueldos)):
        suma = suma + sueldos[i]
        promedio = suma / len(sueldos)
    return promedio

def sueldos_bajo_promedio():
    promedio = sueldo_promedio()
    for i in range(len(sueldos)):
        if sueldos[i] < promedio:
            print(f"Sueldos bajo promedio: {sueldos[i]}")

#cargar_lista()
print(f"Cantidad de sueldos por arriba de 4000: {sueldos_superiores_4000()}")
print(f"Promedio: {sueldo_promedio()}")
sueldos_bajo_promedio()