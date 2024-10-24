#Kevin Rafael Díaz López - 23/10/2024
#Programa que determina que número es menor.

print("\n\t**PROGRAMA QUE CUAL DE LOS 2 NÚMEROS ES MENOR**")

numero1 = int((input("Ingrese un número: ")))
numero2 = int((input("Ingrese otro número: ")))

if numero1 < numero2 :
    print(f"El número {numero1} es menor que el número {numero2}")
elif numero2 < numero1:
    print(f"El número {numero2} es menor que el número {numero1}")
else:
    print("Los números son iguales")