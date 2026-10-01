#Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. 
#La clave es la palabra en ingles y el valor es la palabra en castellano.Crear las siguientes funciones:
#1) Cargar el diccionario.
#2) Listado completo del diccionario.
#3) Ingresar por  teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.
def cargar_diccionario():
    diccionario = {}
    continua = "s"
    while continua == "s":
        palabra_castellano = input("Ingresar palabra en castellano: ")
        palabra_inlges = input("Ingresar palabra en inglés: ")
        diccionario[palabra_inlges] = palabra_castellano
        continua = input("Quiere cargar otra palabra: [S/N]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for dic in diccionario:
        print(dic,diccionario[dic])

def consulta_palabra(diccionario):
    palabra = input("Ingresar una palabra en inglés: ")
    if palabra in diccionario:
        print("En castellano significa: ", diccionario[palabra])
    else:
        print("La palabra no se encuentra en el diccionario.")
   

diccionario = cargar_diccionario()
imprimir(diccionario)
consulta_palabra(diccionario)