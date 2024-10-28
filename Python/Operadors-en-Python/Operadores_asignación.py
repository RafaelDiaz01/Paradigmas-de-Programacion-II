# Kevin Rafael Díaz López - 17/10/2024
# Programa que muestra el uso de los operadores de asignación.

print("\n\t**PROGRAMA QUE MUESTRA EL USO DE LOS OPERADORES DE ASIGNACIÓN**")
print()  # Imprime una línea en blanco.

# Asignación múltiple.
print("   ***   ASIGNACIÓN MULTIPLE  ***")  # Imprime el título para la sección de asignación múltiple.

# Asignación múltiple de enteros.
numero1, numero2 = 7, 10  # Asigna 7 a numero1 y 10 a numero2 en una sola línea.
print(f"Asignación múltiple de enteros: {numero1} y {numero2}") # Imprime el valor de los números enteros.

# Asignación múltiple de decimales.
decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592  # Asigna valores decimales a varias variables en una sola línea.
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}") # Imprime el valor de los números decimales.

# Asignación múltiple combinando tipos de datos.
nombre, numero1, decimal4 = "Rafael", 7, 3.1415926  # Asigna diferentes tipos de datos a varias variables en una línea.
print(f"Asignación múltiple: {nombre}, {numero1} y {decimal4}")

# Asignación de operaciones aritméticas.
suma = numero1 + numero2  # Calcula la suma de numero1 y numero2 y la asigna a suma.
resta = decimal1 - decimal2  # Calcula la resta de decimal1 menos decimal2 y la asigna a resta.
print(f"La suma de {numero1} y {numero2} es: {suma}") # Imprime el resultado de la suma de numero1 y numero2.
print(f"La resta de {decimal1} y {decimal2} es: {resta:.3f}")  # Imprime el resultado de la resta con 3 decimales.

# Asignación encadenada.
print()  # Imprime una línea en blanco.
print("   ***   ASIGNACIÓN ENCADENADA   ***")  # Imprime el título para la sección de asignación encadenada.

# Asignación del mismo valor a varias variables.
numero5 = numero6 = numero7 = 12  # Asigna el valor 12 a las variables numero5, numero6 y numero7 al mismo tiempo.
print(f"Numero 5 es igual a: {numero5}") # Imprime el valor de numero5.
print(f"Numero 6 es igual a: {numero6}") # Imprime el valor de numero6.
print(f"Numero 7 es igual a: {numero7}") # Imprime el valor de numero7.

# Intercambio de variables.
print()  # Imprime una línea en blanco.
print("   ***   INTERCAMBIO DE VARIABLES   ***")  # Imprime el título para la sección de intercambio de variables.

# Solicita dos números al usuario y los intercambia.
print("Ingrese un número: ")
numero8 = int(input())  # Lee un número entero ingresado por el usuario y lo asigna a numero8.

print("Ingrese otro número: ")
numero9 = int(input())  # Lee otro número entero ingresado por el usuario y lo asigna a numero9.

print(f"Valores asignados: primer número= {numero8} y segundo número= {numero9}")  # Imprime los valores asignados inicialmente.
numero9, numero8 = numero8, numero9  # Intercambia los valores de numero8 y numero9.
print(f"Numeros intercambiados: primer número= {numero8} y segundo número= {numero9}")  # Imprime los valores después del intercambio.
