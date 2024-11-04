# Kevin Rafael Díaz López - 28/10/2024
# Programa que determina el área y el perímetro de un rectángulo o de un círculo.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE CALCULA EL ÁREA Y EL PERÍMETRO|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Inicializa la variable 'i' que controla el menú.
i = 1

# Bucle principal que se ejecuta hasta que el usuario elija la opción de salir (0).
while i != 0:
    # Imprime el menú de opciones.
    print("[1] CALCULAR EL ÁREA DE UN RECTÁNGULO")
    print("[2] CALCULAR EL PERÍMETRO DE UN RECTÁNGULO")
    print("[3] CALCULAR EL ÁREA DE UN CÍRCULO")
    print("[4] CALCULAR EL PERÍMETRO DE UN CÍRCULO")
    print("[0] SALIR")

    # Solicita al usuario una opción del menú y la guarda en 'i'.
    i = float(input("¿Qué desea realizar? "))

    # Opción para salir del programa.
    if i == 0:
        print("S A L I S T E ") # Finaliza el bucle y sale del programa

    # Opción para calcular el área de un rectángulo.
    elif i == 1:
        base= float(input("\nIngrese la base del rectángulo: ")) # Solicita el valor de la base del rectángulo.
        altura = float(input("Ingrese la altura del rectángulo: ")) # Solicita el valor de la altura del rectángulo.
        print(f"\nEl área del rectángulo es: {base * altura:.3f}") # Fórmula para calcular el área de un rectángulo.
        print("---------------------------------------------\n") # Imprime una línea para dar formato al programa.

    # Opción para calcular el perímetro de un rectángulo.
    elif i == 2:
        base = float(input("\nIngrese la base del rectángulo: "))  # Solicita el valor de la base del rectángulo.
        altura = float(input("Ingrese la altura del rectángulo: "))  # Solicita el valor de la altura del rectángulo.
        print(f"\nEl perímetro del rectángulo es: {2 * (base + altura):.3f}") # Fórmula para calcular el perímetro de un rectángulo.
        print("---------------------------------------------\n") # Imprime una línea para dar formato al programa.

    # Opción para calcular el área de un círculo.
    elif i == 3:
        radio = float(input("\nIngrese el radio del círculo: ")) # Solicita el valor del radio del círculo.
        print(f"\nEl área del círculo es: {3.1416 * (radio * radio):.3f}") # Fórmula para calcular el área de un círculo.
        print("---------------------------------------------\n") # Imprime una línea para dar formato al programa.

    # Opción para calcular el perímetro de un círculo.
    elif i == 4:
        radio = float(input("\nIngrese el radio del círculo: "))  # Solicita el valor del radio del círculo.
        print(f"\nEl perímetro del círculo es: {2 * 3.1416 * radio:.3f}") # Fórmula para calcular el perímetro de un círculo.
        print("---------------------------------------------\n") # Imprime una línea para dar formato al programa.

    # Muestra un mensaje de error si el usuario ingresa una opción no válida.
    else:
        print("POR FAVOR ELIJA UNA OPCIÓN VÁLIDA\n")
