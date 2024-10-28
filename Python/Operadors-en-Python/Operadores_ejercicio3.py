# Kevin Rafael Díaz López - 22/10/2024
# Ejercicio que verifica si el usuario y la contraseña son correctos.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}| SISTEMA DE AUTENTIFICACIÓN |{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

while True:
    usuario = input("Ingresa tu usuario: ") # Solicita el usuario.
    contraseña = input("Ingresa tu contraseña: ") # Solicita la contraseña.

    acceso_correcto = usuario == "Rafael" and contraseña == "spider" # Verifica si el usuario y la contraseña son correctos.
    print(f"¿El acceso es correcto? {acceso_correcto}") # Imprime el valor booleano de acceso_correcto.
    print()  # Imprime una línea en blanco.

    if acceso_correcto: # Si usuario y contraseña son correctas finaliza el bucle.
        print("\t| ACCESO CORRECTO |") # Imprime un letrero en consola.
        break  # Sale del bucle
