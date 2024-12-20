# Kevin Rafael Díaz López - 12/11/2024
# Programa que muestra una playlist de videos de YouTube.
from audioop import reverse

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RED = "\033[31m" # Define el color rojo para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|PLAYLIST DE VIDEO DE YOUTUBE|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Funciones
def menu():
    print("[1] VER PLAYLIST POR VIDEOS AÑADIDOS")
    print("[2] VER PLAYLIST ORDENADA DE LA A-Z")
    print("[3] VER PLAYLIST ORDENADA DE LA Z-A")
    print("[4] AÑADIR UN VIDEO DE YOUTUBE A LA PLAYLIST")
    print("[5] AÑADIR VARIOS VIDEOS DE YOUTUBE A LA PLAYLIST")
    print("[6] ELIMINAR VIDEO DE LA PLAYLIST")
    print("[0] SALIR")

def menu2():
    print("[1] POR NOMBRE DEL VIDEO")
    print("[2] POR ÍNDICE DE LISTA")
    print("[0] SALIR")


# Código Principal

pelis  = [] # Define una lista vacía.

while True:
    menu() # Llama a la función menu.
    op = int(input("\n¿Qué desea realizar? "))

    if op == 0:
        print(f"\n\t{RED}|SALISTE DEL PROGRAMA|{RESET}")
        break
    elif op == 1:
        if pelis:
            print(f"VIDEOS POR VER: {pelis}\n")
        else:
            print("NO HAY VIDEOS POR VER\n")
    elif op == 2:
        if pelis:
            pelis.sort() # Ordena la lista en forma alfabética.
            print(f"VIDEOS POR VER ORDENADOS DE LA A-Z: {pelis}\n") # Imprime la lista ordenada de la A - Z. Orden alfabético.
        else:
            print("NO HAY VIDEOS POR ORDENAR\n")
    elif op == 3:
        if pelis:
            pelis.sort(reverse=True) # Invierte la lista ordenada alfabéticamente.
            print(f"VIDEOS POR VER ORDENADOS DE LA Z-A: {pelis}\n") # Imprime la lista ordenada de Z - A.
        else :
            print("NO HAY VIDEOS POR ORDENAR\n")
    elif op == 4:
        agregar = input("¿Qué video desea añadir? ")
        pelis.append(agregar)
        print() # Imprime un salto de línea.
    elif op == 5:
        while True:
            agregar = input("¿Qué video desea añadir? ")
            pelis.append(agregar)
            condicion = input("¿Desea agregar otro video (Si/No) ?  ")
            condicion = condicion.lower()
            if condicion == "no":
                break
        print()  # Salto de línea.
    elif op == 6:
        print("\nMENU PARA ELIMINAR VIDEOS")
        while True:
            menu2() # Imprime el segundo menú.
            opcion = int(input("Elija su opción: "))

            if opcion == 0:
                print(f"{RED}|SALISTE DEL MENÚ ELIMINAR|{RESET}\n")
                break
            elif opcion == 1:
                if pelis:
                    elimina = input("¿Qué video desea eliminar? ")
                    if elimina in pelis:
                        pelis.remove(elimina)
                        print(f"Se eliminó correctamente {elimina}")
                    else:
                        print(f"{RED}|ERROR| NO EXISTE ESA VIDEO EN TU LISTA{RESET}")
                else:
                    print("NO HAY VIDEOS EXISTENTES\n")
            elif opcion == 2:
                if pelis:
                    elimina_indice = (int(input("¿Qué número de índice desea eliminar?"))) - 1  # Se le resta 1 para que el índice que se busca coincida correctamente.
                    size = len(pelis)
                    if size > elimina_indice >= 0:
                        pelis.pop(elimina_indice)
                        print(f"Se eliminó correctamente el video ubicado en el indice {elimina_indice + 1}\n")
                    else:
                        print(f"{RED}|ERROR| EL ÍNDICE INGRESADO NO ES CORRECTO{RESET}\n")
                else:
                    print("NO HAY VIDEOS EXISTENTES\n")
            else:
                print(f"{RED}Opción no válida{RESET}\n")
    else:
        print(f"{RED}Opción no valida{RESET}\n")