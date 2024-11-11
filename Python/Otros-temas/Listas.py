# Kevin Rafael Díaz López - 07/11/2024
# Programa que muestra el uso de funciones mediante una calculadora básica en Python.

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|LISTAS|{RESET}\n")  # Imprime el título en color verde.

alumnos = [] # Lista vacía.
alumnos = ["Amelia", "Albert"] # Arreglo de cadenas.

print(alumnos) # Imprime la lista alumnos.

alumnos.append("Kevin") # Añade un elemento al final de la lista.
print(alumnos) # Imprime de nuevo la lista.

alumnos.append("Diana") # Agrega a "Diana", antes que a "Elton".

alumnos.insert(3, "Elton") # Añade un elemento en un índice específico. "Elton en el lugar de "Diana".
print(alumnos)

alumnos.insert(4, "Magdiel") # Añade a "Magdiel" entre "Elton" y "Diana".
alumnos.append("Eden")
alumnos.append("Sergio")

alumnos.insert(7, "Magdiel")
alumnos.insert(9, "Magdiel")
print(alumnos)

alumnos.remove("Magdiel") # Borra un elemento por su valor.
print(alumnos)

alumnos.pop(6)# Borra un elemento por su índice. Estilo de objetos.
print(alumnos)

del alumnos[7] # Otra manera de eliminar por índice.
print(alumnos)

alumnos.sort() # Ordena la lista en forma alfabética.
alumnos.sort(reverse=True) # Invierte la lista.

print(alumnos)
