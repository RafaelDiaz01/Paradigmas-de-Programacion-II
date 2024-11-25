# Kevin Rafael Díaz López - 13/11/2024
# Programa que muestra el uso de los conjuntos (desordenados y mutables).

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RED = "\033[31m" # Define el color rojo para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|RIFA DE UNA LAPTOP DEL 503|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Funciones.

def menu():
    print("[1] VER PARTICIPANTES")
    print("[2] AÑADIR PARTICIPANTES")
    print("[3] ELIMINAR PARTICIPANTES")
    print("[4] SELECCIONAR AL GANADOR")
    print("[0] SALIR")

# Código principal.

participantes = set() # Conjunto vacío.

while True:
    menu() # Se llama la función menu.

    option = int(input("Seleccione la opción que desea realizar: ")) # Puse la variable en inglés para que no me cause detalles con PyCharm.

    if option == 0:
        print(f"\n\t{RED}|SALISTE DEL PROGRAMA|{RESET}")
        break

    elif option == 1:
        print(f"PARTICIPANTES: {participantes}\n")

    elif option == 2:
        participante = input("Ingrese el nombre del participante que se va a agregar a la rifa:  ")
        participantes.add(participante)
        print(f"{participante} se añadió correctamente a la rifa\n")

    elif option == 3:
        participante = input("Ingrese el nombre del participante que se va a eliminar de la rifa: ")

        if participante in participantes:
            participantes.remove(participante)
            print(f"{participante} se eliminó correctamente de la rifa\n")
        else:
            print(f"{participante} no se encuentra en la rifa\n")
