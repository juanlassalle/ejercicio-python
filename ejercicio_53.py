#Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos
#y sus precios.
#Definir las siguientes funciones:
#1) Cargar los nombres de artículos y sus precios.
#2) Imprimir los nombres y precios
#3) Imprimir el nombre de artículo con un precio mayor.
#4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio
#menor o igual al valor ingresado.
def cargar_datos():
    lista_articulos = []
    lista_precios = []
    lista_dimension = 5

    for i in range(1,lista_dimension + 1):
        print(f"Ingresar {i}º artículo")
        articulo = input("Ingresar artículo: ")
        lista_articulos.append(articulo)
        precio = float(input("Ingresar precio: "))
        lista_precios.append(precio)
        print()
    return [lista_articulos,lista_precios]

def imprimir_datos(articulo,precio):
    for i in range(len(articulo)):
        print(f"{articulo[i] - precio[i]}")

def nombre_articulo_mayor_precio(articulo,precio):
    mayor = precio[0]
    posicion = 0
    for i in range(1,len(articulo)):
        if precio[i] > mayor:
            mayor = precio[i]
            posicion = i
    print(f"Artículo con mayor precio es {articulo[posicion]} y su precio es {mayor}")

def nuevo_articulo(articulo,precio):
    importe = float(input("Ingresar importe: "))
    for i in range(len(articulo)):
        if precio[i] <= importe:
            print(f"{articulo[i] - precio[i]}")

articulo,precio = cargar_datos()
imprimir_datos(articulo,precio)
nombre_articulo_mayor_precio(articulo,precio)
nuevo_articulo(articulo,precio)