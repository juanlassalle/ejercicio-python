#Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de 
#productos y como valor el precio del mismo. Desarrollar además las funciones de:
#1) Imprimir en forma completa el diccionario
#2) Imprimir solo los artículos con precio superior a 100
def cargar_diccionario():
    productos = {}
    dimension = 5

    for i in range(dimension):
        producto = input("Ingresar producto: ")
        precio = float(input("Ingresar precio: "))
        productos[producto] = precio
    return productos

def imprimir(productos):
    for producto in productos:
        print(producto,productos[producto])

def imprimir_mayor100(productos):
    for producto in productos:
        if productos[producto] > 100:
            print(producto)

#Bloque principal
productos = cargar_diccionario()
imprimir(productos)
imprimir_mayor100(productos)