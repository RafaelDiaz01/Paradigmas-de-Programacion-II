# Kevin Rafael Díaz López - 18/10/2024
# Programa que muestra el uso de los operadores relacionales en Python.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE MUESTRA EL USO DE LOS OPERADORES RELACIONALES|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Solicita al usuario ingresar dos números decimales.
numdecimal1 = float(input("Ingrese un número decimal: "))  # Lee un número decimal y lo asigna a numdecimal1.
numdecimal2 = float(input("Ingrese otro número decimal: "))  # Lee otro número decimal y lo asigna a numdecimal2.
print()  # Imprime una línea en blanco.

# Operador relacional "mayor que".
print(f"¿El número {numdecimal1:.2f} es mayor que {numdecimal2:.2f}?")  # Muestra la comparación en formato de pregunta.
mayor = numdecimal1 > numdecimal2  # Evalúa si numdecimal1 es mayor que numdecimal2 y almacena el resultado en mayor.
print(mayor)  # Imprime el resultado de la comparación.

# Operador relacional "mayor o igual que".
print(f"¿El número {numdecimal1:.2f} es mayor o igual que {numdecimal2:.2f}?")  # Pregunta si numdecimal1 es mayor o igual a numdecimal2.
mayorig = numdecimal1 >= numdecimal2  # Evalúa si numdecimal1 es mayor o igual que numdecimal2 y almacena el resultado en mayorig.
print(mayorig)  # Imprime el resultado de la comparación.

# Operador relacional "menor que".
print(f"¿El número {numdecimal1:.2f} es menor que {numdecimal2:.2f}?")  # Pregunta si numdecimal1 es menor que numdecimal2.
menor = numdecimal1 < numdecimal2  # Evalúa si numdecimal1 es menor que numdecimal2 y almacena el resultado en menor.
print(menor)  # Imprime el resultado de la comparación.

# Operador relacional "menor o igual que".
print(f"¿El número {numdecimal1:.2f} es menor o igual que {numdecimal2:.2f}?")  # Pregunta si numdecimal1 es menor o igual a numdecimal2.
menorig = numdecimal1 <= numdecimal2  # Evalúa si numdecimal1 es menor o igual que numdecimal2 y almacena el resultado en menorig.
print(menorig)  # Imprime el resultado de la comparación.

# Operador relacional "igual a".
print(f"¿El número {numdecimal1:.2f} es igual que {numdecimal2:.2f}?")  # Pregunta si numdecimal1 es igual a numdecimal2.
igual = numdecimal1 == numdecimal2  # Evalúa si numdecimal1 es igual a numdecimal2 y almacena el resultado en igual.
print(igual)  # Imprime el resultado de la comparación.

# Operador relacional "diferente de".
print(f"¿El número {numdecimal1:.2f} es diferente que {numdecimal2:.2f}?")  # Pregunta si numdecimal1 es diferente de numdecimal2.
dif = numdecimal1 != numdecimal2  # Evalúa si numdecimal1 es diferente de numdecimal2 y almacena el resultado en dif.
print(dif)  # Imprime el resultado de la comparación.
