# Kevin Rafael Díaz López - 20/01/2025
# Programa que simula el juego piedra, papel, tijeras, spock, lagarto utilizando diccionarios.

import random
import datetime

fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Fecha

# Códigos para dar color al texto.
GREEN = "\033[32m"  # Define el color verde para el texto.
RED = "\033[31m"  # Define el color rojo para el texto.
BLUE = "\033[34m"  # Define el color azul para el texto.
RESET = "\033[0m"  # Reinicia el color al original.

# Título del programa.
print(f"\n\t{GREEN}|¡BIENVENIDO A PIEDRA, PAPEL, TIJERA, SPOCK, LAGARTO!|{RESET}\n")

# Reglas del juego
rules = {
    "piedra": ["tijera", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijera": ["papel", "lagarto"],
    "spock": ["piedra", "tijera"],
    "lagarto": ["papel", "spock"]
}

# Inicialización del marcador
scores = {"Jugador": 0, "CPU": 0, "Empates": 0}

# Opciones válidas
choices = list(rules.keys())


def menu():
    print("[1] JUGAR")
    print("[2] HISTORIAL")
    print("[0] SALIR")


# Función para determinar el ganador
def determinar_ganador(jugador, cpu):
    if jugador == cpu:
        return "Empate"
    elif cpu in rules[jugador]:
        return "Jugador"
    else:
        return "CPU"

# Abre el archivo en modo escritura para borrar su contenido.
# Esto con el fin de que cualquier historial anterior sea borrado.
with open("historial_piedra.txt", "w") as archivo:
    pass  # No se escribe nada, lo que vacía el archivo.


i = 1

# Inicio del programa
while True:
    menu()  # Muestra el menú
    try:
        option = int(input("Seleccione la opción que desea realizar: "))
    except ValueError:
        print(f"{RED}Opción no válida. Por favor, ingrese un número.{RESET}\n")
        continue

    if option == 0:
        print(f"\n\t{RED}|SALISTE DEL PROGRAMA|{RESET}")
        break

    elif option == 1:  # Jugar
        print(f"\n{GREEN}Opciones válidas: piedra, papel, tijera, spock, lagarto{RESET}")
        jugador = input("Ingrese su elección: ").lower()
        if jugador not in choices:
            print(f"{RED}Opción inválida. Intenta nuevamente.{RESET}\n")
            continue

        cpu = random.choice(choices)
        print(f"La CPU eligió: {cpu}")

        ganador = determinar_ganador(jugador, cpu)
        if ganador == "Empate":
            scores["Empates"] += 1
            print(f"{BLUE}¡Es un empate!{RESET}\n")
        elif ganador == "Jugador":
            scores["Jugador"] += 1
            print(f"{GREEN}¡Ganaste!{RESET}\n")
        else:
            scores["CPU"] += 1
            print(f"{RED}¡La CPU gana!{RESET}\n")

        # Guardar en el historial
        with open("historial_piedra.txt", "a") as archivo:
            archivo.write(f"{GREEN}Partida {i} con fecha {fecha_hora}{RESET}\nJugador: {jugador}\nCPU: {cpu}\nGanador: {ganador}\n\n")
            i += 1

    elif option == 2:  # Historial
        print(f"\n{BLUE}--- HISTORIAL ---{RESET}")
        print(f"Victorias del jugador: {scores['Jugador']}")
        print(f"{RED}Victorias del CPU: {scores['CPU']}{RESET}")
        print(f"{BLUE}Empates: {scores['Empates']}{RESET}\n")
        try:
            with open("historial_piedra.txt", "r") as archivo:
                historial = archivo.read()
                if historial.strip():
                    print(historial)
                else:
                    print(f"{BLUE}El historial está vacío.{RESET}\n")
        except FileNotFoundError:
            print(f"{RED}No se encontró el archivo de historial.{RESET}\n")

    else:
        print(f"{RED}Opción no válida. Por favor, seleccione una opción válida.{RESET}\n")