# Kevin Rafael Díaz López -21/10/2024
# Ejercicio que ingresa y muestra datos de profesores de la UNSIJ.

nombre_profesor = input("Introduce el nombre del profesor: ") # La función input() toma el valor como un string.
cubiculo_profesor = int(input("Introduce el número de cubículo: ")) # Solicita al usuario el número del cubículo, y lo convierte a un entero utilizando int().
horas_clase = float(input("Introduce el número de horas de clase a la semana: ")) # Solicita el número de horas de clase a la semana, y lo convierte a float.
trabajo = input("¿El profesor tiene más de 5 años en la UNSIJ? (Si/No): ") # Solicita al usuario si el profesor tiene más de 5 años en la UNSIJ, ingresando "Si" o "No".
trabajo = trabajo.lower() == "si" # Convierte la respuesta a minúsculas y la compara con "si".

print() # Salto de línea.

print("**** Datos del Profesor ****") # Imprime un encabezado en la consola.
print(f"Nombre del profesor: {nombre_profesor}") # Imprime el nombre del profesor.
print(f"Número de cubículo: {cubiculo_profesor}") # Imprime el número del cubículo del profesor.
print(f"Horas de clase a la semana: {horas_clase:.3f}")  # Muestra las horas de clase con tres decimales.
print(f"Tiene más de 5 años en la UNSIJ: {trabajo}") # Imprime "True" si el profesor tiene más de 5 años en la UNSIJ o "False" si no tiene más de 5 años en la UNSIJ.
