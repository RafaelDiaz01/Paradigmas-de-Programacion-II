# Kevin Rafael Díaz López - 13/11/2024
# Programa que muestra el uso de las tuplas (ordenadas e inmutables).

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|TUPLAS|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

calificaciones_parcial1 = (9.6, 6.3, 6.0, 8.7, 5.0)
paradigmas, bd, redes, arquitectura, ing_s = calificaciones_parcial1
print(calificaciones_parcial1)

for calificacion in calificaciones_parcial1:
    print(calificacion, end = " | ")

# En las tuplas no se puede usar el pop.

print()
promedio_parcial1 = sum(calificaciones_parcial1)/len(calificaciones_parcial1)
print(f"Promedio: {promedio_parcial1}")