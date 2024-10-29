# Kevin Rafael Díaz López - 24/10/2024

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|TOUR TURÍSTICO ECOTURIXTLÁN|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

precio_adulto = 200  # Precio de entrada para adultos.
precio_niño = 100  # Precio de entrada para niños.

cliente = input("Ingrese el nombre del cliente: ")  # Almacena el nombre del cliente en la variable "cliente".
adultos = int(input("Ingrese el número de adultos: "))  # Solicita el número de adultos.
niños = int(input("Ingrese el número de niños: "))  # Solicita el número de niños.
dia = input("Ingrese el día de la semana: ").lower()  # Se convierte a minusculas para comparar de forma más sencilla.

precio_niño = precio_niño * niños  # Calcula el costo total para niños.
precio_adulto = precio_adulto * adultos  # Calcula el costo total para adultos.
total = precio_niño + precio_adulto  # Suma los costos para obtener el total.

if dia in ["miercoles", "viernes", "sabado", "domingo"]:  # Verifica si el día está en esta lista.
    print(f"Gracias por su visita {cliente} este día {dia}. El costo total es de ${total}")  # Muestra el total sin descuento.
elif dia in ["lunes", "martes", "jueves"]:  # Verifica si el día está en esta lista.
    total = total - (total * (10 / 100))  # Aplica un 10% de descuento al total.
    print(f"Gracias por su visita {cliente} este día {dia}. El costo total es de ${total}")  # Muestra el total con descuento.
else:
    print("E R R O R")  # Muestra un mensaje de error para días inválidos.