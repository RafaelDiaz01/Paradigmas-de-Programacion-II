# Kevin Rafael Díaz López - 28/10/2024
# Programa que imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|LICENCIATURA EN INFORMÁRTICA|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

numero = int(input("Ingrese un número tope: "))  # Solicita un número entero.
i = 1  # Inicializa la variable "i" en 1, que será el contador para el bucle.

while i <= numero:  # Bucle que se ejecuta mientras "i" sea menor o igual a "numero".
    if i%3 == 0 and i%5 == 0: # Comprueba si es múltiplo de 3 o 5 (usando la lógica del módulo y el operador "and").
        print(end="Licenciatura en Informática, \n")
    elif i%3 == 0: # Comprueba si es múltiplo de 3.
        print(end = "Licenciatura, ")
    elif i%5 == 0: # Comprueba si es múltiplo de 5.
        print(end = "Informática, ")
    else: # Si no se cumplió ninguna condición, imprime el valor de "i".
        print(i , end = ", ")  # Imprime el valor de "i" en la misma línea, separado por una coma.
    i = i + 1  # Incrementa "i" en 1 en cada iteración para avanzar al siguiente número.


