# Kevin Rafael Díaz López - 22/10/2024
# Ejercicio que determina si el usuario aplica para una bonificación utilizando operadores relacionales y lógicos.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}| BONIFICACIÓN DE BUEN FIN |{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

cantidad_gastada = float(input("Cantidad gastada: "))  # Lee el valor gastado por el usuario y lo almacena en cantidad_gastada.
mayor = cantidad_gastada > 5000  # Verifica si el gasto es mayor a 5000 y almacena el resultado booleano en mayor.

meses = input("¿La compra fue a MSI? (Si/No)")  # Lee si la compra fue realizada a MSI.
meses = meses.lower() == "si"  # Convierte la entrada a minúsculas y verifica si es "si".

print(f"¿Aplica bonificación de Buen Fin? {mayor and meses}")  # Verifica si ambas condiciones son verdaderas.
