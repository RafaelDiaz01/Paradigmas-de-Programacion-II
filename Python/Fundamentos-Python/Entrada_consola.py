# Kevin Rafael Díaz López - 21/10/2024
# Ejercicio que muestra la entrada de datos por consola para interactuar con el usuario con valores dinámicos.

# Solicita al usuario que introduzca un número decimal.
numero1_cadena = input("Introduce un número decimal: ") # La función 'input()' recibe la entrada del usuario como un string.
numero2_cadena = input("Introduce otro número decimal: ") # Al igual que antes, el valor se almacena como una cadena de texto.
resultado_cadena = numero1_cadena + numero2_cadena # Al tratarse de cadenas, lo que se hace es unir los dos valores como texto.
print() # Imprime un salto de línea.

print(" ****  Recibir número sin un casting de variables  ****") # Imprime un mensaje en consola.
# Imprime el resultado de la concatenación de las dos cadenas.
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}") # La sintaxis 'f"{}"' es para interpolación de cadenas, donde las variables se insertan dentro del texto.

# Se realiza un 'casting' de las variables de tipo string a tipo float.
numero1_float = float(numero1_cadena) # Esto es para realizar una suma en lugar de concatenar texto.
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Suma los dos valores ya convertidos a números decimales.
print() # Imprime un salto de línea.

print(" ****  Casting de variables  ****") # Imprime un mensaje en consola.
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}") # Imprime el resultado de la suma de los dos números decimales.

numero1_float = float(numero1_cadena) # Se convierte el valor de las cadenas a números decimales con el casting.
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Se realiza la suma como operación matemática.
print() # Imprime un salto de línea.

print(" ****  Casting de variables  ****") # Imprime un mensaje en consola.
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}") # Imprime el resultado de la suma después de convertir las cadenas a números decimales.
