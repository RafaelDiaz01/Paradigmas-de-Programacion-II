# Kevin Rafael Díaz López - 24/10/2024
# Programa que determina el promedio de un alumno e indica si aprobó o no la materia.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA PARA CALCULAR EL PROMEDIO DE UNA MATERIA|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
ordinario = float(input("Ingrese la calificación del ordinario: "))

calificacion = (((parcial1 + parcial2 + parcial3) / 3) + ordinario) / 2

if calificacion < 0 or calificacion > 10:
    print("E R R O R")
elif calificacion <6:
    print(f"La calificación final es de: {calificacion:.1f}. Lo siento, no aprobaste.")
else:
    print(f"La calificación final es de: {calificacion:.1f}. ¡Felicidades! Aprobaste")