#Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos
#valores almacenan un valor superior a 100.
lista = [2,3,101,5,200,7,305,150]

x = 0
valor_superior100 = 0
while x < len(lista):
    if lista[x] > 100:
        valor_superior100 = valor_superior100 + 1
    x = x + 1

print(f"Valores superiores a 100 de la lista son {valor_superior100}")