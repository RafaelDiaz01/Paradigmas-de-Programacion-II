#Kevin Rafael Díaz López - 23/10/2024
#Programa que determina si una persona es mayor de edad utilizando la sentencia if.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE MUESTRA SI UNA PERSONA ES MAYOR DE EDAD|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

edad = int((input("Ingrese su edad en años: "))) # Solicita la edad al usuario y la almecena en la variable "edad".

if edad >= 18: # Si la edad ingresada es mayor igual a 18, se cumple la condición.
    print("Usted es mayor de edad") # Imprime un letrero indicando que el usuario es mayor de edad.

# Si la condición no se cumplió, no entró al if.
print("Usted es menor de edad") # Imprime un letrero indicando que el usuario es mayor de edad.