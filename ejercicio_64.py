#Crear un diccionario en Python que defina como clave el número de documento de una persona y como 
#valor un string con su nombre. Desarrollar las siguientes funciones:
#1) Cargar por teclado los datos de 4 personas.
#2) Listado completo del  diccionario.
#3) Consulta del nombre de una persona ingresando su número de documento.
def cargar_diccionario():
    personas = {}
    dimension = 4

    for i in range(dimension):
        dni = int(input("Ingresar DNI: "))
        nombre = input("Ingresar nombre: ")
        personas[dni] = nombre
    return personas

def imprimir(personas):
    for dni in personas:
        print(dni,personas[dni])

def consultar_nombre(personas):
    dni = int(input("Ingresar número de DNI: "))
    if dni in personas:
        print(personas[dni])
    else:
        print("DNI no existente")

#Bloque principal
personas = cargar_diccionario()
imprimir(personas)
consultar_nombre(personas)