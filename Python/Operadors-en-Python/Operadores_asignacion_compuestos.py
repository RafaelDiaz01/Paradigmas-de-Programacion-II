# Kevin Rafael Díaz López - 17/10/2024
# Programa que muestra el uso de los operadores de asignación compuestos.

print("\n\t**PROGRAMA QUE MUESTRA EL USO DE LOS OPERADORES DE ASIGNACIÓN COMPUESTOS**")
print()  # Imprime una línea en blanco.

numero1 = float(input("Ingrese un número flotante: "))  # Lee un número decimal ingresado por el usuario y lo asigna a numero1.
numero2 = float(input("Ingrese otro número flotante: "))  # Lee otro número decimal ingresado por el usuario y lo asigna a numero2.
print() # Imprime una línea en blanco.

print(f"Numero1: {numero1}") # Imprime el valor de numero1.
print(f"Numero2: {numero2}") # Imprime el valor de numero2.
print() # Imprime una línea en blanco.

# Operador de asignación compuesto +=
numero1 += 4  # Suma 4 a numero1 y asigna el resultado a numero1 (equivale a numero1 = numero1 + 4).
print(f"El resultado de numero1 (+4) += es: {numero1}")

# Operador de asignación compuesto -=
numero2 -= 6  # Resta 6 a numero2 y asigna el resultado a numero2 (equivale a numero2 = numero2 - 6).
print(f"El resultado de numero2 (-6) -= es: {numero2}")

# Operador de asignación compuesto *=
numero1 *= 21  # Multiplica numero1 por 21 y asigna el resultado a numero1 (equivale a numero1 = numero1 * 21).
print(f"El resultado de numero1 (*21) *= es: {numero1}")

# Operador de asignación compuesto /=
numero2 /= 14  # Divide numero2 entre 14 y asigna el resultado a numero2 (equivale a numero2 = numero2 / 14).
print(f"El resultado de numero2 (/14) /= es: {numero2}")

# Operador de asignación compuesto %=
numero1 %= 2  # Calcula el resto de numero1 dividido por 2 y asigna el resultado a numero1.
print(f"El resultado de numero1 (%2) %= es: {numero1}")

# Operador de asignación compuesto **=
numero2 **= 2  # Eleva numero2 al cuadrado y asigna el resultado a numero2.
print(f"El resultado de numero2 (**2) **= es: {numero2}")

# Operador de asignación compuesto //=
numero2 //= 3  # Realiza la división entera de numero2 entre 3 y asigna el resultado a numero2.
print(f"El resultado de numero2 (//3) //= es: {numero2}")
