# Kevin Rafael Díaz López - 23/10/2024
# Programa que determinará un descuento en compras en "La cona" utilizando sentencias de control.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|DESCUENTOS POR SER MIEMBROS DE LA CONA|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

pago = int(input("Ingrese la cantidad comprada: "))  # Solicita al usuario el monto de la compra.
membresia = input("¿Cuenta con membresía? (Si/No) ")  # Pregunta al usuario si tiene membresía.
membresia = membresia.lower() == "si"  # Convierte la respuesta a minúsculas y verifica si es "si" para determinar si el usuario tiene membresía.

# Validación de la cantidad comprada
if pago < 0: # Si la cantidad ingresada es negativa, muestra un mensaje de error.
    print("Cantidad Incorrecta")

# Aplicación de descuentos
elif membresia and pago >= 1000:
    pago = pago - (pago * (8 / 100))  # Si el usuario tiene membresía y la compra es de 1000 o más, aplica un descuento del 8%.
    print("Tu descuento es del 8%")  # Indica el descuento del 8% aplicado.
    print(f"El total es de ${pago}")  # Muestra el total después del descuento.

elif membresia:
    pago = pago - (pago * (5 / 100))  # Si el usuario tiene membresía pero la compra es menor de 1000, aplica un descuento del 5%.
    print("Tu descuento es del 5%")  # Indica el descuento del 5% aplicado.
    print(f"El total es de ${pago}")  # Muestra el total después del descuento.

else:
    print("Se te invita a ser miembro de la cona para obtener un descuento de hasta el 8%")  # Mensaje para quienes no tienen membresía.
    print(f"El total es de ${pago}")  # Muestra el total sin aplicar ningún descuento.
