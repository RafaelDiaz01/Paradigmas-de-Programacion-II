# Kevin Rafael Díaz López
# Programa que realiza operaciones basicas.

print("\n\t**CALCULADORA BÁSICA**")
i = 0

while i != 7:
    print()
    print("[1] SUMA")
    print("[2] RESTA")
    print("[3] MULTIPLICACIÓN")
    print("[4] DIVISIÓN")
    print("[5] DIVISIÓN ENTERA")
    print("[6] EXPONENCIACIÓN")
    print("[7] SALIR")

    i = float(input("\nSeleccione su opción: "))
    if i == 7 :
        break
    else:
        numero1 = float(input("\nIngrese un número: "))
        numero2 = float(input("Ingrese un segundo número: "))

    if i == 1:
        print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}")
    elif i == 2:
        print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}")
    elif i == 3:
        print(f"La multiplicación de {numero1} y {numero2} es {numero1 * numero2}")
    elif i == 4:
        print(f"La división de {numero1} y {numero2} es {numero1 / numero2}")
    elif i == 5:
        print(f"La división entera de {numero1} y {numero2} es {numero1 // numero2}")
    elif i == 6:
        print(f"La exponenciación de {numero1} y {numero2} es {numero1 ** numero2}")
    else :
        print("ERROR, ESA OPCIÓN NO EXISTE\n")

print("S A L I S T E")