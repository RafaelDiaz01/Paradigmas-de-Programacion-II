# Kevin Rafael Díaz López - 13/11/2024
# Programa que muestra el uso de los conjuntos (desordenados y mutables).

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|C O N J U N T O S|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

Conjunto1 = set() # Conjunto vacío.
Conjunto2 = {10, 5, 24, 11, 8, 7, 21, 9}
print(f"Conjunto 2: {Conjunto2}")

Conjunto1.add(80) # Añadir elementos
Conjunto1.add(111)
Conjunto1.add(10)
Conjunto1.add(5)
Conjunto1.add(24)
print(f"Conjunto 1: {Conjunto1}")

Conjunto1.remove(111) # Solo funciona si el elemento existe.
print(f"Conjunto 1 eliminando 111: {Conjunto1}")

Conjunto1.discard(10) # No genera error si el número no se encuentra en el conjunto.
print(f"Conjunto1 eliminando el 10 : {Conjunto1}")

conjunto_union = Conjunto1 | Conjunto2
print(f"\nUnión: {conjunto_union}")
conjunto_interseccion = Conjunto1 & Conjunto2
print(f"Intersección: {conjunto_interseccion}")

print() # Salto de línea.
alumnos_lista = ["Albert", "Kevin", "Elton", "Diana", "Rosendo", "Amelia", "Sergio", "Elton"]
alumnos_conjunto = set(alumnos_lista) # Transforma una lista a un conjunto.
print(f"Lista: {alumnos_lista}")
print(f"Conjunto: {alumnos_conjunto}")

nombre = input("\nIngrese un nombre: ")
nombre = nombre.strip() # strip() remueve los espacios iniciales y finales.
if nombre in alumnos_conjunto:
    print("Se encuentra en el conjunto")
else:
    print("Se añadió al conjunto")
alumnos_conjunto.add(nombre)
print(f"Conjunto: {alumnos_conjunto}")
