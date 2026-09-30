#Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuántos
#de esos nombres tienen 5 o más caracteres.
lista_nombres = ["Juan","Sebastian","Jose","Mirta","Daniela"]

nombres_caracteres = 0

x = 0
while x < len(lista_nombres):
    if len(lista_nombres[x]) >= 5:
        nombres_caracteres = nombres_caracteres + 1
    x = x + 1
print(f"Nombres con cinco o más carácteres {nombres_caracteres}")