# Kevin Rafael Díaz López - 20/01/2025
# Programa que muestra el uso de los conjuntos (desordenados y mutables).

import random

archivo = open("historial_rifa.txt", "a") # Crea el archivo de historial

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
    print("[5] HISTORIAL DE GANADORES")
    print("[0] SALIR")


# Código principal.

participantes = [] # Lista vacía.

while True:
    menu() # Se llama la función menu.

    try:
        option = int(input("Seleccione la opción que desea realizar: ")) # Puse la variable en inglés para que no me cause detalles con PyCharm.
    except ValueError:
        print(f"{RED}Opción no válida{RESET}\n")
        continue  # Continúa con el siguiente ciclo del bucle.

    if option == 0:
        print(f"\n\t{RED}|SALISTE DEL PROGRAMA|{RESET}")
        break

    elif option == 1:
        if participantes:
            print(f"PARTICIPANTES: {participantes}\n")
        else:
            print(f"{RED}No hay participantes en la rifa{RESET}\n")

    elif option == 2:
        participante = input("Ingrese el nombre del participante que se va a agregar a la rifa:  ")

        if participante in participantes:
            print("El nombre no esta disponible, ingrese otro por favor\n")
        else:
            participantes.append(participante)
            print(f"{participante} se añadió correctamente a la rifa\n")

    elif option == 3:
        if participantes:
            participante = input("Ingrese el nombre del participante que se va a eliminar de la rifa: ")

            if participante in participantes:
                participantes.remove(participante)
                print(f"{participante} se eliminó correctamente de la rifa\n")
            else:
                print(f"{RED}{participante} no se encuentra en la rifa{RESET}\n")
        else:
            print(f"{RED}No hay participantes en la rifa{RESET}\n")

    elif option == 4:
        i = 1
        if participantes:
            ganador = random.choice(participantes)
            print(f"{GREEN}El ganador de la rifa es {ganador}{RESET}\n")
            archivo.write(f"Ganador {i} = {ganador} \n")
            i += 1
        else:
            print(f"{RED}No hay participantes en la rifa{RESET}\n")
    elif option == 5:
        print(f"{GREEN}HISTORIAL DE GANADORES{RESET}\n")
        archivo = open("historial_rifa.txt", "r")
        lectura_archivo = archivo.read()
        print(lectura_archivo)
    else:
        print(f"{RED}Opción no valida{RESET}\n")