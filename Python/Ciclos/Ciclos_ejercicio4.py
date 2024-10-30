# Kevin Rafael Díaz López
# Ejercicio que simula un programa de Banco Azteca

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|¡BIENVENIDO A BANCO AZTECA!|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Inicializa el índice 'i' que controla el menú y el 'saldo' en cero.
i = 1
saldo = 0

# Bucle principal que se ejecuta hasta que el usuario elija la opción de salir (0).
while i != 0:
    # Imprime el menú de opciones.
    print("[1] CONSULTAR SALDO")
    print("[2] INGRESAR DINERO")
    print("[3] RETIRAR DINERO")
    print("[0] SALIR")

    # Solicita al usuario una opción del menú y la guarda en 'i'.
    i = float(input("¿Qué desea realizar? "))

    # Opción para salir del programa.
    if i == 0:
        print("S A L I S T E ")
        break  # Finaliza el bucle y sale del programa.

    # Opción para consultar el saldo.
    elif i == 1:
        print(f"\nSU SALDO ES DE ${saldo}\n")  # Muestra el saldo actual.

    # Opción para ingresar dinero en la cuenta.
    elif i == 2:
        print("\nINGRESANDO DINERO")
        ingresar = int(input("CANTIDAD A INGRESAR: $"))  # Solicita el monto a ingresar.

        # Verifica que el monto a ingresar sea positivo.
        if ingresar < 0:
            print("INGRESA UNA CANTIDAD CORRECTA\n")  # Muestra un mensaje de error si el monto es negativo.
        else:
            saldo += ingresar  # Suma el monto ingresado al saldo actual.

    # Opción para retirar dinero de la cuenta.
    elif i == 3:
        print("\nRETIRANDO DINERO")
        retirar = int(input("CANTIDAD A RETIRAR: $"))  # Solicita el monto a retirar.

        # Verifica que el monto a retirar sea positivo.
        if retirar < 0:
            print("INGRESA UNA CANTIDAD CORRECTA\n")  # Muestra un mensaje de error si el monto es negativo.

        # Verifica si el saldo es suficiente para realizar el retiro.
        elif saldo < retirar:
            print("NO TIENE SALDO SUFICIENTE\n")  # Muestra un mensaje de error si el saldo es insuficiente.

        # Realiza el retiro y actualiza el saldo.
        else:
            saldo -= retirar
            print("DINERO RETIRADO CON EXITO\n")  # Confirma que el retiro fue exitoso.

    # Muestra un mensaje de error si el usuario ingresa una opción no válida.
    else:
        print("ELIJA UNA OPCIÓN VÁLIDA\n")
