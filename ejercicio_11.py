#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad
#total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide
#confeccionar un programa que ingrese los datos por teclado e informe nivel del mismo según el porcentaje
#de respuestas correctas que ha obtenido, y sabiendo que:

#Nivel máximo: Porcentaje >= 90%.
#Nivel medio: Porcentaje >= 75% y < 90%
#Nivel regular: Porcentaje >= 50% y < 75%
#Fuera de nivel: Porcentaje < 50%

total_preguntas = int(input("Ingresar el total de preguntas realizadas: "))
respuestas_correctas = int(input("Ingresar la cantidad de respuestas correctas: "))

porcentaje_correctas = (respuestas_correctas * 100) / total_preguntas

if porcentaje_correctas >= 90:
    print("NIVEL MÁXIMO")
else:
    if porcentaje_correctas >= 75 and porcentaje_correctas < 90:
        print("NIVEL MEDIO")
    else:
        if porcentaje_correctas >= 50 and porcentaje_correctas < 75:
            print("NIVEL REGULAR")
        else:
            print("FUERA DE NIVEL")