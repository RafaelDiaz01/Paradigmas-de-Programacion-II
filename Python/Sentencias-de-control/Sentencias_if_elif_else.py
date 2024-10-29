#Kevin Rafael Díaz López - 23/10/2024
#Programa que determina un grupo de edad.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE DETERMINA GRUPOS DE EDAD|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

edad = int((input("Ingrese su edad: "))) # Solicita la edad al usuario y almecena el valor en "edad".

if edad < 15:  # Si la edad es menor que 15, indica que pertenece al grupo "Niños y Adolescentes".
    print("Usted pertenece a Niños y Adolescentes")  # Imprime un letrero en consola.
elif edad <= 24:  # Si la edad es 15-24, indica que pertenece al grupo "Jóvenes".
    print("Usted pertenece a Jóvenes")  # Imprime un letrero en consola.
elif edad <= 44:  # Si la edad es 25-44, indica que pertenece al grupo "Adultos Jóvenes".
    print("Usted pertenece a Adultos Jóvenes")  # Imprime un letrero en consola.
elif edad <= 60:  # Si la edad es 45-60, indica que pertenece al grupo "Adultos Maduros".
    print("Usted pertenece a Adultos Maduros")  # Imprime un letrero en consola.
else:  # Si la edad es mayor que 60, indica que pertenece al grupo "Adultos Mayores".
    print("Usted pertenece a Adultos Mayores")  # Imprime un letrero en consola.
