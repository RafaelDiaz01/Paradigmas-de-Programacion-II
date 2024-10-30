# Kevin Rafael Díaz López - 24/10/2024
# Programa que muestra el funcionamiento del Bucle While en Python.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE IMPRIME LOS NÚMEROS DESDE EL 1 HASTA UN TOPE|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

numero = int(input("Ingrese un número tope: "))  # Solicita un número entero.
i = 1  # Inicializa la variable "i" en 1, que será el contador para el primer bucle.
j = 0  # Inicializa la variable "j" en 0, que será el contador para el segundo bucle.

print(f"\nLos números del 1 al {numero} son: ")  # Muestra la lista de números.

while i <= numero:  # Bucle que se ejecuta mientras "i" sea menor o igual a "numero".
    print(i , end = " ")  # Imprime el valor de "i" en la misma línea, separado por un espacio.
    i = i + 1  # Incrementa "i" en 1 en cada iteración para avanzar al siguiente número.

print()  # Imprime una línea en blanco para separar los resultados.

# Imprime los números pares desde 0 hasta el número tope ingresado.
print(f"\nLos números pares del 0 al {numero} son: ")  # Muestra el encabezado de la lista de números pares.

while j <= numero:  # Bucle que se ejecuta mientras "j" sea menor o igual a "numero".
    if j % 2 == 0:  # Verifica si "j" es par.
        print(j, end = " ")  # Imprime el número par en la misma línea, separado por un espacio.
    j = j + 1  # Incrementa "j" en 1 en cada iteración para avanzar al siguiente número.

print("\nFin de la impresión")  # Imprime un mensaje indicando el fin del programa.
