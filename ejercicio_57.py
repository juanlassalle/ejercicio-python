#Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del
#empleado junto a sus últimos tres sueldos (estos tres valores en una tupla).
#El programa debe tener las siguientes funciones:
#1) Carga de los nombres de empleados y sus últimos tres sueldos.
#2) Imprimir el monto total cobrado por cada empleado.
#3) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000
#en los últimos tres meses.
#Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
#empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
def cargar_empleados():
    lista_empleados = []
    dimension_lista_principal = 5
    
    for i in range(dimension_lista_principal):
        nombre_empleado = input("Ingresar nombre: ")
        sueldo_A = float(input("Ingresar primer sueldo: "))
        sueldo_B = float(input("Ingresar segundo sueldo: "))
        sueldo_C = float(input("Ingresar tercer sueldo: "))
        sublista_empleado = [nombre_empleado,(sueldo_A,sueldo_B,sueldo_C)]
        lista_empleados.append(sublista_empleado)
            
    return lista_empleados
#empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
def monto_total(lista_empleados):
    print("Monto total ganado por empleado en los ultimos tres meses")
    for i in range(len(lista_empleados)):
        monto = lista_empleados[i][1][0] + lista_empleados[i][1][1] + lista_empleados[i][1][2]
        print(lista_empleados[i][0], monto)
        
'''def ganancias(empleados):
    for i in range(len(empleados)):
        sueldos = empleados[i][1]  # Guardamos la tupla (2000, 3000, 4233)
        
        # Ahora solo usamos un corchete sobre la variable 'sueldos':
        monto = sueldos[0] + sueldos[1] + sueldos[2]
        
        nombre = empleados[i][0]
        print(nombre, monto)'''

def monto_superior1000(lista_empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for i in range(len(lista_empleados)):
        total = lista_empleados[i][1][0] + lista_empleados[i][1][1] + lista_empleados[i][1][2]
        if total > 1000:
            print(lista_empleados[i][0], total)

#Bloque principal
empleados = cargar_empleados()
monto_total(empleados)
monto_superior1000(empleados)