#Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero
#con el segundo y a este resultado se lo multiplica por el tercero

valor1 = int(input("Ingresar el primer valor: "))
valor2 = int(input("Ingresar el segundo valor: "))
valor3 = int(input("Ingresar el tercer valor: "))

if valor1 == valor2 and valor2 == valor3:
    suma = valor1 + valor2
    producto = suma * valor3
    print(f"La suma de los primeros valores es {suma} y el producto de la suma por el tercero es {producto}")
else:
    print("Es imposible realizar las operaciones pedidas")