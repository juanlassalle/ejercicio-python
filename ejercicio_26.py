#Realizar un programa que lea los datos de n triángulos, e informar:
#a)De cada uno de ellos, que tipo de triángulo es: equilatero, isósceles o escaleno
#b)Cantidad triángulos de cada tipo.
n_triangulos = int(input("Ingresar la cantidad de triángulos a analizar: "))

cantidad_equilatero = 0
cantidad_isosceles = 0
cantidad_escaleno = 0

for i in range(1,n_triangulos + 1):
    print(f"{i}º Triángulo")
    ladoA = int(input("Ingresar valor del lado A: "))
    ladoB = int(input("Ingresar valor del lado B: "))
    ladoC = int(input("Ingresar valor del lado C: "))

    if ladoA == ladoB and ladoA == ladoC:
        print("Triángulo equilatero")
        cantidad_equilatero = cantidad_equilatero + 1
    else:
        if ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            print("Triángulos isósceles")
            cantidad_isosceles = cantidad_isosceles + 1
        else:
            print("Triángulo escaleno")
            cantidad_escaleno = cantidad_escaleno + 1

print(f"La cantidad de triángulos equilateros es {cantidad_equilatero}")
print(f"La cantidad de triángulos isósceles es {cantidad_isosceles}")
print(f"La cantidad de triángulos escalenos es {cantidad_escaleno}")
