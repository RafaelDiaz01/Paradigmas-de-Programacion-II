# Kevin Rafael Díaz López - 24/10/2024
# Bucle While

print("\t**PROGRAMA QUE IMPRIME LOS NUMEROS DESDE EL 1 HASTA UN TOPE**")
numero = int(input("Ingrese un número tope: "))
i = 1
j = 0

print(f"\nLos numeros del 1 al {numero} son: ")
while i <= numero:
    print(i , end = " ") # Con la palabra reservada end agregamos un letrero
    i = i + 1

print()

print(f"\nLos números pares del 0 al {numero} son: ")
while j <= numero:
    if j%2 == 0:
        print(j, end = " ")
    j = j + 1
print("\nFin de la impresión")

