# Kevin Rafael Díaz López - 17/10/2024
# Programa que muestra el uso de los operadores aritméticos en lenguaje Python.

print("\n\t**PROGRAMA QUE MUESTRA EL USO DE LOS OPERADORES ARITMÉTICOS**")
print()  # Imprime una línea en blanco.

print("Ingrese un número: ")  # Muestra un mensaje solicitando al usuario que ingrese un número.
numero1 = int(input())  # Lee un número entero ingresado por el usuario y lo asigna a la variable numero1.

numero2 = int(input("Ingrese otro numero: "))  # Solicita al usuario otro número entero y lo asigna a numero2.

# Realiza operaciones aritméticas entre numero1 y numero2.
suma = numero1 + numero2  # Suma de numero1 y numero2.
resta = numero1 - numero2  # Resta de numero1 menos numero2.
multiplicacion = numero1 * numero2  # Multiplicación de numero1 y numero2.
division = numero1 / numero2  # División de numero1 entre numero2.
modulo = numero1 % numero2  # Módulo de numero1 entre numero2.
dobleast = numero1 ** numero2  # Potencia de numero1 elevado a numero2.
doblediv = numero1 // numero2  # División entera de numero1 entre numero2.

print()  # Imprime una línea en blanco.

print("  ***   Ejemplos de uso de los operadores aritméticos   ***")  # Encabezado para mostrar los resultados.

print(f"El resultado de la suma de {numero1} y {numero2} es {suma}") # Muestra el resultado de la suma de numero1 y numero2.
print(f"El resultado de la resta de {numero1} y {numero2} es {resta}") # Muestra el resultado de la resta de numero1 y numero2.
print(f"El resultado de la multiplicación de {numero1} y {numero2} es {multiplicacion}") # Muestra el resultado de la multiplicación de numero1 y numero2.
print(f"El resultado de la división de {numero1} y {numero2} es {division:.3f}")  # Muestra el resultado de la división con 3 decimales.
print(f"El resultado de módulo de {numero1} y {numero2} es {modulo}")
print(f"El resultado de doble asterisco entre {numero1} y {numero2} es {dobleast}") # Muestra el resultado de la exponenciación de numero1 elevado a numero2.
print(f"El resultado de doble diagonal entre {numero1} y {numero2} es {doblediv}") # Muestra el resultado de la división entera de numero1 entre numero2.
