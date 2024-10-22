# Kevin Rafael Díaz López - 21/10/2024
# Ejercicio que muestra la conversión de cadenas a int, float y boolean mediante la interacción con consola.

print("****   Datos de los alumnos    *****") # Imprime un mensaje en consola, en especifico un encabezado.
nombre = input("Ingresa el nombre: ") # Solicita el nombre del alumno y almacena el valor como un string.
semestre = int(input("Ingresa el no. de semestre: ")) # La función anidada asegura que la entrada sea un número entero.
promedio = float(input("Ingresa el promedio: ")) # Solicita el promedio y lo convierte a float.
es_mujer = input("¿Es mujer (Si/No)?: ") # Solicita al usuario que indique si el alumno es mujer, ingresando "Si" o "No".
es_mujer = es_mujer.lower() == "si" # Convierte la respuesta de 'es_mujer' a minúsculas y compara si la respuesta es igual a "si".

print() # Salto de línea.

# {promedio:.2f} formatea el promedio para que se muestre con dos decimales y el valor de 'es_mujer' será 'True' si la respuesta fue "si" y 'False' si fue "no".
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")
