#Confeccionar un programa que permita cargar un código de producto como clave en un diccionario. 
#Guardar para dicha clave el nombre del producto, su precio y cantidad en stock. Implementar las 
#siguientes actividades:
#1) Carga de datos en el diccionario.
#2) Listado completo de productos.
#3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
#4) Listado de todos los productos que tengan un stock con valor cero.
def cargar_diccionario():
    productos = {}
    continuar = "s"

    while continuar == "s":
        codigo = int(input("Ingresar código de producto: "))
        producto = input("Ingresar nombre de producto: ")
        precio = float(input("Ingresar precio: "))
        stock = int(input("Ingresar stock: "))
        productos[codigo] = (producto,precio,stock)
        continuar = input("Desea cargar otro producto [s/n]?: ")
    return productos

def listar(productos):
    print("Listado completo")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

def consultar_producto(productos):
    codigo = int(input("Ingresar código de producto a consultar: "))
    if codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
    else:
        print("Código inexistente")

def stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

productos = cargar_diccionario()
listar(productos)
consultar_producto(productos)
stock_cero(productos)