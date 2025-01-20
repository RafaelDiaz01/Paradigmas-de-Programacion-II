# Kevin Rafael Díaz López - 28/10/2024
# Programa que simula el juego en donde el usuario intenta adivinar un número secreto.
import random

archivo = open("historial_adivinador.txt", "w") # Crea el archivo de historial

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|JUEGO ADIVINADOR|{RESET}")  # Imprime el título del programa en color verde.
print("Tienes que adivinar un número entre 1 y 100\n") # Imprime las instrucciones del juego.

i = 1  # Inicializa la variable "i" en 1, que será el contador para el bucle.
cpu = random.randint(1, 100)  # Asigna un número random entre 1 y 100 a la variable "cpu".
archivo.write(f"Número Ganador: {cpu} \n")

while i <= 5:  # Bucle que se ejecuta mientras "i" sea menor o igual a 5.
    print(f"INTENTO {i}") # Muestra el número de intentos.
    intento = int(input("Ingrese un número: ")) # Solicita un número.
    archivo.write(f"Intento {i} = {intento} \n") # Escribe el intento en el archivo de historial.

    if intento == cpu: # Verifica si el número ingresado es igual a número secreto.
        print("\nG A N A S T E")
        print(f"¡Y solo necesitaste {i} intentos!") # Imprime el número de intentos ocupados.
        archivo.write(f"Intentos utilizados {i}/5 \n") # Escribe el número de intentos ocupados.
        break # Rompe el ciclo while
    elif intento < cpu: # Condición para darle una pista al usuario.
        print("El número a adivinar es mayor que el número ingresado\n")
    elif intento > cpu: # Condición para darle una pista al usuario.
        print("El número a adivinar es menor que el número ingresado\n")

    i += 1  # Incrementa el contador de intentos

# Condición para mostrar que el jugador ha perdido si no adivina en 5 intentos
if intento != cpu:
    print("P E R D I S T E")
    print(f"El número a adivinar era {cpu}")
    archivo.write(f"Intentos utilizados {i-1}/5 \n")

print(f"\n\t{GREEN}|FIN DEL JUEGO|{RESET}")  # Imprime el fin del programa en color verde.
