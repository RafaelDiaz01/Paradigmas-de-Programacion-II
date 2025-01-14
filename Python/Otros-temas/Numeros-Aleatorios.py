# Kevin Rafael Díaz López - 10 / 12 / 24
# Programa que genera números aleatorios del 5 al 10

import random

while True:
    print(random.randint(5, 10))
    respuesta= input("¿Desea imprimir otro numero?")
    if respuesta == "no":
        break
