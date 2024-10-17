#Kevin Rafael Díaz López

print("Ingrese un número")
numero1=int(input())

numero2=int(input("Ingrese otro numero"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
modulo = numero1 % numero2
dobleast = numero1 ** numero2
doblediv = numero1 // numero2

print(f"El resultado de la suma de {numero1} y {numero2} es {suma}")
print(f"El resultado de la resta de {numero1} y {numero2} es {resta}")
print(f"El resultado de la multiplicación de {numero1} y {numero2} es {multiplicacion}")
print(f"El resultado de la división de {numero1} y {numero2} es {division:.3f}")
print(f"El resultado de módulo de {numero1} y {numero2} es {modulo}")
print(f"El resultado de doble asterisco entre {numero1} y {numero2} es {dobleast}")
print(f"El resultado de doble diagonal entre {numero1} y {numero2} es {doblediv}")

