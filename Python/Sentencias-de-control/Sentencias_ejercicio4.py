# Kevin Rafael Díaz López - 23/10/2024
# Programa que determina si te permiten el acceso al bar "La Negra".

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|ACCESO A BAR 'LA NEGRA'|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

edad = int(input("Ingresa tu edad: "))  # Solicita al usuario su edad.
presupuesto = int(input("Ingresa tu presupuesto: "))  # Solicita al usuario su presupuesto.

if edad <= 0 or edad > 150:  # Si la edad es menor o igual a 0 o mayor a 150, se muestra un mensaje de error.
    print("Ingrese una edad correcta")
elif edad >= 18 and presupuesto >= 250:  # Si la edad es 18 o más y el presupuesto es de al menos 250, se permite el acceso.
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar")  # Si no cumple con las condiciones, se le niega el acceso.

