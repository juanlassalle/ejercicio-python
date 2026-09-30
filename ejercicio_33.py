#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista .
#Mostrar el nombre de persona menor en orden alfabético
lista_nombres = []
dimension_lista = 5

for i in range(1,dimension_lista + 1):
    nombre = input(f"Ingresar el {i}º nombre: ")
    lista_nombres.append(nombre)

# 2. Ordenamiento por método de burbuja (Bubble Sort)
for i in range(len(lista_nombres) - 1):
    for j in range(len(lista_nombres) - 1 - i):
        # Si quieres orden ascendente (A-Z), usa '>'
        # Si quieres orden descendente (Z-A), usa '<'
        if lista_nombres[j] > lista_nombres[j + 1]:
            aux = lista_nombres[j]
            lista_nombres[j] = lista_nombres[j + 1]
            lista_nombres[j + 1] = aux

print()
print(lista_nombres)