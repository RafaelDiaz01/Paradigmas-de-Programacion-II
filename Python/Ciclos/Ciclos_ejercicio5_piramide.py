# Kevin Rafael Díaz López - 07/11/2024
# Programa que imprime una pirámide mediante el uso de ciclos.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PIRÁMIDE|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

filas = int(input("Ingrese el número de filas: "))
print() # Imprime un salto de línea.
# Se definen las variables para el carácter del asterisco y el espacio.
asterisco = "*"
espacio = " "

print("PIRÁMIDE 1")
for i in range(filas+1):
    espacios = espacio * i
    asteriscos = asterisco * i
    print(f"{asteriscos}{espacios}")

print("\nPIRÁMIDE 2\n")
for i in range(filas+1):
    espacios = espacio * i
    asteriscos = asterisco * (filas-i)
    print(f"{asteriscos}{espacios}")

print("PIRÁMIDE 3")
for i in range(filas+1):
    espacios = espacio * (filas-i)
    asteriscos = asterisco * ((2*i)-1)
    print(f"{espacios}{asteriscos}")

print("\nPIRÁMIDE 4")
for i in range(filas+1):
    asteriscos = asterisco * i
    espacios = espacio * (filas-i)
    print(f"{espacios}{asteriscos}")

