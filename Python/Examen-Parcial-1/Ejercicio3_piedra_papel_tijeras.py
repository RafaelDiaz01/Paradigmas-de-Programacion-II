# Kevin Rafael Díaz López - 28/10/2024
# Programa que simula el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatoria con la función randint().
import random
from random import randint

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|JUEGO DE PIEDRA, PAPEL O TIJERA|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Inicializa la variable 'i' que controla el menú.
i = 1

# Inicializa las variables para el historial de juegos jugados.
victorias = 0
empates = 0
victoriasCPU = 0

# Bucle principal que se ejecuta hasta que el usuario elija la opción de salir (0).
while i != 0:
    # Imprime el historial de juegos jugados.
    print(f"Victorias: {victorias} | Empates: {empates} | Victorias del CPU: {victoriasCPU} \n")

    # Imprime el menú de opciones.
    print("[1] PIEDRA")
    print("[2] PAPEL")
    print("[3] TIJERA")
    print("[0] SALIR")

    # Solicita al usuario una opción del menú y la guarda en 'i'.
    i = float(input("¿Qué desea realizar? "))

    # Opción para salir del programa.
    if i == 0:
        print("S A L I S T E ") # Finaliza el bucle y sale del programa

    # Opción cuando el jugador selecciona piedra.
    elif i == 1:
        cpu = random.randint(1,3) # Asigna un número random a la variable "cpu".

        if cpu == 2: # Si "cpu" es igual a 2 significa que es papel.
            print("Jugador: Piedra, CPU: Papel. LA CPU GANA ESTA RONDA") # Papel le gana a piedra.
            victoriasCPU += 1 # Incrementa en 1 el valor de la variable "victoriasCPU".
            print("---------------------------------------------\n") # Imprime una línea para dar formato al programa.
        elif cpu == 3: # Si "cpu" es igual a 3 significa que es tijera.
            print("Jugador: Piedra, CPU: Tijera. EL JUGADOR GANA ESTA RONDA") # Piedra le gana a tijera.
            victorias += 1 # Incrementa en 1 el valor de la variable "victorias".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.
        else : # Si "cpu" no fue ni 2 ni 3 significa que es piedra.
            print("Jugador: Piedra, CPU: Piedra. RONDA EMPATADA")  # Piedra no le gana a piedra, es empate.
            empates += 1 # Incrementa en 1 el valor de la variable "empates".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.

    # Opción cuando el jugador selecciona papel.
    elif i == 2:
        cpu = random.randint(1, 3)  # Asigna un número random a la variable "cpu".

        if cpu == 3:  # Si "cpu" es igual a 3 significa que es tijera.
            print("Jugador: Papel, CPU: Tijera. LA CPU GANA ESTA RONDA")  # Tijera le gana a papel.
            victoriasCPU += 1  # Incrementa en 1 el valor de la variable "victoriasCPU".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.
        elif cpu == 1:  # Si "cpu" es igual a 1 significa que es piedra.
            print("Jugador: Papel, CPU: Piedra. EL JUGADOR GANA ESTA RONDA")  # Papel le gana a piedra.
            victorias += 1  # Incrementa en 1 el valor de la variable "victorias".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.
        else:  # Si "cpu" no fue ni 3 ni 1 significa que es papel.
            print("Jugador: Papel, CPU: Papel. RONDA EMPATADA")  # Papel no le gana a papel, es empate.
            empates += 1  # Incrementa en 1 el valor de la variable "empates".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.

    # Opción cuando el jugador selecciona tijera.
    elif i == 3:
        cpu = random.randint(1, 3)  # Asigna un número random a la variable "cpu".

        if cpu == 1:  # Si "cpu" es igual a 1 significa que es piedra.
            print("Jugador: Tijera, CPU: Piedra. LA CPU GANA ESTA RONDA")  # Piedra le gana a tijera.
            victoriasCPU += 1  # Incrementa en 1 el valor de la variable "victoriasCPU".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.
        elif cpu == 2:  # Si "cpu" es igual a 2 significa que es papel.
            print("Jugador: Tijera, CPU: Papel. EL JUGADOR GANA ESTA RONDA")  # Tijera le gana a papel.
            victorias += 1  # Incrementa en 1 el valor de la variable "victorias".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.
        else:  # Si "cpu" no fue ni 1 ni 2 significa que es tijera.
            print("Jugador: Tijera, CPU: Tijera. RONDA EMPATADA")  # Tijera no le gana a tijera, es empate.
            empates += 1  # Incrementa en 1 el valor de la variable "empates".
            print("---------------------------------------------\n")  # Imprime una línea para dar formato al programa.

    # Muestra un mensaje de error si el usuario ingresa una opción no válida.
    else:
        print("POR FAVOR ELIJA UNA OPCIÓN VÁLIDA\n")