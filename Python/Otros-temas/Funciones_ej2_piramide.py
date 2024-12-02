# Kevin Rafael Díaz López - 07/11/2024
# Programa que muestra el uso de funciones e imprime pirámides en Python.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PIRÁMIDES CON FUNCIONES|{RESET}\n")  # Imprime el título en color verde.

# Función para imprimir el menú de las pirámides.
def menu():
    print("[1] PIRÁMIDE 1")
    print("[2] PIRÁMIDE 2 ")
    print("[3] PIRÁMIDE 3")
    print("[4] PIRÁMIDE 4")
    print("[0] SALIR")

def logic (opcion, filas):
    # Se definen las variables para el carácter del asterisco y el espacio.
    asterisco = "*"
    espacio = " "
    if opcion == 1:
        # PIRÁMIDE 1
        print("\nPIRÁMIDE 1")
        for i in range(filas + 1):
            espacios = espacio * i  # Multiplica el iterador por el espacio y lo almacena en espacios.
            asteriscos = asterisco * i  # Multiplica el iterador por el asterisco y lo almacena en asteriscos.
            print(f"{asteriscos}{espacios}")  # Imprime primero los asteriscos y luego los espacios.
        print() # Imprime un salto de línea.
    elif opcion == 2:
        # PIRÁMIDE 2
        print("\nPIRÁMIDE 2\n")
        for i in range(filas + 1):
            espacios = espacio * i  # Multiplica el iterador por el espacio y lo almacena en espacios.
            asteriscos = asterisco * (filas - i)  # Multiplica el resultado de (filas - iterador) por el asterisco y lo almacena en asteriscos.
            print(f"{asteriscos}{espacios}")  # Imprime primero los asteriscos y luego los espacios.
        print()  # Imprime un salto de línea.
    elif opcion == 3:
        # PIRÁMIDE 3
        print("PIRÁMIDE 3")
        for i in range(filas + 1):
            espacios = espacio * (filas - i)  # Multiplica el espacio por (filas - iterador) y lo almacena en espacios.
            asteriscos = asterisco * ((2 * i) - 1)  # Multiplica el asterisco por ((2 por iterador) - 1) y lo almacena en asteriscos.
            print(f"{espacios}{asteriscos}")  # Imprime primero los espacios y luego los asteriscos.
        print()  # Imprime un salto de línea.
    elif opcion == 4:
        # PIRÁMIDE 4
        print("\nPIRÁMIDE 4")
        for i in range(filas + 1):
            asteriscos = asterisco * i  # Multiplica el asterisco por el iterador y lo almacena en asteriscos.
            espacios = espacio * (filas - i)  # Multiplica el resultado de (filas - iterador) por el espacio y lo almacena en espacios.
            print(f"{espacios}{asteriscos}")  # Imprime primero los espacios y luego los asteriscos.
        print()  # Imprime un salto de línea.

# Código Principal
while True:
    menu()  # Llama a la función del menú.
    opcion = int(input("\nSeleccione su opción: "))

    if opcion == 0: # Verifica si la opción es para salir.
        print("S A L I S T E")
        break
    elif 1 <= opcion <= 4:
        # Pide el número de filas
        filas = int(input("Ingrese el número de filas: "))

        # Llamada a la función para imprimir las pirámides.
        logic(opcion, filas)
    else:
        print("E r r o r: opción no válida\n") # Imprime error en caso de elegir una opción inválida.
