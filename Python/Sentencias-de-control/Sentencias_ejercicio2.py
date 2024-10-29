# Kevin Rafael Díaz López - 23/10/2024
# Programa que determina la estación del año dependiendo del mes.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"   # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PROGRAMA QUE DETERMINA LA ESTACIÓN DEL AÑO|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

mes = int((input("Ingrese el número de mes: "))) # Solicita al usuario ingresar el número de un mes.

if mes <= 0: # Verifica si el número ingresado es menor o igual a cero, lo cual no es un mes válido.
    print("Error, esa estación no existe")  # Muestra un mensaje de error si el número es menor o igual a 0.

elif mes < 3 or mes == 12: # Determina la estación "invierno" si el mes es enero, febrero (1 o 2), o diciembre (12).
    print("La estación es invierno")

elif mes < 6: # Determina la estación "primavera" si el mes está entre marzo y mayo (3 a 5).
    print("La estación es primavera")

elif mes < 9: # Determina la estación "verano" si el mes está entre junio y agosto (6 a 8).
    print("La estación es verano")

elif mes < 12: # Determina la estación "otoño" si el mes está entre septiembre y noviembre (9 a 11).
    print("La estación es otoño")

else: # Si el número es mayor a 12, indica un valor inválido.
    print("Incorrect")  # Muestra un mensaje de error si el número está fuera del rango de meses válidos.