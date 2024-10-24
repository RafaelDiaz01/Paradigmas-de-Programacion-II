#Kevin Rafael Díaz López - 23/10/2024
#Programa que determina la estación del año dependiendo del mes.

print("\n\t**PROGRAMA QUE DETERMINA LA ESTACIÓN DEL AÑO**")

mes = int((input("Ingrese el número de mes: ")))

if mes <= 0:
    print("Error, esa estación no existe")
elif mes < 3 or mes == 12:
    print("La estación es invierno")
elif mes < 6:
    print("La estación es primavera")
elif mes < 9:
    print("La estación es verano")
elif mes < 12:
    print("La estación es otoño")
else:
    print("Incorrect")

#otro:incorrect
#3,4,5 primavera
#6,7,8 verano
#9,10,11 otoño
#12, 1, 2 invierno