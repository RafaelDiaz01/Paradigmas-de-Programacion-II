# Kevin Rafael Díaz López - 18/10/2024
# Programa que muestra el uso de los operadores lógicos en Python para evaluar dos entradas de texto ingresadas por el usuario.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE MUESTRA EL USO DE LOS OPERADORES LÓGICOS|{RESET}")  # Imprime el título en color verde.
print()  # Imprime una línea en blanco.

# Solicita al usuario que ingrese "SI" o "NO".
operador = input("Ingrese SI o NO: ")  # Lee la primera entrada del usuario y la guarda en la variable operador.
operador2 = input("De nuevo ingrese SI o NO: ")  # Lee la segunda entrada del usuario y la guarda en operador2.

# Convierte las entradas a minúsculas y verifica si coinciden con "si" o "no".
operador = operador.lower() == "si"  # Convierte la primera entrada a minúsculas y la compara con "si"; asigna el resultado booleano a operador.
operador2 = operador2.lower() == "no"  # Convierte la segunda entrada a minúsculas y la compara con "no"; asigna el resultado booleano a operador2.

print()  # Imprime una línea en blanco.
print(f"¿Lo que ingresó la primera vez es SI? {operador}")  # Muestra si la primera entrada fue "SI".
print(f"¿Lo que ingresó la segunda vez es NO? {operador2}")  # Muestra si la segunda entrada fue "NO".

# Operador lógico "and".
print()  # Imprime una línea en blanco.
print(f"¿En los 2 casos el resultado fue verdadero? {operador and operador2}")  # Verifica si ambas expresiones son verdaderas.

# Operador lógico "or".
print(f"¿En algun caso el resultado fue verdadero? {operador or operador2}")  # Verifica si alguna de las expresiones es verdadera.

# Operador lógico "not".
print()  # Imprime una línea en blanco.
print(f"Lo contrario de la primera expresión? {not operador}")  # Niega el valor de operador y muestra el resultado.
print(f"Lo contrario de la segunda expresión? {not operador2}")  # Niega el valor de operador2 y muestra el resultado.
