# Kevin Rafael Díaz López - 07/11/2024
# Programa que muestra el uso de funciones mediante una calculadora básica en Python.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|CALCULADORA BÁSICA|{RESET}\n")  # Imprime el título en color verde.


# Función para imprimir el menú de la calculadora.
def menu():
    print("[1] SUMA")
    print("[2] RESTA")
    print("[3] MULTIPLICACIÓN")
    print("[4] DIVISIÓN")
    print("[0] SALIR")


# Función para realizar las operaciones básicas.
def operacion(numero1, numero2, opcion):
    if opcion == 1:
        return numero1 + numero2, "suma"
    elif opcion == 2:
        return numero1 - numero2, "resta"
    elif opcion == 3:
        return numero1 * numero2, "multiplicación"
    elif opcion == 4:
        if numero2 != 0:
            return numero1 / numero2, "división"
        else:
            return None, "división (error: división por cero)"
    return None


# Código Principal
while True:
    menu()  # Llama a la función del menú.
    opcion = int(input("\nSeleccione su opción: "))

    if opcion == 0:
        print("S A L I S T E")
        break
    elif 1 <= opcion <= 4:
        # Pide los números
        numero1 = float(input("Ingrese un número: "))
        numero2 = float(input("Ingrese un segundo número: "))

        resultado, nombre = operacion(numero1, numero2, opcion)
        print(f"El resultado de la {nombre} es: {resultado}\n")
    else:
        print("E r r o r: opción no válida\n")
