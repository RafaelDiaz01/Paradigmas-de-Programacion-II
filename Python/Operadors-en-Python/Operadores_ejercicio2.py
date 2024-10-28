# Kevin Rafael Díaz López - 22/10/2024
# Ejercicio que determina si el usuario pertenece a la comunidad UNSIJ utilizando operadores lógicos.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}| COMUNIDAD UNSIJ |{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

estudiante = input("¿Es estudiante de la UNSIJ? (Si/No) ")  # Lee la entrada del usuario y la almacena en la variable estudiante.
estudiante = estudiante.lower() == "si"  # Convierte la respuesta a minúsculas y verifica si es "si".

profesor = input("¿Es profesor de la UNSIJ? (Si/No) ")  # Lee la entrada del usuario y la almacena en la variable profesor.
profesor = profesor.lower() == "si"  # Convierte la respuesta a minúsculas y verifica si es "si".

print(f"¿Pertenece a la comunidad UNSIJ? {estudiante or profesor}")  # Muestra True si el usuario es estudiante o profesor de la UNSIJ.
