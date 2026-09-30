#Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos
#valores enteros x e y (distintos de cero). Posteriormente imprimir en pantalla en que 
#cuadrante se ubica dicho punto.(1º Cuadrante si X > 0 y Y > 0, 2º Cuadrante
#X < 0 y Y > 0, etc)
X = int(input("Ingresar el valor X de la coordenada: "))
Y = int(input("Ingresar el valor Y de la coordenada: "))

if X > 0 and Y > 0:
    print(f"El punto ({X},{Y}) se encuentra en el primer cuadrante")
else:
    if X > 0 and Y < 0:
        print(f"El punto ({X},{Y} se encuentra en el segundo cuadrante)")
    else:
        if X < 0 and Y < 0:
            print(f"El punto ({X},{Y}) se encuentra en el tercer cuadrante")
        else:
            print(f"El punto ({X},{Y}) se encuentra en el cuarto cuadrante")