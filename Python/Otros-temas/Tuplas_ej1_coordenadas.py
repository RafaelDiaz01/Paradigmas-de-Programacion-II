# Kevin Rafael Díaz López - 13/11/2024
# Programa que muestra el uso de tuplas (ordenadas e inmutables).

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RED = "\033[31m"  # Define el color rojo para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Título del programa.
print(f"\n\t{GREEN}|RECTAS A PARTIR DE PUNTOS EN EL PLANO CARTESIANO|{RESET}")  # Imprime el título del programa en color verde.
print()  # Imprime una línea en blanco.

# Funciones
def menu():
    print("----------------------------------------------------------------------")
    print("[1] VER COORDENADAS ALMACENADAS")
    print("[2] AGREGAR COORDENADA (X, Y)")
    print("[3] CALCULAR LA PENDIENTE Y LA ECUACIÓN DE LA RECTA ENTRE 2 COORDENADAS")
    print("[4] ELIMINAR COORDENADA (X, Y)")
    print("[0] SALIR")

def ver_coordenadas():
    if coordenadas:
        print("\nLISTA DE COORDENADAS:")
        for i, coordenada in enumerate(coordenadas, start=1):
            print(f"Coordenada {i}: {coordenada}")
    else:
        print("\nNO HAY COORDENADAS PARA MOSTRAR.\n")

def agregar(coordenadas):
    x = float(input("Ingrese el valor en la coordenada X: "))
    y = float(input("Ingrese el valor en la coordenada Y: "))
    nueva_coordenada = (x, y)
    print(f"La coordenada {nueva_coordenada} se agregó correctamente.\n")
    return coordenadas + (nueva_coordenada,)  # Devuelve una nueva tupla con la nueva coordenada.

def eliminar(coordenadas):
    ver_coordenadas()
    if coordenadas:
        try:
            indice = int(input("\nIngrese el número de la coordenada a eliminar: ")) - 1
            if 0 <= indice < len(coordenadas):
                coordenada_eliminada = coordenadas[indice]
                coordenadas = coordenadas[:indice] + coordenadas[indice + 1:]  # Elimina la coordenada.
                print(f"La coordenada {coordenada_eliminada} se eliminó correctamente.\n")
            else:
                print("ÍNDICE INVÁLIDO. Intente de nuevo.\n")
        except ValueError:
            print("ENTRADA INVÁLIDA. Intente de nuevo.\n")
    return coordenadas

def calcular_pendiente(coordenadas):
    if len(coordenadas) < 2:
        print("\nSE NECESITAN AL MENOS 2 COORDENADAS PARA CALCULAR LA PENDIENTE.\n")
        return
    ver_coordenadas()
    try:
        indice1 = int(input("\nSeleccione el número de la primera coordenada: ")) - 1
        indice2 = int(input("Seleccione el número de la segunda coordenada: ")) - 1
        if 0 <= indice1 < len(coordenadas) and 0 <= indice2 < len(coordenadas):
            x1, y1 = coordenadas[indice1]
            x2, y2 = coordenadas[indice2]
            if x2 != x1:
                pendiente = (y2 - y1) / (x2 - x1)
                print(f"\nPendiente: {pendiente}")
                print(f"Ecuación de la recta: y = {pendiente:.2f}x + {y1 - pendiente * x1:.2f}\n")
            else:
                print("\nLA RECTA ES VERTICAL (pendiente indefinida).\n")
        else:
            print("ÍNDICES INVÁLIDOS. Intente de nuevo.\n")
    except ValueError:
        print("ENTRADA INVÁLIDA. Intente de nuevo.\n")

# Código Principal
coordenadas = ()  # Define una tupla vacía.

while True:
    menu()  # Llama a la función menu.
    try:
        op = int(input("\n¿Qué desea realizar? "))
    except ValueError:
        print("Por favor, ingrese una opción válida.\n")
        continue

    if op == 0:
        print(f"\n\t{RED}|SALISTE DEL PROGRAMA|{RESET}")
        break

    elif op == 1:
        ver_coordenadas()

    elif op == 2:
        coordenadas = agregar(coordenadas)

    elif op == 3:
        calcular_pendiente(coordenadas)

    elif op == 4:
        coordenadas = eliminar(coordenadas)

    else:
        print("Opción no válida. Intente de nuevo.\n")
