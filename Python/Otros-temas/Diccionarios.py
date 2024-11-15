# Kevin Rafael Díaz López - 13/11/2024
# Programa que muestra el uso de los diccionarios (desordenados e inmutables).
# Se almacenan en forma de key-valor.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|D I C C I O N A R I O S|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

diccionario = {"Key1": 10, "Key2": 7}
profesor = {'Nombre': "Alberto", 'Correo': "alberto.mtba@unsij" , 'cubo': 12}
print(profesor)

correo = profesor.get("Correo")
print(f"Correo: {correo}")
cubo = profesor["Nombre"]
print(f"Nombre del profesor: {cubo}")