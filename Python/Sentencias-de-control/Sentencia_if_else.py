#Kevin Rafael Díaz López - 23/10/2024
#Programa que determina si un número es par o impar.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE DETERMINA SI UN NÚMERO ES PAR|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

numero = int((input("Ingrese un número: "))) # Solicita un número entero al usuario y almacena el valor en "numero".

# Sentencia para comprobar el módulo del número ingresado.
if numero%2 == 0: # Si el módulo es igual a 0, el número es par.
    print("Su número es par") # Imprime que el número del usuario es par.
else: # Si no se cumplió la condición anterior, el número es impar.
    print("Su número es impar") # Imprime que el número del usuario es par.