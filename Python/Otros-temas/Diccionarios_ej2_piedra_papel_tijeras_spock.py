# Kevin Rafael Díaz López - 12/11/2024
# Programa que muestra las películas que ha visto el usuario.

import random

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RED = "\033[31m" # Define el color rojo para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|¡BIENVENIDO A PIEDRA, PAPEL, TIJERA, SPOCK, LAGARTO!|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

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

# Función para determinar el ganador
def determinar_ganador(jugador, cpu):
    if jugador == cpu:
        return "Empate"
    elif cpu in rules[jugador]:
        return "Jugador"
    else:
        return "CPU"


# Función para mostrar el marcador
def mostrar_marcador():
    print("\nMarcador actual:")
    for key, value in scores.items():
        print(f"{key}: {value}")
    print()


# Inicio del programa
print("Opciones válidas: piedra, papel, tijera, spock, lagarto")
print("Escribe 'salir' para terminar el juego.")

while True:
    jugador = input("\nTu elección: ").lower()
    if jugador == "salir":
        break
    if jugador not in choices:
        print("Opción inválida. Intenta nuevamente.")
        continue

    cpu = random.choice(choices)
    print(f"La CPU eligió: {cpu}")

    ganador = determinar_ganador(jugador, cpu)
    if ganador == "Empate":
        scores["Empates"] += 1
        print("¡Es un empate!")
    elif ganador == "Jugador":
        scores["Jugador"] += 1
        print("¡Ganaste!")
    else:
        scores["CPU"] += 1
        print("¡La CPU gana!")

    mostrar_marcador()

print("\nGracias por jugar. ¡Hasta la próxima!")
mostrar_marcador()
