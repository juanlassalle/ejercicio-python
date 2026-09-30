#Elaborar una función que nos retorne el perímetro de un cuadrado pasando
#como parámetros el valor de un lado.
def obtener_perimetro(lado):
    return 4 * lado

def mostrar_perimetro():
    lado = float(input("Ingresar valor de un lado del cuadrado: "))
    print(f"El perimetro del cuadrado es {obtener_perimetro(lado)}")

mostrar_perimetro()