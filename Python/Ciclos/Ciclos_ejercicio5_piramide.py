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
    espacios = espacio * i # Multiplica el iterador por el espacio y lo almacena en espacios.
    asteriscos = asterisco * i # Multiplica el iterador por el asterisco y lo almacena en asteriscos.
    print(f"{asteriscos}{espacios}") # Imprime primero los asteriscos y luego los espacios.

print("\nPIRÁMIDE 2\n")
for i in range(filas+1):
    espacios = espacio * i # Multiplica el iterador por el espacio y lo almacena en espacios.
    asteriscos = asterisco * (filas-i) # Multiplica el resultado de (filas - iterador) por el asterisco y lo almacena en asteriscos.
    print(f"{asteriscos}{espacios}") # Imprime primero los asteriscos y luego los espacios.

print("PIRÁMIDE 3")
for i in range(filas+1):
    espacios = espacio * (filas-i) # Multiplica el espacio por (filas - iterador) y lo almacena en espacios.
    asteriscos = asterisco * ((2*i)-1) # Multiplica el asterisco por ((2 por iterador) - 1) y lo almacena en asteriscos.
    print(f"{espacios}{asteriscos}") # Imprime primero los espacios y luego los asteriscos.

print("\nPIRÁMIDE 4")
for i in range(filas+1):
    asteriscos = asterisco * i # Multiplica el asterisco por el iterador y lo almacena en asteriscos.
    espacios = espacio * (filas-i) # Multiplica el resultado de (filas - iterador) por el espacio y lo almacena en espacios.
    print(f"{espacios}{asteriscos}") # Imprime primero los espacios y luego los asteriscos.

