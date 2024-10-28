# Kevin Rafael Díaz López - 22/10/2024
# Ejercicio que determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4).

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}| EXPRESIÓN BOOLEANA |{RESET}")  # Imprime el título del programa en color verde.
print(f" {GREEN}(exp1 O exp2) Y (exp3 O exp4){RESET}")
print()  # Imprime una línea en blanco.

# Solicita el valor de las cuatro expresiones booleanas al usuario.
exp1 = input("Ingresa un valor booleano (V/F): ")  # Pide al usuario el valor de exp1.
exp2 = input("Ingresa un valor booleano (V/F): ")  # Pide al usuario el valor de exp2.
exp3 = input("Ingresa un valor booleano (V/F): ")  # Pide al usuario el valor de exp3.
exp4 = input("Ingresa un valor booleano (V/F): ")  # Pide al usuario el valor de exp4.

# Evalúa si al menos una de las dos primeras expresiones (exp1 or exp2) es "V".
result = exp1 == "V" or exp2 == "V"  # Si exp1 o exp2 es "V", result será True.

# Evalúa si al menos una de las dos últimas expresiones (exp3 or exp4) es "V".
result2 = exp3 == "V" or exp4 == "V"  # Si exp3 o exp4 es "V", result2 será True.

# Muestra el resultado final de la expresión booleana (result and result2).
print(f"\nEl resultado de la expresión booleana es: {result and result2}")  # Imprime True si ambas condiciones result y result2 son verdaderas.
