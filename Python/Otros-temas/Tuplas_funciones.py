# Kevin Rafael Díaz López - 13/11/2024
# Programa que muestra tuplas usando funciones.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|TUPLAS Y FUNCIONES|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.


def promedio_final(qualification1, qualification2, qualification3, ordinario):
    promedio_parcial = (qualification1 + qualification2 + qualification3) / 3
    final = (promedio_parcial + ordinario) / 2
    return promedio_parcial, final


# Código a nivel de módulo.
qualification1 = float(input("Ingrese la primer calificación: "))
qualification2 = float(input("Ingrese la segunda calificación: "))
qualification3 = float(input("Ingrese la tercer calificación: "))
ordinario = float(input("Ingrese la calificación del ordinario: "))
parcial, final = promedio_final(qualification1, qualification2, qualification3, ordinario)

print(f"El promedio parcial es: {parcial}")
print(f"El promedio final es: {final}")