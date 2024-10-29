# Kevin Rafael Díaz López - 24/10/2024
# Programa que determina el promedio de un alumno e indica si aprobó o no la materia.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA PARA CALCULAR EL PROMEDIO DE UNA MATERIA|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

parcial1 = float(input("Ingrese la calificación del primer parcial: ")) # Solicita la calificación del primer parcial.
parcial2 = float(input("Ingrese la calificación del segundo parcial: ")) # Solicita la calificación del segundo parcial.
parcial3 = float(input("Ingrese la calificación del tercer parcial: ")) # Solicita la calificación del tercer parcial.
ordinario = float(input("Ingrese la calificación del ordinario: ")) # Solicita la calificación del ordinario.

calificacion = (((parcial1 + parcial2 + parcial3) / 3) + ordinario) / 2 # Calcula el promedio de las calificaciones ingresadas.

if calificacion < 0 or calificacion > 10: # Si el promedio es menor a 0 o mayor a 10 imprime un mensaje de error.
    print("E R R O R")
elif calificacion <6: # Si el promedio es menor a 6 pero mayor a 0 imprime un mensaje de reprobado.
    print(f"La calificación final es de: {calificacion:.1f}. Lo siento, no aprobaste.")
else: # Si no se cumplieron las condiciones anteriores, significa que el alumno aprobó.
    print(f"La calificación final es de: {calificacion:.1f}. ¡Felicidades! Aprobaste")