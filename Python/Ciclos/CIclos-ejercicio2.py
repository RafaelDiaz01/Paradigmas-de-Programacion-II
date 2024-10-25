# Kevin Rafael Díaz López - 24/10/2024
# Programa que calcula la suma acumulativa entre 2 números

print("\n \t**PROGRAMA QUE CALCULA LA SUMA ACUMULATIVA ENTRE 2 NÚMEROS**")
numero1 = int(input("Ingrese el número inicial: "))
numero2 = int(input("Ingrese el número final: "))

i = numero1
acumulador = 0

while i <= numero2:
    acumulador = acumulador + i
    i += 1

print(f"La suma de {numero1} hasta {numero2} es: {acumulador}")
