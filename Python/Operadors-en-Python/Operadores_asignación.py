#Kevin Rafael Díaz López - 17/10/2024

numero1, numero2 = 7,10

print(f"Numero 1 es igual a: {n1}")
print(f"Numero 2 es igual a: {numero2}")

numero3, cad, numero4 = 11, "Hola", 9

print(f"Numero 3 es igual a: {numero3}")
print(f"Número 4 es igual a: {numero4}")
print(f"La cadena es: {cad}")

#Tambien se puede asignar sumas y restas
suma = numero1 + numero2
resta = numero3 - numero4
print("")
print(suma)
print(resta)

print("")
#Asignacion encadenada
numero5 = numero6 = numero7 = 12

print(f"Numero 5 es igual a: {numero5}")
print(f"Numero 6 es igual a: {numero6}")
print(f"Numero 7 es igual a: {numero7}")

print("")
#Intercambio de variables
print("Ingrese un número")
numero8 = int(input())

print("Ingrese otro número")
numero9 = int(input())

print(numero8, numero9)

numero9, numero8 = numero8, numero9
print(f"Numeros intercambiados: numero8= {numero8} y numero9= {numero9}")

#Asignación Multiple
numero10, numero11 = int(input("Ingrese un número")), int(input("Ingrese otro número"))
print(f"Sus números son: {numero10} y {numero11}")
