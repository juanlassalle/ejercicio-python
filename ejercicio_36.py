#En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo
#a lo siguiente:
#a)Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
#b)Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición,
#colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7,
#y colocar "Insuficiente" si la nota es inferior a 4.
#c)Imprimir cuantos alumnos tienen la leyenda "Muy Bueno".
lista_nombres = []
lista_notas = []
dimension_listas = 4
cantidad = 0

for i in range(1,dimension_listas + 1):
    print(f"========={i}º Alumno========")
    nombre = input("Ingresar nombre: ")
    lista_nombres.append(nombre)
    nota = int(input("Ingresar nota: "))
    lista_notas.append(nota)

print(f"Nombres: {lista_nombres}")
print(f"Notas:   {lista_notas}")
print()
for i in range(dimension_listas):
    print(lista_nombres[i])
    print(lista_notas[i])

    if lista_notas[i] >= 8:
        print("Muy Bueno")
        cantidad = cantidad + 1
    else:
        if lista_notas[i] >= 4:
            print("Bueno")
        else:
            print("Insuficiente")

print()
print(f"La cantidad de notas con 'Muy Bueno' es {cantidad}")