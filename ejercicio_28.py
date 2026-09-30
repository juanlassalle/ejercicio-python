#Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos.
#con valor iguales o superiores a 7.
lista = [2,9,8,7,1]

valores_siete = 0
for i in range(len(lista)):
    if lista[i] >= 7:
        valores_siete = valores_siete + 1

print(f"Los valores iguales o superiores a 7 son {valores_siete}")