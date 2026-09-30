#De un operario se conoce su sueldo y los años de antiguedad. Se pide confeccionar un programa que lea los
#datos de entrada e informe:
#a)Si el sueldo es inferior a 500 y su antiguedad es igual o superior a 10 años,otorgarle un aumento del
#20%, mostrar el sueldo a pagar.
#b)Si el sueldo es inferior a 500 pero su antiguedad es menor a 10 años, otorgarle un aumento de 5%
#c)Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios

sueldo_operario = float(input("Ingresar sueldo de operario: "))
antiguedad =  int(input("Ingresar antiguedad del operario: "))
aumento_sueldo = 0

if sueldo_operario < 500 and antiguedad >= 10:
    aumento_sueldo = sueldo_operario + sueldo_operario * 0.20
    print(f"Sueldo a pagar es {aumento_sueldo}")
else:
    if sueldo_operario < 500 and antiguedad < 10:
        aumento_sueldo = sueldo_operario + sueldo_operario * 0.05
        print(f"El aumento de sueldo es {aumento_sueldo}")
    else:
        print(f"EL sueldo es {sueldo_operario}")
