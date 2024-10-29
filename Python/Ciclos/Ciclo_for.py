# Kevin Rafael Díaz López - 29/10/2024

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|EJEMPLO DE CICLO FOR|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

frase = input("Ingresa una frase: ")

for caracter in frase:
    print(caracter, end = "-")
print("\nFIN DE CADENA")

print() # Imprime espacio en blanco.
alumnos = ["Albert", "Kevin", "Elton", "Diana", "Rosendo", "Amelia", "Sergio"]
for alumno in alumnos:
    print(f"Hola {alumno}")