# Kevin Rafael Díaz López - 24/10/2024
# Programa que calcula la suma acumulativa

print("\t**PROGRAMA QUE CALCULA LA SUMA ACUMULATIVA**")
numero = int(input("Ingrese el número final: "))
acumulador = 0
i = 0
while i <= numero:
    acumulador = acumulador + i
    i += 1

print(f"La suma de 0 hasta {numero} es: {acumulador}")
