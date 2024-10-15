# Kevin Rafael Díaz López - 14/10/2024
# Ejercicio que muestra el casting de variables en Python

# Convertir los siguientes números en cadenas
numero1 = 3.14159265
numero2 = 12
numero3 = 0

# Se realiza el casting de números a cadenas
cadena1 = str(numero1)
cadena2 = str(numero2)
cadena3 = str(numero3)

# Se imprimen las conversiones de números a cadenas
print(f"Número 3.14159265 convertido a cadena: {cadena1}")
print(f"Número 12 convertido a cadena: {cadena2}")
print(f"Número 0 convertido a cadena: {cadena3}")
print()  # Salto de línea

# Indicar el valor booleano de los números anteriores
print(f"El valor booleano de 3.14159265 es: {bool(numero1)}")
print(f"El valor booleano de 12 es: {bool(numero2)}")
print(f"El valor booleano de 0 es: {bool(numero3)}")
print()  # Salto de línea

# c) Se convierten las cadenas a números
cadena_num1 = "10002"
cadena_num2 = "100.02"
cadena_num3 = "0"

# Se realiza el casting de cadenas a números
numero_convertido1 = int(cadena_num1)  # Convertir a entero
numero_convertido2 = float(cadena_num2)  # Convertir a flotante
numero_convertido3 = int(cadena_num3)  # Convertir a entero

# Se imprimen las conversiones de cadenas a números
print(f'Cadena "10002" convertida a entero: {numero_convertido1}')
print(f'Cadena "100.02" convertida a flotante: {numero_convertido2}')
print(f'Cadena "0" convertida a entero: {numero_convertido3}')
print()  # Salto de línea

# Indicar el valor booleano de las cadenas anteriores
print(f"El valor booleano de la cadena '10002' es: {bool(cadena_num1)}")
print(f"El valor booleano de la cadena '100.02' es: {bool(cadena_num2)}")
print(f"El valor booleano de la cadena '0' es: {bool(cadena_num3)}")

# Explicación del valor booleano de la cadena "0"
print("\nEl valor booleano de cualquier cadena que no esté vacía es True.")
print("Esto incluye la cadena '0', aunque su valor numérico convertido es 0, sigue siendo una cadena no vacía.")
