#Kevin Rafael Díaz López - 23/10/2024
#Programa que determina un grupo de edad.

print("\n\t**PROGRAMA QUE DETERMINA GRUPOS DE EDAD**")

edad = int((input("Ingrese su edad: ")))

if edad < 15:
    print("Usted pertenece a Niños y Adolescentes")
elif edad <= 24:
    print("Usted pertenece a Jóvenes")
elif edad <= 44:
    print("Usted pertenece a Adultos Jóvenes")
elif edad <= 60:
    print("Usted pertenece a Adultos Maduros")
else:
    print("Usted pertenece a Adultos Mayores")