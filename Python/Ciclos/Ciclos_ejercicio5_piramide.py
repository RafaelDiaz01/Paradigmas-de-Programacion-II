# Kevin Rafael Díaz López - 07/11/2024
# Programa que imprime una piramide.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PIRAMIDE|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

filas = int(input("Ingrese el número de filas: "))
print() # Imprime un salto de línea.
asterisco = "*"
espacio = " "

print("PIRAMIDE 1")
for i in range(filas+1):
    espacios = espacio * i
    asteriscos = asterisco * i
    print(f"{asteriscos}{espacios}")

print("\nPIRAMIDE 2\n")
for i in range(filas+1):
    espacios = espacio * i
    asteriscos = asterisco * (filas-i)
    print(f"{asteriscos}{espacios}")

print("\nPIRAMIDE 4")
for i in range(filas+1):
    asteriscos = asterisco * i
    espacios = espacio * (filas-i)
    print(f"{espacios}{asteriscos}")

