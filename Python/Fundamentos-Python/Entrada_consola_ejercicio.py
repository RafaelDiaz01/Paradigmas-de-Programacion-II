# Kevin Rafael Díaz López -21/10/2024
# Ejercicio que realiza las operaciones básicas de una calculadora.

numero1 = float(input("Introduce el primer número decimal: ")) # Solicita al usuario que ingrese el primer número decimal y lo convierte a float.
numero2 = float(input("Introduce el segundo número decimal: ")) # Solicita al usuario que ingrese el segundo número decimal y lo convierte a float.

suma = numero1 + numero2 # Realiza la suma de los dos números ingresados.
resta = numero1 - numero2 # Realiza la resta del primer número menos el segundo.
multiplicacion = numero1 * numero2 # Realiza la multiplicación de los dos números ingresados.
division = numero1 / numero2 # Realiza la división del primer número entre el segundo.

print(f"La suma de {numero1} y {numero2} es: {suma}") # Muestra el resultado de la suma de los dos números.
print(f"La resta de {numero1} menos {numero2} es: {resta}") # Muestra el resultado de la resta del primer número menos el segundo.
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}") # Muestra el resultado de la multiplicación de los dos números.
print(f"La división de {numero1} entre {numero2} es: {division}") # Muestra el resultado de la división del primer número entre el segundo.
