# Kevin Rafael Díaz López - 23/10/2024
# Programa que determina qué número es menor.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE DETERMINA CUÁL DE LOS 2 NÚMEROS ES MENOR|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

numero1 = int((input("Ingrese un número: "))) # Solicita al usuario que ingrese un número.
numero2 = int((input("Ingrese otro número: "))) # Solicita al usuario que ingrese otro número.

# Compara los dos números para determinar cuál es menor.
if numero1 < numero2:  # Si el primer número es menor que el segundo, indica que el primer número es menor.
    print(f"El número {numero1} es menor que el número {numero2}")  # Imprime un letrero en consola.
elif numero2 < numero1:  # Si el segundo número es menor que el primero, indica que el segundo número es menor.
    print(f"El número {numero2} es menor que el número {numero1}")  # Imprime un letrero en consola.
else:  # Si ambos números son iguales, indica que ambos son iguales.
    print("Los números son iguales")  # Imprime un letrero en consola.
