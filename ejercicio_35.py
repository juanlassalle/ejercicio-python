#Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra
#Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer
#producto ingresado
lista_nombres = []
lista_precios = []
dimension_listas = 5

for i in range(1,dimension_listas + 1):
    print(f"{i}º Producto")
    nombre = input("Ingresar nombre: ")
    lista_nombres.append(nombre)
    precio = float(input("Ingresar precio: "))
    lista_precios.append(precio)

print(f"Nombres: {lista_nombres}")
print(f"Precios: {lista_precios}")

cantidad = 0

for i in range(dimension_listas):
    if lista_precios[i] > lista_precios[0]:
        cantidad = cantidad + 1

print(f"La cantidad de precios mayores al primer producto es {cantidad}")