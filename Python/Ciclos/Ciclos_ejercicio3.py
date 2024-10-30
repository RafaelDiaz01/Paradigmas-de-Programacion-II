# Kevin Rafael Díaz López
# Programa que realiza operaciones básicas.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|CALCULADORA BÁSICA|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

i = 0 # Inicializa la variable 'i' en 0, que se usará para controlar el menú de opciones.

# Bucle que continúa hasta que el usuario seleccione la opción de salir (7).
while i != 7:
    # Muestra el menú de operaciones disponibles.
    print()
    print("[1] SUMA")
    print("[2] RESTA")
    print("[3] MULTIPLICACIÓN")
    print("[4] DIVISIÓN")
    print("[5] DIVISIÓN ENTERA")
    print("[6] EXPONENCIACIÓN")
    print("[7] SALIR")

    # Solicita al usuario que seleccione una opción del menú.
    i = float(input("\nSeleccione su opción: "))

    # Verifica si la opción seleccionada es '7' (salir).
    if i == 7:
        break  # Sale del bucle y termina el programa.
    else:
        # Si la opción no es '7', solicita al usuario dos números para realizar la operación.
        numero1 = float(input("\nIngrese un número: "))
        numero2 = float(input("Ingrese un segundo número: "))

    # Realiza la operación correspondiente a la opción seleccionada.
    if i == 1:
        print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}")  # Suma
    elif i == 2:
        print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}")  # Resta
    elif i == 3:
        print(f"La multiplicación de {numero1} y {numero2} es {numero1 * numero2}")  # Multiplicación
    elif i == 4:
        print(f"La división de {numero1} y {numero2} es {numero1 / numero2}")  # División
    elif i == 5:
        print(f"La división entera de {numero1} y {numero2} es {numero1 // numero2}")  # División entera
    elif i == 6:
        print(f"La exponenciación de {numero1} y {numero2} es {numero1 ** numero2}")  # Exponenciación
    else:
        # Si el usuario ingresó una opción no válida, muestra un mensaje de error.
        print("ERROR, ESA OPCIÓN NO EXISTE\n")

# Mensaje final indicando que el programa ha finalizado.
print("S A L I S T E")
